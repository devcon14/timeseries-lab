class Human:
    name: str
    eyes: int = 2
    legs: int = 2
    arms: int = 2
    heads: int = 1
    nose: int = 1

    def __init__(self, name: str):
        self.name = name


def hello(human: Human) -> str:
    return f"hello {human.name}"


def untyped_hello(name):
    return f"hello {name}"


conal = Human("Conal")
hello(conal)
untyped_hello("Conal")

st1 = "this is a string"
st2 = "this is a string"
