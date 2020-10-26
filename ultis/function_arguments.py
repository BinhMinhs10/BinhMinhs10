# two special symbols use when not sure number args
# 1. *args(Non keyword arguments)
# 2. **Kwargs (Keyword Arguments)

def adder(*num):
    sum_ = 0
    for n in num:
        sum_ = sum_ + n
    print("Sum:", sum_)


def intro(**data):
    print("\nData type of argument:", type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))


if __name__ == "__main__":
    adder(3, 5, 7)
    intro(Name="Minh", Age=23, Email="bkbinhminh9x@gmail.com")


