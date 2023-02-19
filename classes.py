import doctest


class Bookcase:
    def __init__(self, color: None, heigh: float):
        #создание и подготовка к работе книжный шкаф

        ...
    def does_bookcase_fit_a_room(self, room_heigh: float) -> None:
        ...#помещается ли шкаф в комнату
    def repaint(self, new_color: None) -> None:
        #перекрасить шкаф
        ...
class Vase:
    def __init__(self, number_of_Flowers: float, volume_of_water: float):
        #создание и подготовка к работе ваза
        ...
    def put_flowers(self, new_flowers: float) -> float:
        ... #постивать цветы в вазу, если ваза пустая
    def add_water(self, water: float)->None:
        ... #добавить воду в вазу


class Site:
    def __init__(self, daily_numbers_of_visitor: float, name: None):
        ... #создание и подготовка к работе Сайт
    def compare_daily_numbers_of_visitors_with_wishes(self,wish_numbers_of_visitors: float) -> float:
        ... #сравнить количество посетителей сайта с желаемым, дать ответ в проценжх
    def rename_site(self, new_name: None)-> None:
        ... #переименовать сайт
if __name__ == "__main__":
    doctest.testmod() # тестирование примеров, которые находятся в документации
