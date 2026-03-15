class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._age = age
        self._height = height
        print(f"Plant created: {name}")

    def set_height(self, height: int) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            h = height
            print(f"\nInvalid operation attempted: height {h}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self) -> str:
        return f"{self._height}cm"

    def get_age(self) -> str:
        return f"{self._age} days"

    def get_name(self) -> str:
        return self._name


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    P = SecurePlant("Rose", 25, 30)
    P.set_height(25)
    P.set_age(30)
    P.set_height(-5)
    print(f"\nCurrent plant: {P.get_name()} ({P.get_height()}, {P.get_age()})")


if __name__ == "__main__":
    ft_garden_security()
