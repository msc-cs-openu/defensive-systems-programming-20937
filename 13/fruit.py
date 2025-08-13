class AppleBasket:
    apple_quantity: int
    apple_color: str

    def __init__(self, quantity: int, color: str) -> None:
        self.apple_quantity: int = quantity
        self.apple_color: str = color

    def __str__(self) -> str:
        return f"A basket of {self.apple_quantity} {self.apple_color} apples."

    def increase(self) -> None:
        self.apple_quantity += 1


class GreenAppleBasket(AppleBasket):
    def __init__(self, quantity: int) -> None:
        super().__init__(quantity, "Green")


def main():
    print("------------------ Section A ------------------")
    print(f"Example1:  {AppleBasket(2, 'red')}")
    print(f"Example2:  {AppleBasket(3, 'blue')}")
    print("------------------ Section B ------------------")
    print(f"Example3:  {GreenAppleBasket(1)}")


if __name__ == '__main__':
    main()
