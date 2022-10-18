from Cartoon import Cartoon


class CartoonList:
    cartoonList = []

    def add(self, cartoon: Cartoon):
        self.cartoonList.append(cartoon.copy())

    def delete_last(self):
        self.cartoonList.pop()

    def __str__(self):
        for cartoon in self.cartoonList:
            print(cartoon[0], cartoon[1])

