class Store:

    def __init__(self, id1, name, address, max_obj):
        self.id = id1
        self.name = name
        self.address = address
        self.max_obj = max_obj
        self.equip = []

    def send_to(self, *eq):
        for el in eq:
            self.equip.append(el)
        print(self.equip)


class OfficeEquip(Store):
    def __init__(self, id1, model, name):
        self.id = id1
        # self.type = type
        self.model = model
        self.name = name


class Printer(OfficeEquip):
    def __init__(self, id1, model, name):
        super().__init__(id1, model, name)
        self.type = "Printer"


class Scanner(OfficeEquip):
    def __init__(self, id1, model, name):
        super().__init__(id1, model, name)
        self.type = "Scanner"


class Copier(OfficeEquip):
    def __init__(self, id1, model, name):
        super().__init__(id1, model, name)
        self.type = "Scanner"


store_01 = Store(1, "Store №1", "Moscow, Soviet 1", 5)
printer_01 = Printer("p1", "HP ", "LaserJet 1")
printer_02 = Printer("p2", "HP ", "LaserJet 2")

store_01.send_to(printer_01.id, printer_02.name)
