class a():
    def __init__(self) -> None:
        self.a = 10

with open("example.txt", "w") as f:
    f.write(str(a()))