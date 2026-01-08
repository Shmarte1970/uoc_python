from users.user import Cashier, Customer
from products.product import Product

class Order:
  def __init__(self, cashier:Cashier, customer:Customer):
    self.cashier = cashier
    self.customer = customer
    self.products = []

  def add(self, product : Product):
    self.products.append(product)

  def remove(self, product_id: str) -> Product:
    """Elimina un producto del pedido por su ID. Retorna el producto eliminado o None"""
    for i, product in enumerate(self.products):
      if product.id.lower() == product_id.lower():
        return self.products.pop(i)
    return None

  def calculateTotal(self) -> float:
    total = 0.0
    for product in self.products:
      total += product.price
    return total
  
  def show(self):
    print("Hola : "+self.customer.describe())
    print("Fue atendido por : "+self.cashier.describe())
    for product in self.products:
      print(product.describe())
    print(f"Precio total : {self.calculateTotal():.2f} EUR")
