"""Classes for melon orders."""

class AbstractMelonOrder():
    shipped = False


    def __init__(self, species, qty):

        self.species = species
        self.qty = qty
        #self.order_type = order_type



    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        if self.species == "Christmas melon":
            base_price = base_price * 1.5
            return total

        if self.order_type == 'international' and self.qty < 10:
            return total + 3
        #else:
        #    return total





    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

   
    order_type = "domestic"
    tax = 0.08

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    
    order_type = "international"
    tax = 0.17

    # def __init__(self, qty):
    #     super().__init__(qty)
    #     if order_type == 'international' and self.qty < 10:
    #         total = get_total()
    #         return total = total + 3






    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.country_code = country_code


    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code




