from Cartoon import Cartoon
from CartoonList import CartoonList

if __name__ == "__main__":
    cartoonList = CartoonList()

    cartoon1 = Cartoon("Cars", 2006, 92, "Lassetr")
    cartoon2 = Cartoon("Shrek", 2001, 90, "Adamson")

    cartoonList.add(cartoon1)
    cartoonList.add(cartoon2)

    print(cartoonList.cartoonList)