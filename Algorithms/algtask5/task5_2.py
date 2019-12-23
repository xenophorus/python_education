import collections as c

# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
# вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


def allinput(c):
    name = input('Введите название компании: ')
    q1 = float(input('Введите прибыль за первый квартал: '))
    q2 = float(input('Введите прибыль за второй квартал: '))
    q3 = float(input('Введите прибыль за третий квартал: '))
    q4 = float(input('Введите прибыль за четвертый квартал: '))
    avg = (q1 + q2 + q3 + q4) / 4
    return c(name, q1, q2, q3, q4, avg)


def minmax(comps,fun):
    a, b = [], []
    for i in comps:
        a.append(i.name)
        b.append(i.average)
    return a[b.index(fun(b))], fun(b)


def main():
    company = c.namedtuple('company', 'name, quart1, quart2, quart3, quart4, average')
    companies = []
    # companies = [company(name='asd', quart1=123.0, quart2=234.0, quart3=345.0, quart4=456.0, average=289.5),
    #               company(name='sdf', quart1=12.0, quart2=23.0, quart3=34.0, quart4=45.0, average=28.5),
    #               company(name='dfg', quart1=111.0, quart2=222.0, quart3=333.0, quart4=444.0, average=277.5)]
    avg_all = 0
    n = int(input('Введите количествое предприятий: '))
    for i in range(n):
        companies.append(allinput(company))
    # print(companies)
    print('Средняя прибыль для каждой компании: ')
    for i in range(n):
        print(f'\t{companies[i].name} - {companies[i].average}')
    print('Средняя прибыль суммарно за год: ')
    for i in range(n):
        avg_all = avg_all + companies[i].average
    print(f'\t{avg_all / n}')
    print('Минимальная прибыль у компании ')
    print('\t', *minmax(companies, min))
    print('Максимальная прибыль у компании ')
    print('\t', *minmax(companies, max))

# Дополнительные проверки не вводил ради того, чтоб успеть до дедлайна. Уповаю на идеального пользователя

main()
