import time
# ------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Введите ваш ответ:")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)
# ------------------------
def check_answer(answer,guess):
    if answer == guess:
        print("Правильно!")
        return 1
    else:
        print("Неправильно!")
        return 0
# ------------------------
def display_score(correct_guesses, guesses):
    print("------------------------")
    print("ВОТ И РЕЗУЛЬТАТЫ ПОДЪЕХАЛИ")
    print("------------------------")
    print("Правильные ответы: ", end=" ")
    for i in questions:
        time.sleep(1)
        print(questions.get(i), end="")
    print()

    print("Ваши ответы: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Правильных ответов: "+str(score)+"%")
# ------------------------
def play_again():
    responce = input("Хотите начать заново (ДА или НЕТ)? ")
    responce = responce.upper()
    if responce == "YES":
        return True
    else:
        return False
# ------------------------
questions = {"Чей Крым? ": "A",
             "Семен воняет? ": "B",
             "2+2?": "C"
             }

options = [["A. Украины","B. Америки","C. Эфиопии"],
           ["A. Да","B. Нет"],
           ["A. 5","B. 4","C. Бублик","D. Я гуманитарий"]]

new_game()

while play_again():
    new_game()

print("Пока бобик")