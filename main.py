from datetime import datetime
from datetime import date


class PersonKeep:
    pass


class Person(PersonKeep):

    def __init__(self, name, birthday) -> str:
        self.name = name
        self.birthday = datetime.strptime(birthday, '%d.%m.%Y').date()

    def days_to_birthday(self):
        current = datetime.now().date()
        birthday_parsed_modified = self.birthday.replace(current.year)
        if birthday_parsed_modified > current:
            delta = birthday_parsed_modified - current
        else:
            next_birthday = birthday_parsed_modified.replace(current.year + 1)
            delta = next_birthday - current
        return delta.days
        # if datetime.MAXYEAR > current(year)


if __name__ == '__main__':
    person_A = Person('Andrew', '10.08.2020')
    person_B = Person('Benjamin', '02.02.1980')
    print(f'{person_A.name} has {person_A.days_to_birthday()} days left')
    print(f'{person_B.name} has {person_B.days_to_birthday()} days left')

sdfvhujsdhf