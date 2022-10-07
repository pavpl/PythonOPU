from Cartoon import Cartoon

class CartoonList:
    cartoonList = []

    def add(self, cartoon: Cartoon):
        self.cartoonList.append(cartoon.copy())

    def delete_last(self):
        self.cartoonList.pop()

    def __str__(self):
        for x in self.cartoonList:
            print(x[0], x[1])