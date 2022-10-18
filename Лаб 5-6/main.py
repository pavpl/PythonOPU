from tkinter import *

from Cartoon import Cartoon


class FirstWindow:
    def __init__(self, master):
        master.title("Лаб работа 5-6")
        master.geometry("300x100")

        frame = Frame(master)
        frame.pack(fill=X)

        self.btn1 = Button(frame, text="Добавить фильм", command=self.open_window)
        self.btn1.pack(fill=BOTH)
        self.quitBtn = Button(frame, text="Выйти", command=frame.quit)
        self.quitBtn.pack(fill=BOTH)

    @staticmethod
    def open_window():
        root1.destroy()
        root2 = Tk()
        SecondWindow(root2)
        root1.mainloop()


class SecondWindow(FirstWindow):
    cartoonList = []

    def __init__(self, master):
        master.protocol("WM_DELETE_WINDOW", self.close)
        var1 = StringVar()

        frame_top = Frame(master)
        frame_top.pack()
        frame1 = Frame(master)
        frame1.pack(side=TOP, fill=BOTH)

        self.label = Label(frame_top, text="Название фильма: ")
        self.label.grid(row=0, column=0, sticky=E)
        self.label1 = Label(frame_top, text="Год выхода: ")
        self.label1.grid(row=1, column=0, sticky=E)
        self.label2 = Label(frame_top, text="Длительность: ")
        self.label2.grid(row=2, column=0, sticky=E)
        self.label3 = Label(frame_top, text="Продюссер: ")
        self.label3.grid(row=3, column=0, sticky=E)

        self.txt = Entry(frame_top)
        self.txt.grid(row=0, column=1)
        self.txt1 = Entry(frame_top)
        self.txt1.grid(row=1, column=1)
        self.txt2 = Entry(frame_top)
        self.txt2.grid(row=2, column=1)
        self.txt3 = Entry(frame_top)
        self.txt3.grid(row=3, column=1)

        self.btn1 = Button(frame1, text="OK", command=self.write_to_file)
        self.btn1.pack(fill=X)
        self.showBtn = Button(frame1, text="Показать список", command=self.show_btn_click)
        self.showBtn.pack(fill=X)
        self.sortBtn = Button(frame1, text="Очистить список", command=self.clear_list)
        self.sortBtn.pack(fill=X)
        self.delBtn = Button(frame1, text="Удалить", command=self.delete_last)
        self.delBtn.pack(fill=X)
        self.closeBtn = Button(frame1, text='Закрыть', command=self.close)
        self.closeBtn.pack(fill=X)

        self.R1 = Radiobutton(master, text="По названию", variable=var1, value='1', command=self.sort_by_name)
        self.R1.pack(fill=X)
        self.R2 = Radiobutton(master, text="По году", variable=var1, value='2', command=self.sort_by_year)
        self.R2.pack(fill=X)
        self.R3 = Radiobutton(master, text="По длительноти", variable=var1, value='3', command=self.sort_by_duration)
        self.R3.pack(fill=X)
        self.R4 = Radiobutton(master, text="По продюссеру", variable=var1, value='4', command=self.sort_by_producer)
        self.R4.pack(fill=X)
        self.quickBtn = Button(master, text="Сортировать", command=self.sort)
        self.quickBtn.pack(fill=X)

    def compareByName(self, inputStr):
        return inputStr[0]

    def compareByYear(self, inputStr):
        return inputStr[1]

    def compareByDuration(self, inputStr):
        return inputStr[2]

    def compareByProducer(self, inputStr):
        return inputStr[3]

    def sort_by_name(self):
        self.cartoonList.sort(key=self.compareByName)

    def sort_by_year(self):
        self.cartoonList.sort(key=self.compareByYear)

    def sort_by_duration(self):
        self.cartoonList.sort(key=self.compareByDuration)

    def sort_by_producer(self):
        self.cartoonList.sort(key=self.compareByProducer)

    def sort(self):
        clear_btn_file = open("./data.cvs", "r+")
        clear_btn_file.truncate(0)

        if self.R1.select():
            self.sort_by_name()
        elif self.R2.select():
            self.sort_by_year()
        elif self.R3.select():
            self.sort_by_duration()
        elif self.R4.select():
            self.sort_by_producer()

        write_file = open("./data.cvs", "a")
        for cartoon in self.cartoonList:
            write_file.write(f"{cartoon[0]}, {cartoon[1]}, {cartoon[2]}, {cartoon[3]}\n")
        write_file.close()

    def delete_last(self):
        self.cartoonList.pop()
        file = open("./data.cvs", 'rb')
        pos = next = 0
        for line in file:
            pos = next  # position of beginning of this line
            next += len(line)  # compute position of beginning of next line
        file = open("./data.cvs", 'ab')
        file.truncate(pos)

    def write_to_file(self):
        cartoon = Cartoon(self.txt.get(), self.txt1.get(), self.txt2.get(), self.txt3.get())
        self.cartoonList.append(cartoon.copy())
        write_file = open("./data.cvs", "a")
        write_file.write(f"{self.txt.get()}, {self.txt1.get()}, {self.txt2.get()}, {self.txt3.get()}\n")
        write_file.close()

    def clear_list(self):
        self.cartoonList.clear()
        clear_btn_file = open("./data.cvs", "r+")
        clear_btn_file.truncate(0)

    def show_btn_click(self):
        show_file = open("./data.cvs", "r")
        print(show_file.read())
        show_file.close()

    @staticmethod
    def close():
        root1.quit()


if __name__ == "__main__":
    root1 = Tk()
    root1.title("Lab 5/6")
    a = FirstWindow(root1)
    root1.mainloop()
    clear_file = open("./data.cvs", "r+")
    clear_file.truncate(0)
