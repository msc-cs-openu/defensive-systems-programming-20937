class User:
    def __init__(self, name: str, profession: str) -> None:
        self.name: str = name
        self.profession: str = profession


class Engineer(User):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Engineer")


class Technician(User):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Technician")


class Politician(User):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Politician")


class ElectricalEngineer(Engineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.specialization: str = "Electrical Engineering"


class ComputerEngineer(Engineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.specialization: str = "Computer Engineering"


class MechanicalEngineer(Engineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.specialization: str = "Mechanical Engineering"


class ClassBuilder:
    def __init__(self, class_name: str, base_class_name: str, method_name: str, attribute_name: str) -> None:
        self.class_name: str = class_name
        self.base_class_name: str = base_class_name
        self.method_name: str = method_name
        self.attribute_name: str = attribute_name

    def generate_class(self) -> None:
        base_class = globals().get(self.base_class_name, object)
        new_class = type(self.class_name, (base_class,), {
            self.method_name: lambda self: f"{self.class_name} method called",
            self.attribute_name: None
        })
        globals()[self.class_name] = new_class
        print(f"Class {self.class_name} generated with base class {self.base_class_name}, method {self.method_name}, and attribute {self.attribute_name}.")

    def print_class(self) -> None:
        cls = globals().get(self.class_name)
        if cls:
            print(f"Class Name: {cls.__name__}")
            print(
                f"Base Class: {cls.__bases__[0].__name__ if cls.__bases__ else 'None'}")
            print(f"Class __name__ is: {cls.__name__}")
            print(f"Class __dict__ is: {cls.__dict__}")
        else:
            print(f"Class {self.class_name} not found.")


def main():
    print("Class Generation v1")

    while True:
        class_name = input("Please enter the name of new class: ")
        base_class_name = input(
            "Please enter name of base class (blank if none): ")
        method_name = input(
            f"Please enter name of new method for class {class_name}: ")
        attribute_name = input(
            f"Please enter name of new attribute for class {class_name}: ")

        builder = ClassBuilder(class_name, base_class_name,
                               method_name, attribute_name)

        try:
            builder.generate_class()
            builder.print_class()
        except Exception as e:
            print(f"Error generating class: {e}")


if __name__ == "__main__":
    main()
