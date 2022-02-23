from colorama import *
from enum import Enum, unique


@unique
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class DijkstraFlag(list):
    color_str = {Color.RED: Back.RED,
                 Color.BLUE: Back.BLUE, Color.GREEN: Back.GREEN}

    def __swap_item(self, idx_one, idx_two) -> None:
        if (idx_one != idx_two) and (idx_one >= 0) and (idx_two >= 0) and (idx_one < len(self)) and (idx_two < len(self)):
            new_one_item = self[idx_two]
            self[idx_two] = self[idx_one]
            self[idx_one] = new_one_item

    def add_color(self, color) -> None:
        if (isinstance(color, Color)):
            self.append(color)
        else:
            print("PARAMETRO NO VÁLIDO: Debes usar un color de la clase Color")

    def get_flag_str(self, red_position=None, green_position=None, blue_position=None) -> str:
        flag_str = Fore.BLACK
        for idx, val in enumerate(self):
            c = self[idx]
            pointer_char = "·"
            if idx == red_position:
                pointer_char = "R"
            elif idx == blue_position:
                pointer_char = "B"
            elif idx == green_position:
                pointer_char = "G"

            flag_str += self.color_str[c] + pointer_char

        flag_str += Back.BLACK + Fore.WHITE
        return flag_str

    def sort_iterative(self, debug=False) -> None:
        red_position = green_position = -1
        actual_position = 0
        blue_position = len(self)
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
                print("  Step  >                  " +
                      self.get_flag_str(red_position, green_position, blue_position))

    def sort_recursive(self, debug=False, red_position=None, green_position=None, blue_position=None, actual_position=None) -> None:
        if (red_position == None) or (green_position == None) or (blue_position == None) or (actual_position == None):
            # Inicialización para la primera invocación
            red_position = green_position = -1
            actual_position = 0
            blue_position = len(self)

        if actual_position >= blue_position:
            # Condición de fin de recursividad
            return

        actual_item = self[actual_position]

        if actual_item == Color.RED:
            # Poner item actual a continuación del último rojo
            red_position += 1
            self.__swap_item(red_position, actual_position)
            green_position += 1

        elif actual_item == Color.GREEN:
            # Si es verde ya està en su sitio => avanzo una posicion
            green_position += 1

        else:
            # Poner el item actual antes del primer azul
            blue_position -= 1
            self.__swap_item(blue_position, actual_position)
 
        # El item a ordenar es el siguiente al último verde
        actual_position = green_position + 1

        if debug:
            print("  Step  >                  " +
                  self.get_flag_str(red_position, green_position, blue_position))

        self.sort_recursive(debug, red_position,
                            green_position, blue_position, actual_position)
