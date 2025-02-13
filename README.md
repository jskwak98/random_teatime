# random_teatime
팀 내 랜덤 티타임 대상자 추출하기!

# 1. 데이터 세팅 예시
### 1. 카페 정보
```yaml
cafes:
  - name: "스타벅스 강남점"
    link: "https://naver.me/abc123"
    weight: 3  # 자주 가는 카페
  - name: "투썸플레이스 서초점"
    link: "https://naver.me/xyz789"
    weight: 2  # 보통
  - name: "블루보틀 삼성점"
    link: "https://naver.me/def456"
    weight: 1  # 가끔 가는 카페
settings:
  team_leader_weights:
    join: 3    # 팀장님 참여 확률 3/5
    skip: 2    # 불참 확률 2/5 
  participant_count_weights:
    one: 95    # 한 명 선택 확률 95%
    two: 5     # 두 명 선택 확률 5%
```

### 2. 멤버 정보
```yaml
members:
  - name: "홍길동"
    part: "백엔드"
    image: "images/hong.jpg"
  - name: "김철수"
    part: "프론트엔드"
    image: "images/kim.jpg"
  - name: "이영희"
    part: "디자인"
    image: "images/lee.jpg"
```