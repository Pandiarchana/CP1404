class Band:
    def __init__(self, name):
        self.name = name
        self.instruments = []

    def __str__(self):
        return f"{self.name}({', '.join(self.instruments)})"

    def add_instrument(self, instrument):
        self.instruments.append(instrument)

    def play(self):
        if not self.instruments:
            print(f"{self.name} needs an instrument!")
        else:
            print(f"{self.name} is playing: {self.instruments[0]}")


if __name__ == "__main__":
    bands = [
        Band("Band 1"),
        Band("Band 2"),
        Band("Band 3")
    ]

    bands[0].add_instrument("Guitar")
    bands[1].add_instrument("Drums")

    for band in bands:
        band.play()
