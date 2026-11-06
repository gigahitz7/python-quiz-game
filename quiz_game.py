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