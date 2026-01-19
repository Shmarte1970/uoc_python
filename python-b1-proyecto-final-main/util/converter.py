from abc import ABC, abstractmethod
from users.user import Cashier, Customer
from products.product import Hamburger, Soda, Drink, HappyMeal

class Converter(ABC):
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass  
  def print(self, objects):
    for item in objects:
      print(item.describe())

class CashierConverter(Converter):
  def convert(self, dataFrame):
    cashiers = []
    for index, row in dataFrame.iterrows():
      cashier = Cashier(str(row['dni']), row['name'], int(row['age']), row['timetable'], float(row['salary']))
      cashiers.append(cashier)
    return cashiers

class CustomerConverter(Converter):
  def convert(self, dataFrame):
    customers = []
    for index, row in dataFrame.iterrows():
      customer = Customer(str(row['dni']), row['name'], int(row['age']), row['email'], str(row['postalcode']))
      customers.append(customer)
    return customers

class ProductConverter(Converter):
  def convert(self, dataFrame, product_type):
    products = []
    for index, row in dataFrame.iterrows():
      if product_type == 'hamburger':
        product = Hamburger(row['id'], row['name'], float(row['price']))
      elif product_type == 'soda':
        product = Soda(row['id'], row['name'], float(row['price']))
      elif product_type == 'drink':
        product = Drink(row['id'], row['name'], float(row['price']))
      elif product_type == 'happymeal':
        product = HappyMeal(row['id'], row['name'], float(row['price']))
      products.append(product)
    return products