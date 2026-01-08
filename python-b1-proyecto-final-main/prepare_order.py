"""
Ejercicio 1: Sistema de comida rápida
 
Implementar un paquete llamado ‘products' que tiene dos módulos: ‘food_package.py' y ‘product.py', con la siguiente estructura:

products/
        __init__.py
        food_package.py
        product.py

El módulo food_package.py contendrá una clase abstracta denominada 'FoodPackage' con dos funciones abstractas: 'def pack(self)  -> str ' y 'def material(self) -> str '. Esta clase nos permite crear un tipo específico de paquete o envoltura dependiendo del tipo de alimento a empacar, por ejemplo:

Un vaso de soda puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Una hamburguesa puede ser empacada en un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las siguientes clases ‘Wrapping’, ‘Bottle’, ‘Glass’ y ‘Box’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Wrapping’ se puede definir como:

class Wrapping(FoodPackage):  
  def pack(self):
    return "Food Wrap Paper"
  def material(self):
    return "Aluminium" 

El módulo 'product.py’ contendrá una clase abstracta denominada 'Product' con dos funciones abstractas: 'def type(self) -> str' y 'def foodPackage(self)-> FoodPackage. Esta clase nos permita crear un producto específico y relacionarlo con su tipo de empaque por ejemplo:

Un producto con código de barras G1, es una soda Sprite cuyo precio es de 5 euros, pertenece al tipo Soda y puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Un producto con código de barras H1, es una hamburguesa Bacon  cuyo precio es de 15 euros, pertenece al tipo Hamburger y puede ser empacado en un paquete un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Hamburger’, ‘Soda’, ‘Drink’ y ‘HappyMeal’, es decir, de forma parecida al módulo anterior, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Hamburger’, se puede definir como:

class Hamburger(Product):
    def __init__(self, id:str, name:str, price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburger"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        
Implementar un paquete llamado ‘users' que tiene un módulo ‘user.py', con la siguiente estructura:

users/
        __init__.py
        user.py

El módulo 'user.py' contendrá una clase abstracta denominada ‘User’ que tiene un constructor por defecto para los siguientes datos 'def __init__(self, dni:str, name:str, age:int) ', con una función abstracta: 'def describe(self) '.

Luego en el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Cashier’ y ‘Customer’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Adicionalmente, estas clases se diferencian por los parámetros que reciben sus constructores, por tanto, debemos hacer uso de herencia para inicializar el constructor de la clase padre y agregar características propias a cada clase.  

Implementar un paquete llamado 'util' que tiene dos módulos, denominados 'file_manager.py' y 'converter.py’, con la siguiente estructura:

util/
        __init__.py
        file_manager.py
        converter.py

El módulo ‘file_manager.py' contendrá una clase ‘CSVFileManager’ la cual es una implementaciòn libre y debe incluir las funciones:

La función 'def read(self)' lee un archivo en formato CSV y permite exportar su resultado como un Data Frame.
La función 'def write(self, dataFrame)' convierte un Data Frame en un archivo CSV. Esta es una función opcional, se deja al estudiante la implementación.

Los archivos en formato CSV se encuentran en la ruta “data/”, a continuación, se describe el contenido de cada archivo:

cashiers.csv: Información de los cajeros que harán uso del sistema.
customers.csv: Información de los clientes que harán uso del sistema.
drinks.csv: Información de los diferentes tipos de bebidas.
sodas.csv: Información de los diferentes tipos de gaseosas.
hamburgers.csv: Información de los diferentes tipos de hamburguesas.
happyMeal.csv: Información de los diferentes tipos de happy meals.

El módulo 'converter.py' contendrá una clase denominada ‘Converter’ con una función abstracta para convertir las filas de un Data Frame en instancias de objetos. La función sería ‘def convert(self, dataFrame, *args) -> list’. Adicionalmente esta clase debe incluir un método que permite imprimir la información de los objetos ‘def print(self, list)’. En el mismo módulo se deberán incluir las implementaciones específicas que permitan leer los archivos en formato CSV y convertir sus filas en objetos de cada clase utilizando los paquetes product y users.

Implementar un paquete llamado 'orders' que tiene un módulo 'order.py', con la siguiente estructura:

orders/
        __init__.py
        order.py

El módulo 'order.py' contendrá una clase denominada ‘Order’ con un constructor ‘def __init__(self, cashier:Cashier, customer:Customer):’, el cual permite inicializar la clase con los datos del cajero, del cliente y la lista de productos vacía por defecto. Además, debe incluir tres funciones para agregar productos, calcular el total de la orden solicitada y mostrar la información de la orden que está siendo procesada. Las funciones son ‘def add(self, product: Product)', ' def calculateTotal(self) -> float' y ‘def show(self)’, respectivamente.

Finalmente tendremos una clase principal que se llamará ‘PrepareOrder’ en la cual se deberá realizar una implementación que permita integrar los diferentes módulos empleados para leer los archivos en formato CSV y convertirlos en objetos. La implementación de esta clase es libre, es decir, no indicaremos las funciones que debe contener, pero la funcionalidad de la clase debe permitir crear una opción de menú que permita buscar los clientes, los cajeros y los productos para finalmente crear una orden. 

Se sugiere utilizar los métodos de entrada de teclado para leer los datos del dni cajero, cliente e id de los productos. 


A grandes rasgos, la aplicación seguiría los siguientes pasos:

1)	Leer archivos en formato csv: 
a.	Leer cada archivo en formato csv: Utilizar una instancia de la clase 'CSVFileManager' y llamar al método 'read()'.
2)	Convertir a listas de objetos:
a.	Convertir cajeros: Función creada por el alumno  
b.	Convertir clientes: Función creada por el alumno 
c.	Convertir productos: Función creada por el alumno 
3)	Preparar Orden:
a.	Buscar cajero por dni: Función creada por el alumno y debe devolver una instancia de tipo cajero.
b.	Buscar cliente por dni. Función creada por el alumno y debe devolver una instancia de tipo cliente.
c.	Inicializar Orden: Utilizar una instancia la clase 'Order', e inicializar con su constructor por defecto.
d.	Mostrar productos a vender: Función creada por el alumno.
e.	Escoger productos: Función creada por el alumno.
f.	Agregar productos: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'add()'.
4)	Mostrar Orden: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'show()'


"""
from users.user import Cashier, Customer
from products.product import Product
from orders.order import Order
from util.file_manager import CSVFileManager
from util.converter import CashierConverter, CustomerConverter, ProductConverter


