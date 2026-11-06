from quiz_game import QuizGame


def main():
    game = QuizGame()

    while True:
        game.show_menu()

        choice = input("선택: ")

        if choice == "1":
            game.play_quiz()

        elif choice == "2":
            game.add_quiz()

        elif choice == "3":
            game.show_quizzes()

        elif choice == "4":
            game.show_score()

        elif choice == "5":
            game.save_data()

            print("프로그램을 종료합니다.")
            break

        else:
            print(
                "1~5 사이 숫자를 입력하세요."
            )


if __name__ == "__main__":
    main()