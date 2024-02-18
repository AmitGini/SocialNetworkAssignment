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
        return (f'{self.publisher_username} posted a product for sale:\nFor sale! {self.__product},'
                f' price: {self.__price}, pickup from: {self.__location}\n')

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
            print(f"Discount on {self.publisher_username} product! the new price is: {self.__price:.1f}")

    # todo: DESCRIPTION
    def sold(self, password):
        if self._user.check_password(password) is not True:
            print("Invalid password")
        else:
            self.__for_sale = False
            print(f"{self.publisher_username}'s product is sold")
