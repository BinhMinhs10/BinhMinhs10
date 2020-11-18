class Vehicle:
    def __init__(self, horn, country):
        self.__horn = horn
        self._country = country


class Car(Vehicle):
    def __init__(self, horn, country):
        # private attributes
        self.__horn = horn
        # protected attributes
        self._country = country

    def __str__(self):
        return f"Car: {self.__horn}, {self._country!r}"

    def _move_to_center(self):
        print(f"The car ({self}) exhibit spot.")

    def _move_to_side(self):
        print(f"Move {self} back.")

    def __enter__(self):
        print("__enter__ is called")
        self._move_to_center()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__ is called")
        self._move_to_side()


if __name__ == "__main__":
    v1 = Vehicle("honda", "jp")
    v2 = Car("vinfast", "vn")
    print(v2.__dict__)
    # print(v2._country)

    # alter value of private attr
    v2._Car__horn = 'new car'
    print(v2.__dict__)

    print(v2)
    with v2:
        print("It's very good car")
