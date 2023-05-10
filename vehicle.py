class Vehicle:
    """ Clas representing vehicle.
    """

    def __init__(self, owner: str, color: str):
        """_summary_

        Args:
            owner (str): The owner of the vehicle.
            color (str): The color of the vehicle.
        """
        self.owner = owner
        self.color = color

        def display(self):
            """Displays  vehicle info.
            """
            print(
                f"Type: {self.__class__.__name__}, Owner: {self.owner}, Color: {self.color}")
