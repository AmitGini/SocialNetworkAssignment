from Posts import Posts

# todo: DESCRIPTION
ARGS_INDEX_PRODUCT = 0
ARGS_INDEX_PRICE = 1
ARGS_INDEX_LOCATION = 2
TOTAL_PERCENTAGE = 100


# todo: DESCRIPTION

class SalePost(Posts):

    # todo: DESCRIPTION
    def __init__(self, user, tuple_args):
        super().__init__(user, tuple_args)
        self.__product = tuple_args[ARGS_INDEX_PRODUCT]
        self.__price = tuple_args[ARGS_INDEX_PRICE]
        self.__location = tuple_args[ARGS_INDEX_LOCATION]
        self.__for_sale = True

    # Special method being overridden, to print the data as required.
    def __str__(self):
        return "{username} posted a product for sale:\n" \
               "For sale! {product}, price: {price:.1f}, pickup from: {location}\n".format(
            username=self.publisher_username, product=self.__product, price=self.__price, location=self.__location)

    # todo: DESCRIPTION
    def discount(self, discount_rate, password):

        if self._user.check_password(password) is not True:
            print("Invalid password")

        elif self.__for_sale is not True:
            print("Product already been Sold!")

        elif not (0 < discount_rate <= 100):
            print("Invalid discount rate, Must be between 1-100")

        else:
            discount = self.__price * (discount_rate / TOTAL_PERCENTAGE)
            self.__price -= discount
            print("Discount on {username} product! the new price is: {price:.1f}".format(
                username=self.publisher_username, price=self.__price))

    # todo: DESCRIPTION
    def sold(self, password):
        if self._user.check_password(password) is not True:
            print("Invalid password")
        else:
            self.__for_sale = False
            print("{username} product is sold\n".format(username=self.publisher_username))
