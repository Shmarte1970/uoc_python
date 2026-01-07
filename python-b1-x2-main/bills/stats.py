# Write your imports here
from collections import defaultdict
from .item import Product
from .entity import Buyer, Seller
from .item import Bill


class OrderType:
    # Do not change this enum
    ASC = 0
    DES = 1


class Statistics:
    def __init__(self, bills: list[Bill]):
        # Do not change this method
        self.bills = bills

    def find_top_sell_product(self) -> (Product, int):
        counter = defaultdict(int)

        for bill in self.bills:
            for product in bill.products:
                counter[product] += 1

        top_product = max(counter, key=counter.get)
        return top_product, counter[top_product]

    def find_top_two_sellers(self) -> list:
        totals = defaultdict(float)

        for bill in self.bills:
            totals[bill.seller] += bill.calculate_total()

        ordered = sorted(
            totals.items(), key=lambda x: x[1], reverse=True
        )

        return [seller for seller, _ in ordered[:2]]

    def find_buyer_lowest_total_purchases(self) -> (Buyer, float):
        totals = defaultdict(float)

        for bill in self.bills:
            totals[bill.buyer] += bill.calculate_total()

        buyer, total = min(totals.items(), key=lambda x: x[1])
        return buyer, total

    def order_products_by_tax(self, order_type: OrderType) -> tuple:
        product_taxes = {}

        for bill in self.bills:
            for product in bill.products:
                pid = product.product_id

                if pid not in product_taxes:
                    product_taxes[pid] = [product, 0.0]

                product_taxes[pid][1] += product.calculate_total_taxes()

        result = [(data[0], data[1]) for data in product_taxes.values()]

        if order_type == OrderType.DES:
            # impuestos DESC, product_id ASC
            result.sort(key=lambda x: (-x[1], x[0].product_id))
        else:
            # impuestos ASC, product_id ASC
            result.sort(key=lambda x: (x[1], x[0].product_id))

        return result

    def show(self):
        # Do not change this method
        print("Bills")
        for bill in self.bills:
            bill.print()
