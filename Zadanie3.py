class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):

    def __init__(self, area, rooms, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'Powierzchnia domu:  {self.area}m²,' \
               f' ilość pokoi: {self.rooms},' \
               f' cena: {self.price}zł, adres: {self.address},' \
               f' powierzchnia działki: {self.plot}m² '


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Powierzchnia domu:  {self.area}m²,' \
               f' ilość pokoi: {self.rooms}, cena: {self.price}zł,' \
               f' adres: {self.address}, ilość pięter: {self.floor} '
