# In this course. David Aroesti teach us about assertions and exceptions, private a protected attributes.
# I combine this knowledge with POO concept to build a class for the supermarkets

import datetime

class Supermarket:
    """
        Class Supermarket: it a have a bunch of methods and attribute of any supermarket

        >>> mercado = Supermarket(products=dict(), employees=list(), clients=list())
    """

    def __init__(self, products, employees, clients):
        self.products = products
        self.employees = employees
        self.clients = clients
        self.open = False  # attribute to set is the supermarket is open or closed
        self._funds = 300  # protected attribute
        self.__owner = "Jose Colmenares"  # private atribute

    def update_products(self, products_prices):
        # I want to try exceptions
        try:
            return self.products.update(
                products_prices
            )  # update values on a dictionary
        except ValueError as problem:  # you have to introduce a key with the right value
            print("Invalid input")
            print(problem)
            return self.products

    def update_workers(self, list_employees):
        # I want to try assertions
        assert type(list_employees) == list, "It have to be a list"
        self.employees = list_employees  # update list
        return self.employees

    def sell_products(self, item, quantity, client):
        # We substract the number of item in the dictionary
        self.products[item] -= quantity
        # We add the current client to our list
        self.clients.append(client)
        print("{} {} sold to {}".format(quantity, item, client))

    def toogle_open(self):
        self.open = not self.open  # open/closed
        # print a string with the current local datetime with tzinfo = None
        print(
            "The supermarket has {0} at {1}".format(
                "opened" if self.open == True else "closed", datetime.datetime.today()
            )
        )

    # decorators: accesing to private value
    @property
    def owner(self):  # we access to private value using getters
        return self.__owner  # we can return the value

    @owner.setter  # we can modify the value with a setter
    def owner(self, new_owner):  # introduce new value
        print("Selling supermarket to...")
        self.__owner = new_owner
        print("The new owner is ", self.__owner)

    @owner.deleter  # deleter
    def owner(self):
        print("Deleting owner..")
        del self.__owner


class Grocery(Supermarket):
    # first we have to initialize the new-subclass with its new arguments
    def __init__(self, productos, empleados, clientes):
        # we inherit all the attributes and methods of the super class
        super().__init__(productos, empleados, clientes)
        self._funds = 100  # less cash than a supermarket

    # Here we use the concept polymorphism
    # This is not a supermarket, is a local grocery store.
    # We have to change the output
    def toogle_open(self):
        self.open = not self.open  # atribute inherited from Supermarket
        # print a string with the new name
        print("The grocery has {}".format("opened" if self.open == True else "closed"))


if __name__ == "__main__":

    # I'm going to create a new instance of a supermarket called 'mercadonut'
    mercadonut = Supermarket(products=dict(), employees=list(), clients=[])
    mercadonut.toogle_open()
    # list of employees
    workers = ["Ana Maria Guerrero", "Vicente Almeida", "Juan Alberto Donoso"]
    # upload employees list ( with no charges, everybody do the same job)
    print(mercadonut.update_workers(workers))

    # list of initial products with price
    products1 = {"milk": 20, "chocolate": 30, "wheat": 60, "eggs": 40}
    # function for upload productos
    mercadonut.update_products(products1)
    print("current inventory: \n", mercadonut.products)

    products2 = {"yogurt": 100}
    # we try that update(dict) functions works
    mercadonut.update_products(products2)
    print("current inventory: \n", mercadonut.products)

    # I want to sell a product to somebody
    mercadonut.sell_products("chocolate", 3, "Robert")
    print("Today's clients: ", mercadonut.clients)
    print("current inventory: \n", mercadonut.products)

    print("*" * 30)  # separator

    # this is a very useful fucntion when you're working with POO
    print(
        "mercadonut is instance of Supermarket? ", isinstance(mercadonut, Supermarket)
    )
    # help(Supermarket) # with this line I could see the documentation that I have created

    print("*" * 30)  # separator
    print(
        "Current funds in out account: ", mercadonut._funds
    )  # this is a protected attribute, you can print it but now modifying it

    mercadonut.owner
    mercadonut.owner = "Vicente Herrera"  # this is a private attribute, it have to be modified with setter and getters
    del mercadonut.owner
    mercadonut.toogle_open()
    print("*" * 30)  # separator

    # We create a small market called grocery, similar to a 'Bodega'
    fruteriadonramon = Grocery(productos=dict(), empleados=list(), clientes=[])
    print(
        "fruteriadonramon is instance of Supermarket? ",
        isinstance(fruteriadonramon, Supermarket),
    )
    print(
        "fruteriadonramon is instance of Grocery? ",
        isinstance(fruteriadonramon, Grocery),
    )

    # help(fruteriadonramon) # with this command you could see which methods are inherit from the Super class
    print(fruteriadonramon.owner)
    fruteriadonramon.toogle_open()
