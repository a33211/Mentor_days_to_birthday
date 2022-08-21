from datetime import datetime
from datetime import date


class PersonKeep:
    pass


class Person(PersonKeep):

    def __init__(self, name, birthday) -> str:
        self.name = name
        self.birthday = birthday

    def days_to_birthday(self, birthday):
        current = datetime.now().date()
        birthday_parsed = datetime.strptime(birthday, '%d.%m.%Y').date()
        birthday_parsed_modified = birthday_parsed.replace(current.year)
        if birthday_parsed_modified > current:
            delta = birthday_parsed_modified - current
        else:
            next_birthday = birthday_parsed_modified.replace(current.year + 1)
            delta = next_birthday - current
        return delta
        print(f'you have {delta} days before birthday')
        # if datetime.MAXYEAR > current(year)


if __name__ == '__main__':
    person_A = Person('Andrew', '10.08.2020')
    person_B = Person('Benjamin', '02.02.1980')
    print(person_A.days_to_birthday())
    print(person_B.days_to_birthday())
