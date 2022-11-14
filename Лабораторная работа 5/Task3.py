from random import choice
def get_unique_list_numbers(beginning_: int, end_: int, amount_: int) -> list[int]:
    if end_ - beginning_ + 1 < amount_:
        raise ValueError("Невозможно создать список, так как уникальных значений в заданном диаппозоне меньше чем требуется для создания списка")
    ans = []
    numbers = list(range(beginning_, end_+1))
    for _ in range(amount_):
        chosenn = choice(numbers)
        ans.append(chosenn)
        numbers.remove(chosenn)
    return ans
    # TODO написать функцию для получения списка уникальных целых чисел



list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
