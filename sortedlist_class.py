class SortedList(list):
    # Creamos una clase que añade la busque dicotómica la clase lista que trae python
    # Para ello usamos la heréncia

    def dichotomic_index(self, key):
        # Devuelve la posición de key en la lista o None si no se encuentra
        return self.__dichotomic_search(key, 0, len(self)-1)

    def __dichotomic_search(self, key, ini_index, end_index):
        central_index = int((ini_index + end_index) / 2)

        if (ini_index > end_index):
            # Si la clave buscada no este en la lista devolveremo None.
            return None

        if(self[central_index] == key):
            # Si clave encontrada devolvemos la posición
            return(central_index)

        if (key < self[central_index]):
            # Si la clave es menor buscamos en la parte izquierda
            # Llamada recursiva
            return self.__dichotomic_search(key, ini_index, central_index-1)

        # Si la clave es mayor (sino habria entrado en los anterior if) buscamos en la parte derecha
        # Llamada recursiva
        return self.__dichotomic_search(key, central_index+1, end_index)

    def append(self, item):
        # Al añadir items ordenamos la lista ya que sino la busqueda dicotomica no funciona.
        super().append(item)
        super().sort()