num1 = float(input("Son kiriting!\n>>>"))
num2 = float(input("Son kiriting!\n>>>"))
action = str(input("Belgini tanlang: Qo'shish(q), Ayirish(a), Bo'lish(b), Ko'paytirish(k)\n>>>"))

print("Javob:", end='')
if action.lower() == 'q':
    print(num1+num2)
elif action.lower() == 'a':
    print(num1-num2)
elif action.lower() == 'b':
    print(num1/num2)
else:
    print(num1*num2)