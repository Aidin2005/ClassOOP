class Car:
    def __init__(self, make=None, model=None, year=None, price=None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
       
        if self.price is not None:
            print(f"Car Info: {self.year} {self.make} {self.model}, Price: ${self.price}")
        else:
            print(f"Car Info: {self.year} {self.make} {self.model}, Price: Not available")

    def apply_discount(self, discount):
       
        if not (0 <= discount <= 100):
            print("Discount must be between 0 and 100%.")
            return
        if self.price is None:
            print("Price is not set, unable to apply discount.")
        else:
            original_price = self.price
            self.price -= self.price * (discount / 100)
            print(f"Original price: ${original_price}, New price after {discount}% discount: ${self.price:.2f}")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_car_info():
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = input("Enter car year: ")

    price = None
    while price is None:
        try:
            price = get_float_input("Enter car price: ")
        except ValueError:
            print("Please enter a valid number for the price.")
    return make, model, year, price

def main():
    cars = []
    N = int(input("Enter the number of cars: "))

    for _ in range(N):
        make, model, year, price = get_car_info()
        car = Car(make, model, year, price)
        cars.append(car)

    for car in cars:
        car.display_info()
        discount = get_float_input("Enter discount percentage: ")
        car.apply_discount(discount)

if __name__ == "__main__":
    main()
