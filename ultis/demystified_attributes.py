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


if __name__ == "__main__":
    v1 = Vehicle("honda", "jp")
    v2 = Car("vinfast", "vn")
    print(v2.__dict__)
    # print(v2._country)

    # alter value of private attr
    v2._Car__horn = 'new car'
    print(v2.__dict__)
