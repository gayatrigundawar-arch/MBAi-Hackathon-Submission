'''
Members: Ankur Banga, Yukti Toshniwal
'''

x = int(input())
y = int(input())
ticket = 0

if (y< (x-10)):
    ticket = 10
elif (y >= x+6 and y <= x+20):
    ticket = 75
elif (y>=x+21 and y<x+40):
    ticket =  150
elif y>=x+40:
    ticket = 300
else:
    ticket = 0 

print(ticket)