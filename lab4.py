import doctest

class Criminal:
    def __init__(self, name: str, status: str):
        """
        Создание объекта "Преступник"
        :param name: имя преступника
        :param status: в розыске или пойман

        Примеры:
        >>> criminal = Criminal('Daniel', 'cought')
        """
        if not isinstance(status, str):
            raise TypeError
        self.status = status
        self.name = name

    def change_status(self) -> str:
        """
        Меняет статус пресступника, после того как его поймали
        :return: Cought
        """
        ...

    def __str__(self) -> str:
        return f"Имя {self.name}. Статус {self.status}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, status = {self.status!r})"


class Thief(Criminal):
    def __init__(self, name: str, status: str, damage: int):
        """
        Создание объекта "Вор"
        :param name: имя преступника
        :param status: в розыске или пойман
        :param damage: размер ущерба в рублях

        Примеры:
        >>> thief = Thief('Daniel', 'cought', 200000)
        """
        super().__init__(name, status)
        if not isinstance(damage, int):
            raise TypeError
        self.damage = damage

    def determin_punishment(self, damage: int) -> str:
        """
        Определяет наказание по размеру ущерба
        :param damage: размер ущерба кражи
        :return: выводит статью наказания
        Пример:
        >>> thief = Thief('Daniel', 'Wanted', '200000')
        >>> vaultdoor.open_door('2000000')
        """
        ...

    def __str__(self) -> str:
        return f"Имя {self.name}. Статус {self.status}. Ущерб {self.damage}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, status = {self.status!r}), damage = {self.damage})"


if __name__ == "__main__":
    doctest.testmod()
    pass

