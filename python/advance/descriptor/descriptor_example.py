class Descriptor:
    def __init__(self) -> None:
        self.__name = ''

    def __get__(self, instance, owner):
        return self.__name
    
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError(f"field should be string")
        self.__name = value

    def __delete__(self, instance):
        del self.__name

class Person:
    name = Descriptor()
    email = Descriptor()

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f"I am {self.name} and my id {self.email}"
    
person_1 = Person("John Doe", "abc@abc.com")
print(person_1)
#person_1.name = 22
#person_1 = Person("John Doe", 22)

