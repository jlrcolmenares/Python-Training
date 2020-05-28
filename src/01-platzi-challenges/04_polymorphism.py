# I want to understand the concept of polymorphism

class Supermarket:
    def __init__(self, open):
        self.open = open
    
    def toggle_open(self):
        self.open = not self.open
        print('The supermarket is {}'.format( 'Open' if self.open == True else 'Closed' ) )


class GroceryStore(Supermarket):
    def __init__(self,open):
        super().__init__( open)
    
    def toggle_open(self):
        self.open = not self.open
        print('The grocery store is {}'.format( 'Open' if self.open == True else 'Closed' ) )

class MultiMarket(Supermarket):
    def __init__(self, abierto): # la nueva clase tiene un argumento llamado abierto
        super().__init__(open) # aquí heredo los metodos de la super clase, entre ellos el atributo 'open'
        # para este punto tenemos 2 atributos: open y abierto. con el mismo valor
        self.abierto = open # aqui le asignamos el valor de uno al otro
        # EN ESTE PUNTO DEBEN EXISTIR DOS VALORES self.open y self. abierto

    # se toma el metodo heredado pero se le da una nueva definicion. Que se ve en el strings
    def toggle_open(self):
        self.abierto = not self.abierto
        print('The multimarket store is {}'.format( 'Open' if self.abierto == True else 'Closed' ) )

if __name__ == "__main__":
    supermercado = Supermarket( open = False)
    supermercado.toggle_open()
    supermercado.toggle_open()

    bodega = GroceryStore( open = False)
    bodega.toggle_open()
    bodega.toggle_open()
    # La aplicación de este código funciona sin problemas.

    makro = MultiMarket( abierto = False) # creo que la
    print(makro.abierto)
    print(makro.open)
    makro.toggle_open()
    makro.toggle_open()