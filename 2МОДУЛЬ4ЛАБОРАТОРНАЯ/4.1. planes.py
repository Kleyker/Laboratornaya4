if __name__ == "__main__":
    class Plane:
        """Базовый класс Самолёт"""

        def __init__(self, brand: str, model: str):
            self.brand = brand
            self.model = model

        def fly(self):
            """Метод полёта самолета"""
            return f'{self.__class__.__name__} {self.brand} {self.model} летит по небу'

        def __str__(self) -> str:
            return f'{self.__class__.__name__}: {self.brand} {self.model}'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}({self.brand!r}, {self.model!r})'

    class CargoPlane(Plane):
        """Дочерний класс Грузовой самолет"""

        def __init__(self, brand: str, model: str, cargo_capacity: int = 60000):
            super().__init__(brand, model)
            self.cargo_capacity = cargo_capacity

        def fly(self):
            """Перегрузка метода fly для грузового самолета"""
            return f'{self.__class__.__name__} {self.brand} {self.model} летит с весом груза {self.cargo_capacity} кг'

        def __repr__(self):
            return f'{self.__class__.__name__}({self.brand!r}, {self.model!r}, {self.cargo_capacity!r})'

    print(CargoPlane('Ан','22').fly())


    class PassengerPlane(Plane):
        """Дочерний класс Пассажирский самолет"""

        def __init__(self, brand: str, model: str, passengers: int = 200):
            super().__init__(brand, model)
            self.passengers = passengers

        def fly(self):
            """Перегрузка метода fly для пассажирского самолета"""
            return f'{self.__class__.__name__} {self.brand} {self.model} летит с {self.passengers} пассажирами на борту'

        def __repr__(self):
            return f'{self.__class__.__name__}({self.brand!r}, {self.model!r}, {self.passengers!r})'


    print(PassengerPlane('Boeing', '777').fly())
    pass
