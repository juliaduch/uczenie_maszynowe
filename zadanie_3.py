# 3. Stworzyć następujące klasy:
# Property (klasa opisująca posiadłość/nieruchomość), posiadająca pola: area, rooms (int),price,address
# House (klasa dziedzicząca klasę Property , która opisuje dom), posiadająca pola: plot (rozmiar działki, int)
# Flat (klasa dziedzicząca klasę Property , która opisuje mieszkanie), posiadająca pola: floor
# Dodatkowo:
# Każda z klas dziedziczących ma mieć zaimplementowaną metodę __str__ , która będzie opisywała obiekt.
# Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas tworzenia instancji klasy za pośrednictwem
# konstruktora.
# Stworzyć po jednym obiekcie klasy House oraz Flat, a następnie je wyświetlić.

class Property:
    def __init__(self,area,rooms:int,price,address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

class House(Property):
    def __init__(self,area,rooms:int,price,address,plot,rozmair_dzialki:int):
        super().__init__(area,rooms,price,address)
        self.plot = plot
        self.rozmiar_dzialki = rozmair_dzialki

    def __str__(self):
        return f'House with area of {self.area} and {self.rooms} rooms, costs {self.price}, in {self.address}, plot {self.plot}, area {self.rozmiar_dzialki}'


class Flat(Property):
    def __init__(self,area, rooms: int, price, address,floor):
        super().__init__(area,rooms,price,address)
        self.floor = floor

    def __str__(self):
        return f'Flat with area of {self.area} and {self.rooms} rooms, costs {self.price}, in {self.address}, on {self.floor} floor'

house = House(1234,5,60000,'warszawa','stalowy',15)
flat = Flat(60,2,20000,'bytom',5)

print(house)
print(flat)