expense = [
18694.6,
413,
605,
200,
30,
1500,
90,
250,
3037.5,
4536,
441,
2103.24
]

income = [
38806.4,
1323
]

expense_total = 0
income_total = 0

for i in expense:
    expense_total += i
    
for y in income:
    income_total += y   

# tax


print("expense_total = " , expense_total)
print("income_total = ", income_total)
print("profit: ", income_total-expense_total)
print("tax: ")