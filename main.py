import random
"""
Практическая работа: Создание игры «Виселица»

Цель: Научиться применять основы алгоритмизации и программирования, включая использование циклов, условных конструкций, работы со строками и списками.
Задачи для выполнения:

    Создать базовую структуру программы
        Определите основную цель игры и опишите её в комментариях.
        Подсказка: Используйте функцию def main(): как точку входа в вашу программу.

    Подготовить список слов
        Создайте массив (список) из нескольких слов, которые будут использоваться в игре.
        Подсказка: Для начала можете использовать 5–10 слов, чтобы протестировать программу.

    Выбор случайного слова
        Программа должна выбирать случайное слово из списка при каждом запуске.
        Подсказка: Используйте модуль random и функцию random.choice().

    Реализовать отображение текущего состояния слова
        Добавьте отображение текущего состояния угадывания: например, "слово: _ _ _ _".
        Подсказка: Используйте строки или списки для хранения угаданных символов.

    Обработка ввода пользователя
        Добавьте запрос ввода одной буквы от игрока.
        Подсказка: Проверьте корректность ввода — игрок должен вводить только одну букву.

    Проверка буквы
        Реализуйте проверку, есть ли введённая буква в загаданном слове.
        Подсказка: Используйте цикл for, чтобы пройтись по всем символам загаданного слова.

    Обновление состояния игры
        Если буква угадана, обновите текущее состояние слова.
        Если буква не угадана, уменьшите количество оставшихся попыток.
        Подсказка: Используйте переменную для отслеживания оставшихся попыток.

    Отображение виселицы
        Реализуйте визуальное отображение виселицы, которое обновляется с каждой ошибкой.
        Подсказка: Используйте список строк (HANGMANPICS), где каждая строка — новая стадия виселицы.

    Проверка окончания игры
        Добавьте проверку, угадал ли игрок слово или закончились попытки.
        Подсказка: Используйте условные конструкции if для проверки победы или поражения.

    Реализовать повтор игры
        После окончания игры предложите игроку сыграть снова.
        Подсказка: Используйте цикл while и запрос на ввод "Хотите сыграть снова? (да/нет)".
"""
import random
HANGMANPICS = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]

COMMON_NOUNS = [
    "время",
    "человек",
    "год",
    "дело",
    "день",
    "рука",
    "раз",
    "город",
    "слово",
    "место",
    "лицо",
    "друг",
    "глаз",
    "вопрос",
    "дом",
    "сторона",
    "страна",
    "мир",
    "случай",
    "голова",
    "ребёнок",
    "сила",
    "конец",
    "вид",
    "система",
    "часть",
    "работа",
    "жизнь",
    "власть",
    "женщина",
    "дорога",
    "образ",
    "отец",
    "история",
    "нога",
    "вода",
    "война",
    "любовь",
    "минута",
    "право",
    "небо",
    "сын",
    "душа",
    "утро",
    "вечер",
    "месяц",
    "комната",
    "ночь",
    "мать",
    "утро",
    "вещь",
    "цель",
    "народ",
    "сердце",
    "шаг",
    "девушка",
    "машина",
    "уровень",
    "окно",
    "ответ",
    "условие",
    "начало",
    "свет",
    "действие",
    "век",
    "школа",
    "газета",
    "плечо",
    "путь",
    "дверь",
    "язык",
    "любовь",
    "порядок",
    "автор",
    "гость",
    "закон",
    "число",
    "идея",
    "смерть",
    "сон",
    "ресурс",
    "лес",
    "проблема",
    "искусство",
    "река",
    "проект",
    "журнал",
    "стена",
    "товарищ",
    "книга",
    "письмо",
    "помощь",
    "группа",
    "участие",
]

# основаня цель игры: программа рисует картинку, похожую на виселицу с человеком, используя символы
def main(): 
    answer = list(random.choice(COMMON_NOUNS))
    print("".join(answer)) 
    at = 0
    playfield = []
    for i in answer:
        playfield.append("_")
  
    while True:
        print("слово:")
        print("".join(playfield))
        x = input("Введите букву: ")

        if len(x) > 1:
            print("Введите одну букву")
            continue

        for i in range (len(answer)):
            if x == answer[i]:
                playfield[i] = x
      
        if answer == playfield:
            print("Вы угадали!")
            break

        if x in answer:
            continue
        else:
            print(HANGMANPICS[at])
            at += 1
    
        if at == 7:
            print("Вы проиграли!")
            break


while True:
    user = input("Хотите сыграть еще раз? (да\нет): ")
    if user == 'да':
       main()
    elif user == 'нет':
       print('Спасибо за игру!')
       break
    else:
       print("Выберите один вариант ответа") 
