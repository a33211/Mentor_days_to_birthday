# from main import  *
import calendar
from datetime import datetime

test_now = datetime.now().date()
test_birthday = "18.08.1990"
test_birthday_parsed = datetime.strptime(test_birthday, '%d.%m.%Y').date()
test_birthday_parsed_modified = test_birthday_parsed.replace(test_now.year)
if test_birthday_parsed_modified > test_now:
    delta = test_birthday_parsed_modified - test_now
    print(f'birthday will be this year in {delta.days} days')
else:
    next_birthday = test_birthday_parsed_modified.replace(year = test_now.year+1)
    delta = next_birthday - test_now
    print(f'birthday will be this year in {delta.days} days')


print(test_now)
print(f'Parsed time string {test_birthday_parsed}')
print(type(test_birthday_parsed))
print(test_birthday_parsed_modified)