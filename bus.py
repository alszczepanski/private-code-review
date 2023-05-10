from vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, owner: str, color=None):
        super().__init__(owner, color)
        if not color:
            self.color = "yellow"
