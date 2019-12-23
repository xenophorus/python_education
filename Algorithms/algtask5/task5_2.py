import collections as c

# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
# вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


def allinput(c):
    name = input('Ввелите название компании: ')
    q1 = int(input('Введите прибыль за первый квартал: '))
    q2 = int(input('Введите прибыль за второй квартал: '))
    q3 = int(input('Введите прибыль за третий квартал: '))
    q4 = int(input('Введите прибыль за четвертый квартал: '))
    return c(name, q1, q2, q3, q4)


def main():
    company = c.namedtuple('company', 'name, quart1, quart2, quart3, quart4')
    companies = []
    n = int(input('Введите количествое предприятий: '))
    for i in range(n):
        companies.append(allinput(company))
    print(companies)


main()

