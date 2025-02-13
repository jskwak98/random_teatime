import yaml
import json
import random
from datetime import datetime
from pathlib import Path
import os

class TeaTimeGenerator:
    def __init__(self):
        self.data_dir = Path("data")
        self.log_file = self.data_dir / "teatime_log.json"
        self.load_data()

    def load_data(self):
        # 멤버 데이터 로드
        with open(self.data_dir / "members.yaml", "r", encoding="utf-8") as f:
            self.members_data = yaml.safe_load(f)

        # 카페 데이터 로드
        with open(self.data_dir / "cafes.yaml", "r", encoding="utf-8") as f:
            self.cafes_data = yaml.safe_load(f)

        # 로그 데이터 로드
        if os.path.exists(self.log_file):
            with open(self.log_file, "r", encoding="utf-8") as f:
                self.log_data = json.load(f)
        else:
            self.log_data = []

    def get_available_members(self):
        used_members = set()
        if self.log_data:
            for entry in self.log_data:
                for member in entry["participants"]:
                    used_members.add(member["name"])
        
        return [m for m in self.members_data["members"] 
                if m["name"] not in used_members]

    def generate_teatime(self):
        # 사용 가능한 멤버 확인
        available_members = self.get_available_members()
        if not available_members:
            return None, "모든 멤버가 이미 참여했습니다. 리셋이 필요합니다."

        # 파트별로 멤버 그룹화
        members_by_part = {}
        for member in available_members:
            if member["part"] not in members_by_part:
                members_by_part[member["part"]] = []
            members_by_part[member["part"]].append(member)

        # 각 파트에서 1-2명 선택 (가중치 기반)
        selected_members = []
        weights = self.cafes_data['settings']['participant_count_weights']
        for part, members in members_by_part.items():
            if members:
                # 가중치 기반으로 선택할 인원 수 결정
                num_to_select = random.choices(
                    [1, 2],
                    weights=[weights['one'], weights['two']],
                    k=1
                )[0]
                num_to_select = min(num_to_select, len(members))  # 가용 인원보다 많이 선택하지 않도록
                selected = random.sample(members, num_to_select)
                selected_members.extend(selected)

        # 날짜, 카페, 팀장 참여 여부 선택
        weekdays = ["월", "화", "수", "목", "금"]
        selected_day = random.choice(weekdays)

        # 가중치 기반 카페 선택
        cafe_weights = [cafe['weight'] for cafe in self.cafes_data['cafes']]
        selected_cafe = random.choices(
            self.cafes_data['cafes'],
            weights=cafe_weights,
            k=1
        )[0]

        # 가중치 기반 팀장 참여 여부 선택
        team_leader_weights = self.cafes_data['settings']['team_leader_weights']
        team_leader_joins = random.choices(
            [True, False],
            weights=[team_leader_weights['join'], team_leader_weights['skip']],
            k=1
        )[0]

        result = {
            "date": selected_day,
            "cafe": selected_cafe,
            "team_leader_joins": team_leader_joins,
            "participants": selected_members,
            "timestamp": datetime.now().isoformat()
        }

        return result, None

    def save_result(self, result):
        self.log_data.append(result)
        with open(self.log_file, "w", encoding="utf-8") as f:
            json.dump(self.log_data, f, ensure_ascii=False, indent=2)

    def reset_log(self):
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
        self.log_data = [] 