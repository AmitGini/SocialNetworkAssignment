from CustomErrors import SalePostCreationError, WrongPassword, ProductSoldError, InvalidDiscountError
from Posts import Posts

# todo: DESCRIPTION
PRODUCT_INDEX = 0
PRICE_INDEX = 1
LOCATION_INDEX = 2
TOTAL_PERCENTAGE = 100


# todo: DESCRIPTION

class SalePost(Posts):
    __for_sale_ = None

    # Constructor for sale post, changing the _post_data and adding for sale, for product status
    def __init__(self, user, *args):
        try:
            if len(args[PRODUCT_INDEX]) < 1 or args[PRICE_INDEX] < 1 or len(args[LOCATION_INDEX]) < 1:
                raise SalePostCreationError
            super().__init__(user, None)
            self._post_data: list = [args[PRODUCT_INDEX], args[PRICE_INDEX], args[LOCATION_INDEX]]
            self.__for_sale = True
            print(self)
        except (SalePostCreationError, Exception) as e:
            print(e)

    # Special method being overridden, to print the data as required.
    def __str__(self):
        sale_status = "For sale!"
        if not self.__for_sale:
            sale_status = "Sold!"
        return (f'{self._user.username} posted a product for sale:\n{sale_status} {self._post_data[PRODUCT_INDEX]},'
                f' price: {self._post_data[PRICE_INDEX]}, pickup from: {self._post_data[LOCATION_INDEX]}\n')

    # Decrease the price of the product for sale
    def discount(self, discount_rate, password):
        try:
            if self._user.password_validation(password) is not True:  # 1. Exceptions: Password Validation
                raise WrongPassword
            elif self.__for_sale is not True:  # 2. Exceptions: Product Availability, Validation
                raise ProductSoldError
            elif not (0 < discount_rate <= 100):  # 3. Exceptions: Logic Discount, Validation
                raise InvalidDiscountError
            price = self._post_data[PRICE_INDEX]  # Current Product Price
            discount = price * (discount_rate / TOTAL_PERCENTAGE)  # Discount Price(number)
            discounted_price = price - discount  # Product Price after Discount
            self._post_data[
                PRICE_INDEX] = discounted_price  # Changing the product price                print(f"Discount on {self._user.username} product! the new price is: {discounted_price:.1f}")
        except (WrongPassword, ProductSoldError, Exception) as e:
            print(e)

    # Changing the status of the product to sold
    def sold(self, password):
        try:
            if self._user.password_validation(password) is not True:
                raise WrongPassword
            self.__for_sale = False
            print(f"{self._user.username}'s product is sold")
        except (WrongPassword, Exception) as e:
            print(e)
