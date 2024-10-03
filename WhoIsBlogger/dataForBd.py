#Some shitcode need refactor

import random

random.seed(12)

patientId = range(1, 31)
age = range(18, 55)
visitId = range(1, 91)
serviceId = range(1, 21)
date = range(2019, 2023)
cost = range(100, 2000)

for j in range(1):
    print("INSERT INTO patients(patientId, age) VALUES")
    for id in patientId:
        if id == patientId[-1]:
            print(f'({id}, {random.randint(age[0], age[-1])});')
        else:
            print(f'({id}, {random.randint(age[0], age[-1])}),')

  ### упаковать в функции
for i in range(1):
    print("INSERT INTO visits(visitId, patientId, serviceId, date) VALUES")
    for id in visitId:
        if id == visitId[-1]:
            print(f'({id}, {random.randint(patientId[0], patientId[-1])}, {random.randint(serviceId[0],serviceId[-1])}, "{random.randint(date[0], date[-1])}-{random.randint(1,13)}-{random.randint(1,31)}");')
        else:
            print(f'({id}, {random.randint(patientId[0], patientId[-1])}, {random.randint(serviceId[0],serviceId[-1])}, "{random.randint(date[0], date[-1])}-{random.randint(1,12)}-{random.randint(1,30)}"),')

for i in range(1):
    print("INSERT INTO Services(serviceId, cost) VALUES")
    for id in serviceId:
        if id == serviceId[-1]:
            print(f'({id}, {random.randint(cost[0], cost[-1])});')
        else:
            print(f'({id}, {random.randint(cost[0], cost[-1])}),')
