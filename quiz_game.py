from quiz import Quiz


class QuizGame:
    def __init__(self):
        self.best_score = 0

        self.quizzes = [
            Quiz(
                "Python의 창시자는?",
                [
                    "Guido van Rossum",
                    "Linus Torvalds",
                    "James Gosling",
                    "Dennis Ritchie"
                ],
                1
            ),
            Quiz(
                "Python에서 리스트를 만드는 기호는?",
                [
                    "()",
                    "{}",
                    "[]",
                    "<>"
                ],
                3
            )
        ]

    def show_menu(self):
        print("\n===== 나만의 퀴즈 게임 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 퀴즈 삭제")
        print("6. 종료")

    def play_quiz(self):
        score = 0

        for quiz in self.quizzes:
            quiz.display()

            answer = int(
                input("정답 번호: ")
            )

            if quiz.check_answer(answer):
                print("정답!")
                score += 1
            else:
                print("오답!")

        print(f"점수: {score}")

        if score > self.best_score:
            self.best_score = score

    def add_quiz(self):
        question = input("문제: ")

        choices = []

        for i in range(1, 5):
            choices.append(
                input(f"선택지 {i}: ")
            )

        answer = int(
            input("정답 번호: ")
        )

        self.quizzes.append(
            Quiz(
                question,
                choices,
                answer
            )
        )

        print("퀴즈 추가 완료")

    def show_quizzes(self):
        for i, quiz in enumerate(
            self.quizzes,
            start=1
        ):
            print(
                f"{i}. {quiz.question}"
            )

    def show_score(self):
        print(
            f"최고 점수 : {self.best_score}"
        )

    def delete_quiz(self):
        self.show_quizzes()

        number = int(
            input("삭제할 번호: ")
        )

        if 1 <= number <= len(self.quizzes):
            self.quizzes.pop(number - 1)

            print("삭제 완료")