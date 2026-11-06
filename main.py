from quiz_game import QuizGame


def main():
    game = QuizGame()

    while True:
        game.show_menu()

        choice = input("선택: ")

        if choice == "1":
            game.play_quiz()

        elif choice == "5":
            print("프로그램을 종료합니다.")
            break


if __name__ == "__main__":
    main()