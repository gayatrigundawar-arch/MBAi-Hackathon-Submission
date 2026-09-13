'''
Members: Ankur Banga, Yukti Toshniwal
'''

temp = 0
theat = 0
tcool = 0
temp = int(input("Enter the average daily temperature: "))
while (temp!=-460):
    if temp<60:
        theat+=1
    elif temp>80:
        tcool+=1
    temp = int(input("Enter the average daily temperature: "))

print("Heating days: ", theat)
print("Cooling days: ", tcool)

