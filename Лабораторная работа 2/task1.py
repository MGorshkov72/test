money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

money_capital += salary
money_capital -= spend

count = 0

while money_capital >= 0:
    money_capital += salary
    spend += spend * 0.05
    money_capital -= spend
    count += 1

print("Количество месяцев, которое можно протянуть без долгов:", count)
