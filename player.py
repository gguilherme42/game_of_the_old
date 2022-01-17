class Player():
    def __init__(self, name="User 1") -> None:
        self.name = name
        self.choices = []
        self.status: str = None

    def add_choice(self, choice: str):
        if choice.upper() in 'A1B1C1A2C2B2A3B3C3' and len(choice) == 2:
            self.choices.append(choice)
        