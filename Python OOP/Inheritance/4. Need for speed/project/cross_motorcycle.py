from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):
    def __init__(self, fuel, horse_power: int):
        super().__init__(fuel, horse_power)
