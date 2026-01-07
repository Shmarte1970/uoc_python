from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, dni: str, email: str, mobile: str, address: str):
        self.dni = dni
        self.email = email
        self.mobile = mobile
        self.address = address

    @abstractmethod
    def print(self):
        pass

    def __eq__(self, another):
       # Do not change this method
       return hasattr(another, 'dni') and self.dni == another.dni
    
    def __hash__(self):
       # Do not change this method
       return hash(self.dni)

class Buyer(Person):
    def __init__(self, dni: str, full_name: str, age: int,
                 email: str, mobile: str, address: str):
        super().__init__(dni, email, mobile, address)
        self.full_name = full_name
        self.age = age

    def print(self):
        return self.full_name

class Seller(Person):
    def __init__(self, dni: str, email: str, mobile: str,
                 bussines_name: str, bussines_address: str):
        super().__init__(dni, email, mobile, bussines_address)
        self.bussines_name = bussines_name
        self.bussines_address = bussines_address

    def print(self):
        return self.bussines_name
