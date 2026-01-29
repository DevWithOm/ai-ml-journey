from datetime import date
def calculate_age(birth_year):
    current_year =date.today().year
    age = current_year - birth_year
    return age
def rupees_to_dollars(salary_rupees):
    dollar_rate = 92
    salary_dollars = salary_rupees / dollar_rate
    return salary_dollars
birth_year = int(input("Enter your birth year: "))
salary_rupees = float(input("Enter your salary in rupees: "))
age = calculate_age(birth_year)