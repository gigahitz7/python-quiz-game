import json
import os

from quiz import Quiz


class QuizGame:
    def __init__(self):
        self.quizzes = self.create_default_quizzes()
        self.best_score = 0

        self.load_data()

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

            try:
                answer = int(
                    input("정답 번호를 입력하세요: ")
                )

                if quiz.check_answer(answer):
                    print("정답입니다!")
                    score += 1
                else:
                    print(
                        f"오답입니다. 정답은 {quiz.answer}번입니다."
                    )

            except ValueError:
                print("숫자를 입력하세요.")

        print(
            f"\n결과 : {len(self.quizzes)}문제 중 "
            f"{score}문제 정답"
        )

        if score > self.best_score:
            self.best_score = score
            self.save_data()

            print("새로운 최고 점수입니다!")

    def add_quiz(self):
        print("\n새로운 퀴즈를 추가합니다.")

        question = input("문제 : ")

        choices = []

        for i in range(1, 5):
            choice = input(
                f"선택지 {i} : "
            )
            choices.append(choice)

        answer = int(
            input("정답 번호 (1~4): ")
        )

        new_quiz = Quiz(
            question,
            choices,
            answer
        )

        self.quizzes.append(new_quiz)

        self.save_data()

        print("퀴즈가 추가되었습니다.")

    def show_quizzes(self):
        print("\n===== 등록된 퀴즈 =====")

        for index, quiz in enumerate(
                self.quizzes,
                start=1):
            print(
                f"{index}. {quiz.question}"
            )

    def show_score(self):
        print(
            f"\n최고 점수 : "
            f"{self.best_score}"
        )

    def save_data(self):
        data = {
            "quizzes": [
                quiz.to_dict()
                for quiz in self.quizzes
            ],
            "best_score": self.best_score
        }

        with open(
                "state.json",
                "w",
                encoding="utf-8") as file:

            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

    def load_data(self):
        if not os.path.exists("state.json"):
            return

        try:
            with open(
                    "state.json",
                    "r",
                    encoding="utf-8") as file:

                data = json.load(file)

            self.best_score = data.get(
                "best_score",
                0
            )

            self.quizzes = []

            for item in data.get(
                    "quizzes",
                    []
            ):
                self.quizzes.append(
                    Quiz(
                        item["question"],
                        item["choices"],
                        item["answer"]
                    )
                )

        except Exception:
            print(
                "저장 파일이 손상되었습니다."
            )
