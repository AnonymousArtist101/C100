class Laptop():
    def __init__(self, brand, version, keyboard, mouse, price, color):
        self.brand=brand,
        self.version=version,
        self.keyboard=keyboard,
        self.mouse=mouse,
        self.price=price,
        self.color=color
    def laptopPrice(self):
        print("50 percent off!")
windows=Laptop("windows", 10, "black", "none", 100, "grey")
print(windows.laptopPrice())
print(windows.price)
print(windows.version)