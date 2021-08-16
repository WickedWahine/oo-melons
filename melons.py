class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, country_code='USA'):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code


    def get_total(self):
        """Calculate price, including tax."""
        if self.species == "Christmas melon":
            base_price = 5 * 1.5
        else:
            base_price = 5
            
        total = (1 + self.tax) * self.qty * base_price

        if self.country_code != 'USA' and self.qty < 10:
            total += 3

        return '{:.2f}'.format(total)

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    tax = 0.08
    order_type = "domestic"



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17
    



class GovernmentMelonOrder(AbstractMelonOrder):
    """A US Government order."""
    
    tax = 0
    passed_inspection = False

    def mark_inspection(passed):

        if passed:
            passed_inspection = True



    # def get_country_code(self):
    #     """Return the country code."""

    #     return self.country_code
