from Cartoon import Cartoon

if __name__ == "__main__":

    nm = str(input("Введите название фильма: "))
    yr = int(input("Введите год выхода: "))
    dr = int(input("Длительность фильма (в мин): "))
    pd = str(input("Введите имя режиссера: "))

    cartoon = Cartoon(nm, yr, dr, pd)

    cartoon.show()

    cartoon.set_name()
    cartoon.set_year()
    cartoon.set_duration()
    cartoon.set_producer()

    cartoon.show()