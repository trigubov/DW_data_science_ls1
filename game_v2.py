"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count

def algo_predict(number: int =1,min: int =1,max: int =100) -> int:
    """Угадываем число по алгоритму: каждая следущая попытка выбирает среднее число между предидущей
    неудачной попыткой, и максимальным/минимальным возможным вариантом

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        min (int, optional): Минимально возможное число. Defaults to 1.
        max (int, optional): Максимально возможное число. Defaults to 100.

    Returns:
        int: число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number = (min + max) // 2
        if number == predict_number:
            break  # выход из цикла если угадали
        elif predict_number > number: # задуманное число - меньше предсказанного
            max = predict_number - 1 # изменили верхнюю границу поиска
        elif predict_number < number: # задуманное число - больше предсказанного
            min = predict_number + 1 # изменили нижнюю границу поиска
            
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
