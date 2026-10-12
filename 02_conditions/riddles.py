"""Мини-игра с загадками: одна функция, которую вызываем с разными вопросами."""


def ask_riddle(question, answer):
    """Задаёт загадку и возвращает True, если ответ верный."""
    print("Внимание, загадка!", question)
    user_answer = input("> ").strip()
    if user_answer.lower() == answer.lower():
        print("Правильно!")
        return True
    print("Неверно! Правильный ответ:", answer)
    return False


riddles = [
    ("Не лёд, а тает, не лодка, а уплывает. Что это?", "Зарплата"),
    ("Кто всегда отвечает первым на вопрос «Кому лень?»", "Мне"),
]

score = sum(ask_riddle(question, answer) for question, answer in riddles)
print(f"Отгадано загадок: {score} из {len(riddles)}")
