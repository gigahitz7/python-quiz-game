from quiz import Quiz


class QuizGame:
    def __init__(self):
        self.quizzes = self.create_default_quizzes()
        self.best_score = 0

    def create_default_quizzes(self):
        return [
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
            ),
            Quiz(
                "True와 False의 자료형은?",
                [
                    "int",
                    "bool",
                    "float",
                    "dict"
                ],
                2
            ),
            Quiz(
                "함수를 정의할 때 사용하는 키워드는?",
                [
                    "func",
                    "define",
                    "def",
                    "class"
                ],
                3
            ),
            Quiz(
                "조건문에 사용하는 키워드는?",
                [
                    "if",
                    "for",
                    "while",
                    "class"
                ],
                1
            )
        ]

    def show_menu(self):
        print("\n===== 나만의 퀴즈 게임 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")

    def play_quiz(self):
        score = 0

        print("\n퀴즈를 시작합니다!")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[문제 {index}]")

            quiz.display()

            answer = input("정답 번호를 입력하세요: ")

            try:
                answer = int(answer)

                if quiz.check_answer(answer):
                    print("정답입니다!")
                    score += 1
                else:
                    print("오답입니다.")

            except ValueError:
                print("숫자를 입력하세요.")

        print(
            f"\n결과: {len(self.quizzes)}문제 중 "
            f"{score}문제 정답"
        )

        if score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다!")
