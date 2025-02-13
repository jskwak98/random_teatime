from teatime_generator import TeaTimeGenerator

def print_menu():
    print("\n=== 티타임 생성기 ===")
    print("[1] 새로운 티타임 생성")
    print("    - 각 파트별 1-2명 랜덤 선택")
    print("    - 카페 및 날짜 선택")
    print("    - 팀장님 참석 여부 결정")
    print("[2] 로그 초기화")
    print("    - 이전 티타임 기록을 모두 삭제")
    print("    - 새로운 티타임 사이클 시작")
    print("[3] 종료 (Quit)")
    print("\n원하는 작업의 번호를 입력하세요.")

def main():
    generator = TeaTimeGenerator()
    
    while True:
        print_menu()
        choice = input("선택 (1-3): ")
        
        if choice == "1":
            result, error = generator.generate_teatime()
            if error:
                print(f"\n⚠️ 에러: {error}")
                input("\n계속하려면 Enter를 누르세요...")
                continue
                
            print("\n=== 생성된 티타임 ===")
            print(f"📅 날짜: {result['date']}")
            print(f"☕ 카페: {result['cafe']['name']}")
            print(f"🔗 위치: {result['cafe']['link']}")
            print(f"👥 팀장님 참석: {'예' if result['team_leader_joins'] else '아니오'}")
            print("\n참여자:")
            for p in result['participants']:
                print(f"- {p['name']} ({p['part']})")
            
            while True:
                save = input("\n이 결과를 저장하시겠습니까? (Y/N): ").lower()
                if save in ['y', 'n']:
                    break
                print("Y 또는 N을 입력해주세요.")

            if save == 'y':
                generator.save_result(result)
                print("\n✅ 저장되었습니다.")
            
            input("\n계속하려면 Enter를 누르세요...")
        
        elif choice == "2":
            while True:
                confirm = input("\n⚠️ 정말로 로그를 초기화하시겠습니까? (Y/N): ").lower()
                if confirm in ['y', 'n']:
                    break
                print("Y 또는 N을 입력해주세요.")

            if confirm == 'y':
                generator.reset_log()
                print("\n✅ 로그가 초기화되었습니다.")
            
            input("\n계속하려면 Enter를 누르세요...")
        
        elif choice == "3":
            print("\n프로그램을 종료합니다. 안녕히 가세요! 👋")
            break
        
        else:
            print("\n❌ 잘못된 선택입니다. 1-3 사이의 숫자를 입력해주세요.")
            input("\n계속하려면 Enter를 누르세요...")

if __name__ == "__main__":
    main() 