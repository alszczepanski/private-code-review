# I etap:
# Stworzyć klasę Vehicle oraz dwie klasy pochodne Truck i Bus. Klasy powinny przechowywać informacje o właścicielu oraz kolorze.
#  Informacje te powinny być przekazane w momencie tworzenia obiektu klasy.
#  Dodatkowo domyślny kolor klasy Bus powinien być ustawiony jako yellow.
# Klasy powinny mieć metodę display, która wypisuje: typ, właściciela i kolor pojazdu.
# Wykorzystując klasy pojazdów, utworzyć klasę VehicleFactory, przyjmującą listę z konfiguracjami pojazdów do wyprodukowania.
# Pojedyncza konfiguracja powinna zawierać: typ pojazdu, nazwę i kolor. W klasie utworzyć trzy metody:
# * display - do wypisania w konsoli danych o wyprodukowanych pojazdach,
# * save_to_file - przyjmująca nazwę pliku do którego mają zostać zapisane dane pojazdów w formacie JSON,
# * load_configuration_from_file - odczytywania konfiguracji pojazdów do utworzenia z pliku w formacje JSON.
# Należy pamiętać o tym, że konfiguracje pojazdów można podać na etapie tworzenia klasy, lub po jej utworzeniu wczytując je z pliku.
# Do wykonania zadania należy użyć standardowych bibliotek pythona.

from vehicle_factory import VehicleFactory
from bus import Bus
from truck import Truck

config_list = [
    {
        "type": "Truck",
        "owner": "owner",
        "color": "color"
    },
    {
        "type": "Truck",
        "owner": "owner",
        "color": "color"
    },
    {
        "type": "Truck",
        "owner": "owner",
        "color": "color"
    },
    {
        "type": "Truck",
        "owner": "owner",
        "color": "color"
    },
    {
        "type": "Truck",
        "owner": "owner",
        "color": "color"
    }
]


if __name__ == "__main__":
    factory_from_list = VehicleFactory(config_list)
    print(factory_from_list.configuration)

    factory = VehicleFactory()
    print(factory.load_configuration_from_file('test'))
    print(factory.configuration)

    print(factory.run_factory())
    print(factory.display())
