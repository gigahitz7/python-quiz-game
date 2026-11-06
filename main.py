from quiz_game import QuizGame


def main():
    game = QuizGame()

    while True:
        print("\n===== 나만의 퀴즈 게임 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")

        choice = input("선택: ")

        if choice == "5":
            print("프로그램을 종료합니다.")
            break


if __name__ == "__main__":
    main()