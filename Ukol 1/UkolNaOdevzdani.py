class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} Kč."


class Pizza(Item):
    def __init__(self, name: str, price: float, ingredients: dict):
        super().__init__(name, price)
        self.ingredients = ingredients

    def add_extra(self, ingredient: str, quantity: int, price_per_ingredient: int):
        self.price += price_per_ingredient
        return f"Extra {ingredient}: {quantity} grams."

    def __str__(self):
        return f"Pizza {self.name}, celková cena je {self.price}"


class Drink(Item):
    def __init__(self, name: str, price: float, volume: int):
        super().__init__(name, price)
        self.volume = volume

    def __str__(self):
        return f"{self.name} v objemu {self.volume} ml stojí {self.price} Kč."


class Order:
    def __init__(self, name: str, address: str, items: list, status: str = "Nová"):
        self.name = name
        self.address = address
        self.items = items
        self.status = status

    def mark_delivered(self):
        self.status = "Doručeno."

    def __str__(self):

        itemsText = ""

        for item in self.items:
            itemsText += item.name + ", "

        return f"Jméno zákazníka: {self.name} \nAdresa: {self.address} \nPoložky v objednávce: {itemsText} \nStav objednávky: {self.status}"


class DeliveryPerson:
    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number

        self.available = True
        self.current_order = None

    def assign_order(self, order: Order):
        if not self.available:
            return False

        else:
            self.order = order
            order.status = "Na cestě"
            self.available = False
            return True

    def complete_delivery(self):
        self.order.status = "Doručeno."
        self.available = True

    def __str__(self):
        if self.available:
            return f"{self.name} je dostupný pro další objednávku."
        else:
            return f"{self.name} momentálně doručuje objednávku."


# Vytvoření instance pizzy a manipulace s ní
margarita = Pizza("Margarita", 200, {"sýr": 100, "rajčata": 150})
margarita.add_extra("olivy", 50, 10)

# Vytvoření instance nápoje
cola = Drink("Cola", 1.5, 500)

# Vytvoření a výpis objednávky
order = Order("Jan Novák", "Pražská 123", [margarita, cola])
print(order)

# Vytvoření řidiče a přiřazení objednávky
delivery_person = DeliveryPerson("Petr Novotný", "777 888 999")

if delivery_person.assign_order(order):
    print("Objednávka byla přiřazena.")
else:
    print("Doručovatel není dostupný.")

print(delivery_person)

# Dodání objednávky
delivery_person.complete_delivery()
print(delivery_person)

# Kontrola stavu objednávky po doručení
print(order)
