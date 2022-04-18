# Создать свой класс данных +
# Добавить в класс статикметод +
# Добавить в класс классметод +
# Создать метакласс


from dataclasses import dataclass


@dataclass
class ElectronicCigarette():
    minimal_power = 8
    name: str
    power: int
    users: int

    @classmethod
    def change_default_value(cls, minimal_power_new):
        cls.minimal_power = minimal_power_new

    @staticmethod
    def compare_power(first_pod, second_pod):
        return first_pod.power > second_pod.power



vap_xros = ElectronicCigarette("Vaporesso XROS", 16, 16513216)
vap_barr = ElectronicCigarette("Vaporesso Barr", 13, 15644424)
elf = ElectronicCigarette("Elf Bar", 12, 19849652)
print(vap_xros)
print(ElectronicCigarette.compare_power(vap_barr, elf))
print(vap_barr.minimal_power)
vap_barr.change_default_value(10)
print(vap_barr.minimal_power)