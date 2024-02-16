from Posts import Posts

ARGS_INDEX_ITEM = 0
ARGS_INDEX_PRICE = 1
ARGS_INDEX_LOCATION = 2
TOTAL_PERCENTAGE = 100


class SalePost(Posts):
    __item = None
    __price = None
    __location = None
    __for_sale = None

    def __init__(self, user, *args):
        super().__init__(user, args)
        self.__item = args[ARGS_INDEX_ITEM]
        self.__price = args[ARGS_INDEX_PRICE]
        self.__location = args[ARGS_INDEX_LOCATION]
        self.__for_sale = True

    def __str__(self):
        print(
            "{username} posted a product for sale:\nFor sale! {post}".format(username=self._user, post=self._post_data))

    def discount(self, discount_rate, password):
        if discount_rate is not type(int):
            return None
        elif self.__for_sale is not True:
            return None
        elif self._user.check_password(password) is not True:
            return None
        else:
            discount = self.__price * (discount_rate / TOTAL_PERCENTAGE)
            self.__price -= discount
            print("Discount on {username} product! the new price is: {price.2f}".format(username=self._user,
                                                                                        price=self.__price))
