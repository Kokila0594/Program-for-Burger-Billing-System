class BurgerBillingSystem:
    def __init__(self):
        self.menu = {
            1: {"name": "Aloo Tikki", "price": 5},
            2: {"name": "Maharaja", "price": 10},
            3: {"name": "Mac Special", "price": 15},
            # Add more menu items here
        }

    def display_menu(self):
        print("****** Menu ******")
        for sr, item in self.menu.items():
            print(f"{sr}. {item['name']}: ${item['price']}")
        print("******************")

    def get_order(self):
        order = {}
        while True:
            self.display_menu()
            choice = int(input("Enter the serial number of your choice (0 to finish): "))
            if choice == 0:
                break
            quantity = int(input("Enter quantity: "))
            order[choice] = quantity
        return order

    def calculate_bill(self, order):
        total = 0
        bill = []
        for choice, quantity in order.items():
            item = self.menu[choice]
            price = item["price"] * quantity
            total += price
            bill.append({"name": item["name"], "price": item["price"], "quantity": quantity, "total": price})
        return bill, total

    def apply_discount(self, total):
        is_student = input("Are you a student? (yes/no): ")
        if is_student.lower() == "yes":
            discount = total * 0.2
            return total - discount
        return total

    def add_delivery_charge(self, total):
        delivery = input("Do you want delivery? (yes/no): ")
        if delivery.lower() == "yes":
            return total + (total * 0.05)
        return total

    def add_tip(self, total):
        tip = input("Do you want to give a tip? (yes/no): ")
        if tip.lower() == "yes":
            tip_amount = int(input("Enter tip amount (2, 5, 10): "))
            return total + tip_amount
        return total

    def print_bill(self, bill, total):
        print("****************** Final Bill ***********************")
        for i, item in enumerate(bill, start=1):
            print(f"{i}. {item['name']} ${item['price']} x {item['quantity']} = ${item['total']}")
        print("---------------------------------------------------")
        student_discount = 0
        if input("Are you a student? (yes/no): ").lower() == "yes":
            student_discount = total * 0.2
            print(f"Student discount 20%: -${student_discount:.2f}")
        delivery_charge = 0
        if input("Do you want delivery? (yes/no): ").lower() == "yes":
            delivery_charge = total * 0.05
            print(f"Delivery charge 5%: +${delivery_charge:.2f}")
        tip = 0
        if input("Do you want to give a tip? (yes/no): ").lower() == "yes":
            tip_amount = int(input("Enter tip amount (2, 5, 10): "))
            tip = tip_amount
            print(f"Tip: +${tip}")
        print(f"Total bill: ${total - student_discount + delivery_charge + tip:.2f}")
        print("***************************************************")
        print("Thank you and come again!")

    def run(self):
        order = self.get_order()
        bill, total = self.calculate_bill(order)
        total = self.apply_discount(total)
        total = self.add_delivery_charge(total)
        total = self.add_tip(total)
        self.print_bill(bill, total)

if __name__ == "__main__":
    billing_system = BurgerBillingSystem()
    billing_system.run()