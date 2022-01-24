'''
Команда проекта «Дом питомца» планирует большой корпоратив для своих волонтеров.
Вам необходимо написать программу, которая позволяла бы составлять список нескольких гостей.
Решите задачу с помощью метода конструктора и примените один из принципов наследования.
При выводе в консоль вы должны получить:  “Иван Петров, г.Москва, статус "Наставник"
'''
class Guest:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def desc(self):
        return f"Name: {self.name}, city: {self.city}"

class NewGuest(Guest):
        def __init__(self, name, city, status):
            super().__init__(name, city)
            self.status = status

        def get_all(self):
            return f" {self.name}, city: {self.city} , status: {self.status}"

a = NewGuest("Илья", "London", "Student")
person_1 = a.get_all()

b = NewGuest("Vasil", "Dubai", "Teacher")
person_2 = b.get_all()

print(person_1)
print(person_2)