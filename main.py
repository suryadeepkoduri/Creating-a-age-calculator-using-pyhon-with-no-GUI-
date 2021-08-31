# to calculate the age in years using basic python3 code
from datetime import date

birth_year = input('please input your birth year: ')

age = date.today().year - int(birth_year)
print(f'{age} years')
