from CustomErrors import SalePostCreationError, WrongPassword, ProductSoldError, InvalidDiscountError
from Post import Post

# Factory Design Pattern
TOTAL_PERCENTAGE = 100  # Represent the total percentage of discount calculations


# Sale post implements post, represent post of sale with product description, price and location
# can discount and update the state of the product (for sale or sold)
class PostSale(Post):
    __product = None  # product description
    __price = None  # product price
    __location = None  # product location
    __for_sale_ = None  # status of the product

    # Constructor for sale post, changing the _post_data and adding for sale, for product status
    def __init__(self, author, product, price, location):
        super().__init__(author=author)  # Initial data to none and overwrite it manually
        self.__product = str(product)
        self.__price = price
        self.__location = str(location)
        self.__for_sale = "For sale!"  # Adding product status
        print(self)  # Printing post after creation

    # Special method being overridden, to print the data as required.
    def __str__(self):
        return (f'{self._author.username} posted a product for sale:\n{self.__for_sale} {self.__product},'
                f' price: {self.__price}, pickup from: {self.__location}\n')

    # Decrease the price of the product for sale
    def discount(self, discount_rate, password):
        try:
            if self._author.password_validation(password) is not True:  # 1. Exceptions: Password Validation
                raise WrongPassword
            elif self.__for_sale == "Sold!":  # 2. Exceptions: Product Availability, Validation
                raise ProductSoldError
            elif not (
                    0 < discount_rate <= TOTAL_PERCENTAGE):  # 3. Exceptions: Logic Discount (max discount 100), Validation
                raise InvalidDiscountError
            price = self.__price  # Current Product Price
            discount = price * (discount_rate / TOTAL_PERCENTAGE)  # Discount Price(number)
            discounted_price = price - discount  # Product Price after Discount
            self.__price = discounted_price  # Changing the product price
            print(f"Discount on {self._author.username} product! the new price is: {discounted_price:.1f}")
        except (WrongPassword, ProductSoldError, Exception) as e:
            print(e)

    # Changing the status of the product to sold
    def sold(self, password):
        try:
            if self._author.password_validation(password) is not True:
                raise WrongPassword
            self.__for_sale = "Sold!"
            print(f"{self._author.username}'s product is sold")
        except (WrongPassword, Exception) as e:
            print(e)
