import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом делим пополам диапозон возможных чисел, до тех пор пока не найдем загаданное число.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    #создаем контрольные точки минимума и максимума
    predict_min = 0 
    predict_max = 0
    while number != predict:
        count += 1
        if number > predict:
            if predict_max > 0:
                predict_min = predict
                predict = int(predict_min+(predict_max - predict_min)/2)
            else:
                predict_min = predict
                predict = int(predict + (100 - predict_min)/2)
        elif number < predict:
            predict_max = predict
            predict = int(predict_min+(predict_max - predict_min)/2)

    return count
    
print(f'Количество попыток: {game_core_v3()}')
   