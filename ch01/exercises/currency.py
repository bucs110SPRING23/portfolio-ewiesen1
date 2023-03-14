rate = input("What is the current exchange rate for the Euro to Dollar?")
rate = float(rate)
#cast rate to float because input automatically return strings but we are dealing with money.

amount = input("To convert from Euro to Dollar, please input your Euro amount.")
amount = float(amount)

total = rate*amount
print("You have ", total, " dollars.")

result = total - 3
print ("This ATM converter requires a $3.00 service fee. You now have ", result, " available.")
