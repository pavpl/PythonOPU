class Film:
    count = 0

    def __init__(self, name, year, duration):
        Film.count += 1
        print("Вызов конструктора №" + str(Film.count))
        self.name = name
        self.year = year
        self.duration = duration

    def __del__(self):
        Film.count -= 1
        print("Вызов деструктора №" + str(Film.count))

    def set_name(self):
        print("Enter name:")
        self.name = str(input())

    def set_year(self):
        print("Enter year of publishing:")
        self.year = int(input())

    def set_duration(self):
        print("Enter duration of cartoon(in minutes):")
        self.duration = str(input())

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_duration(self):
        return self.duration

    def __str__(self) -> str:
        return f"""
        Name - "{self.name}". Year of publishing is {self.year}. 
        Duration - {self.duration} minutes.

        """