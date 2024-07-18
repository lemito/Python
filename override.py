from collections import deque


class Animal:
    """Класс животные.

    Содержит:
        name(str): имя.
        weight(float) вес.

    Raises:
        ValueError: Атрибут инициализации либо строка, либо float, либо kwargs, либо без аргументов (по умолчанию name='default', weight=0.0)

    Returns:
        class Animal: класс животных
    """

    weight: float
    name: str

    def __init__(self, *args: tuple | list, **kwargs: dict) -> None:
        """_summary_

        Args:
            name (Optional[str]): имя...
            weight (Optional[float]):вес...
        """

        print(args)

        if len(kwargs) != 0:
            self.name = kwargs.get("name")
            self.weight = kwargs.get("weight")
        else:
            if len(args) == 0:
                name = "default"
                weight = 0.0
            elif isinstance(args[0], str) and isinstance(args[1], float):
                name = args[0]
                weight = args[1]
            elif isinstance(args[0], float) and isinstance(args[1], str):
                name = args[1]
                weight = args[0]

            elif isinstance(args[0], float):
                weight = args[0]
                name = "default"
            elif isinstance(args[0], str):
                weight = 0.0
                name = args[0]
            else:
                raise ValueError(
                    "Атрибут либо строка, либо float, либо kwargs, либо без аргументов (по умолчанию name='default', weight=0.0)"
                )

            self.name = name
            self.weight = weight

    def getName(self):
        return self.name

    def sound(self):
        print("Животное издает звук...")

    def __repr__(self) -> str:
        return f"Animal [Name = {self.name}, weight = {self.weight}]"


class Dog(Animal):
    poroda: str

    def __init__(self, name, weight, poroda: str) -> None:
        super().__init__(name, weight)
        self.poroda = poroda

    def sound(self):
        super().sound()
        print("Собака гаввкает...")


d = Dog("qq", 5.25, "Corgie")
a1 = Animal()
a2 = Animal("qq", 5.25)
a3 = Animal(name="qqqq", weight=5.25)
meow = ["werhgfddfg", "sfddf"]
qq = deque()
qq.append(1)
qq.append(2)
a3 = Animal(meow, qq)
print(a1.__repr__)
print(a2.__repr__)
print(a3.__repr__)
d.sound()
