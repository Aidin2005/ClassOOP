1. The Class Itself:

The Car class is a blueprint for creating car objects. It has attributes like make, model, year, and price to store details about the car. When you create a new car, you pass these details into the class, and they get saved in the object.

2. The __init__ Method:

This is the constructor, which gets called when we create a new car. It sets up the car’s details based on what we give it. If no details are given, it sets them to None by default, but ideally, you’d always provide them.
    def __init__(self, make=None, model=None, year=None, price=None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
So when you create a car, you give it a make, model, year, and price, and it stores those values.

3. The display_info Method:

This method is for showing the car’s information. It prints out the details like the make, model, year, and price in a nice, easy-to-read format.
   def display_info(self):
       print(f"Car Info: {self.year} {self.make} {self.model}, Price: ${self.price}")

4. The apply_discount Method:

This method lets you apply a discount to the car’s price. You give it a discount percentage, and it will reduce the car’s price accordingly. If the price isn’t set (i.e., it’s None), it will tell you that the price is not set.

def apply_discount(self, discount):
    if self.price:
        self.price -= self.price * (discount / 100)
        print(f"New price after {discount}% discount: ${self.price}")
    else:
        print("Price is not set.")
This allows for dynamic price changes after the car is created. You can adjust the price anytime you want.

How It Meets the Requirements:
	•	Stores Car Info: The class takes care of storing all the essential details like make, model, year, and price.
	•	Shows Car Info: The display_info method helps to print out the details of each car, so you can easily review them.
	•	Applies Discounts: The apply_discount method lets you apply discounts to the car’s price, and it updates the price accordingly.