class PrepareOrder:
    def __init__(self):
        self.cashiers = []
        self.customers = []
        self.products = []

    def loadData(self):
        """Carga todos los archivos CSV y los convierte en objetos"""
        # Cargar cajeros
        cashier_df = CSVFileManager("data/cashiers.csv").read()
        self.cashiers = CashierConverter().convert(cashier_df)

        # Cargar clientes
        customer_df = CSVFileManager("data/customers.csv").read()
        self.customers = CustomerConverter().convert(customer_df)

        # Cargar productos
        hamburger_df = CSVFileManager("data/hamburgers.csv").read()
        hamburgers = ProductConverter().convert(hamburger_df, 'hamburger')

        soda_df = CSVFileManager("data/sodas.csv").read()
        sodas = ProductConverter().convert(soda_df, 'soda')

        drink_df = CSVFileManager("data/drinks.csv").read()
        drinks = ProductConverter().convert(drink_df, 'drink')

        happymeal_df = CSVFileManager("data/happyMeal.csv").read()
        happymeals = ProductConverter().convert(happymeal_df, 'happymeal')

        # Combinar todos los productos
        self.products = hamburgers + sodas + drinks + happymeals

        print("Datos cargados exitosamente!\n")

    def findCashierByDni(self, dni: str):
        """Busca un cajero por DNI"""
        for cashier in self.cashiers:
            if str(cashier.dni).lower() == dni.lower():
                return cashier
        return None

    def findCustomerByDni(self, dni: str):
        """Busca un cliente por DNI"""
        for customer in self.customers:
            if str(customer.dni).lower() == dni.lower():
                return customer
        return None

    def findProductById(self, product_id: str):
        """Busca un producto por ID"""
        for product in self.products:
            if product.id.lower() == product_id.lower():
                return product
        return None

    def showProducts(self):
        """Muestra todos los productos disponibles"""
        print("\n========== PRODUCTOS DISPONIBLES ==========")
        for product in self.products:
            print(f"  {product.id} - {product.name} - {product.price} EUR - [{product.type()}]")
        print("===========================================\n")

    def createOrder(self):
        """Flujo principal para crear una orden"""
        print("\n*** SISTEMA DE COMIDA RAPIDA ***\n")

        # Buscar cajero
        while True:
            cashier_dni = input("Ingrese el DNI del cajero: ")
            cashier = self.findCashierByDni(cashier_dni)
            if cashier:
                print(f"Cajero encontrado: {cashier.name}\n")
                break
            else:
                print("Cajero no encontrado. Intente nuevamente.\n")

        # Buscar cliente
        while True:
            customer_dni = input("Ingrese el DNI del cliente: ")
            customer = self.findCustomerByDni(customer_dni)
            if customer:
                print(f"Cliente encontrado: {customer.name}\n")
                break
            else:
                print("Cliente no encontrado. Intente nuevamente.\n")

        # Crear orden
        order = Order(cashier, customer)

        # Agregar productos
        while True:
            self.showProducts()

            # Cambiar el mensaje si ya hay productos en el pedido
            if len(order.products) > 0:
                product_id = input("Ingrese el ID del producto (eliminar producto inserta el ID o 'fin' para terminar): ")
            else:
                product_id = input("Ingrese el ID del producto (o 'fin' para terminar): ")

            if product_id.lower() == 'fin':
                break

            # Verificar si el producto está en el pedido actual (para eliminar)
            removed_product = order.remove(product_id)

            if removed_product:
                # El producto estaba en el pedido, se eliminó
                print(f"\nProducto eliminado: {removed_product.name}")
            else:
                # El producto no estaba en el pedido, intentar agregarlo
                product = self.findProductById(product_id)
                if product:
                    order.add(product)
                    print(f"\nProducto agregado: {product.name}")
                else:
                    print("\nProducto no encontrado. Intente nuevamente.")

            # Mostrar pedido actual si hay productos
            if len(order.products) > 0:
                print("\n--- Su pedido actual: ---")
                for p in order.products:
                    print(f"  [{p.id:>4}] {p.name:<30} {p.price:>8.2f} EUR")
                print(f"\nTotal productos: {len(order.products)}")
                print(f"Total a pagar: {order.calculateTotal():>8.2f} EUR")
                print("-" * 45 + "\n")
            else:
                print("\n(El pedido está vacío)\n")

        # Mostrar orden
        print("\n========== RESUMEN DE LA ORDEN ==========")
        order.show()
        print("=========================================\n")

    def run(self):
        """Ejecuta la aplicacion"""
        self.loadData()
        self.createOrder()


if __name__ == "__main__":
    app = PrepareOrder()
    app.run()

