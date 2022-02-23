from colorama import *
from enum import Enum, unique


@unique
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class DijkstraFlag(list):
    def __init__(self) -> None:
        pass

    def add_color(self, color) -> None:
        if (isinstance(color, Color)):
            self.append(color)
        else:
            print("PARAMETRO NO VÁLIDO: Debes usar un color de la clase Color")

    def get_flag_str(self, red_position=None, green_position=None, blue_position=None) -> str:
        flag_str = ""
        for c in self:
            if c == Color.RED:
                flag_str += Back.RED + " "
            elif c == Color.BLUE:
                flag_str += Back.BLUE + " "
            elif c == Color.GREEN:
                flag_str += Back.GREEN + " "
            else:
                flag_str += Back.BLACK + "*"

        flag_str += Back.BLACK + Fore.WHITE
        return flag_str

    def __swap_item(self, idx_one, idx_two) -> None:
        if (idx_one != idx_two) and (idx_one >= 0) and (idx_two >= 0) and (idx_one < len(self)) and (idx_two < len(self)):
            new_one_item = self[idx_two]
            self[idx_two] = self[idx_one]
            self[idx_one] = new_one_item

    def sort(self, debug=False) -> None:
        red_position = -1
        green_position = -1
        actual_position = 0
        blue_position = len(self)
        step = 0
        while actual_position < blue_position:
            actual_item = self[actual_position]

            if actual_item == Color.RED:
                # Poner item actual a continuación del último rojo
                red_position += 1
                self.__swap_item(red_position, actual_position)
                green_position += 1

            elif actual_item == Color.GREEN:
                # Si es verde ya està en su sitio => avanzo una posicion
                green_position += 1

            elif actual_item == Color.BLUE:
                # Poner el item actual antes del primer azul
                blue_position -= 1
                self.__swap_item(blue_position, actual_position)
            else:
                # Ni idea de dónde poner estos
                print("ATENCION: Color no esperado!!!!")
                break

            # El item a ordenar es el siguiente al último verde
            actual_position = green_position + 1
            
            if debug:
                print("  Step  >                  "  + self.get_flag_str())
