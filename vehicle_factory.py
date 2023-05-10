import json
import gc
import importlib


class VehicleFactory:
    """ Class designed to create and initialize various vehicles. It takes list of JSON configs as input.
    """
    configuration = None
    produced_vehicles = []

    def __init__(self, configuration=None):
        """ Initializes VehicleFactory. Has two ways of initializing: 
                a) with empty config list 
                b) with list of vehicle parameters represented by dictionaries. 

        Args:
            configuration (list): List of dictionaries representing vehicle params.
        """
        if configuration:
            self.configuration = configuration

    def display(self):
        """Displays vehicles produced by factory.

        Returns:
            list: List of dictionaries representing vehicles.
        """
        return [self._prepare_json(vehicle) for vehicle in self.produced_vehicles]

    def save_to_file(self, filename: str):
        """Saves vehicles produced by factory to file. Provide only filename, without extension.

        Args:
            filename (str): Desired filename to save into.
        """
        vehicles_to_save = json.dumps(self.display())
        with open(f"{filename}.json", "w") as output_file:
            json.dump(vehicles_to_save, output_file)

    def load_configuration_from_file(self, filename: str):
        """Loads configuration list from file. Provide only filename, without extension.

        Args:
            filename (str): Name of the file load.
        """
        with open(f"{filename}.json", "r") as input_file:
            json_str = json.load(input_file)
            self.configuration = json.loads(json_str)

    def run_factory(self):
        """Creates vehicles from VehicleFactory.configuration.

        Returns:
            list: List of created vehicle objects.
        """
        return [self._create_vehicle(vehicle["type"], vehicle["owner"], vehicle["color"]) for vehicle in self.configuration]

    def _create_vehicle(self, vehicle_type: str, owner: str, color: str):
        """Creates vehicle object.

        Args:
            vehicle_type (str): Desired Vehicle type, possible options: Bus, Truck.
            owner (str): Owner of the vehicle.
            color (str): Color of the vehicle.

        Returns:
            Object: Returned object type depends on the vehicle_type.
        """
        vehicle_module = importlib.import_module(
            name=f"{vehicle_type.lower()}")
        class_ = getattr(vehicle_module, vehicle_type)
        vehicle = class_(owner=owner, color=color)
        self.produced_vehicles.append(vehicle)
        return vehicle

    def _prepare_json(self, vehicle: object):
        """Creates dictionary from vehicle.

        Args:
            vehicle (object): Provided vehicle object to serialize.

        Returns:
            dict: Dictionary with serialized object data.
        """
        return {
            "type": vehicle.__class__.__name__,
            "owner": vehicle.owner,
            "color": vehicle.color
        }
