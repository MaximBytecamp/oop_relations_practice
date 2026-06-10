class OrderItem:
    def __init__(self, title: str, price: float, quantity: int):
        self.title = title 
        self.price = price 
        self.quantity = quantity

    def get_cost(self) -> float:
        return self.price * self.quantity


class Order:
    def __init__(self, number: str):
        self.number = number
        self.items = []

    def add_item(self, title: str, price: float, quantity: int):
        orderitem = OrderItem(title, price, quantity)
        self.items.append(orderitem) #[OrderItem(blabla, 500, 3), OrderItem(okokm, 1000, 34)]

    def get_total(self) -> float:
        total = 0

        for orderitem in self.items:
            total += orderitem.get_cost()

        return total 

    def print_receipt(self):
        print(f"{self.number} - Номер заказа")

        for orderitem in self.items:
            print(f"{orderitem.title} - {orderitem.get_cost()}")



order = Order("A-1001")
order.add_item("Клавиатура", 2500, 1)
order.add_item("Мышь", 1200, 2)
order.add_item("Коврик", 700, 1)
order.print_receipt()

total = order.get_total()
print(total)