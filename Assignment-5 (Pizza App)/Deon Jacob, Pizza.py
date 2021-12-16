




tprice = []
choices = []
ctoppings = []


def main(c,p):
    choices.append(c)
    tprice.append(p)

def error():
    print('\t'"Error, this choice DOES-NOT exist!")
    print('\t'"     Please Choose Again!")


# WELCOME SCREEN
print()
print('\t''\t'"Welcome to YETI'S PIZZA app!")
input('\t''\t'" 'Always Trying To Please!'")

# DIRECTIONS
print()
print('\t'"_____________________________________________________")
print('\t''\t''\t''\t'"INDEX")
print('\t'"Use the number-pad to type in the Number at the")
print('\t'"left-hand-side to select an option")
print('\t'"_____________________________________________________")

# SIZE SELECTION
print()
size = ["", "Small - $10.00", "Medium - $12.00", "Large - $14.00", "Extra-Large - $14.96"]
for i,s in enumerate(size):
    if i == 0:
        print()
    else:
        print (i,'.', s)

#inputs size
print()
loop = True
while loop==True:
    c1 = int(input('\t' "# "))
    if c1 == 1:
        main('Small', 10.00)
        loop = False
    elif c1 == 2:
        main('Medium', 12.00)
        loop = False
    elif c1 == 3:
        main('Large', 14.00)
        loop = False
    elif c1 == 4:
        main('Extra-Large', 14.96)
        loop = False
    else:
        loop = True
        error()
        
print('\t', size[c1])
print('\t'"-----------------------------------------------------")


# TOPPINGS SELECTION
print()
print("     All TOPPINGS are $2.00 each")
print("     choose as many as you like.")
toppings = ["","Pepperoni", "Mushroom", "Extra-Cheese", "Sausage", "Onion", "Black-Olives", "Green-Pepper", "Fresh-Garlic", "Tomato", "Fresh-Basil"]
for i,t in enumerate(toppings):
    if i == 0:
        print()
    else:
        print (i,'.', t)
print("If your DONE-CHOOSING toppings then ENTER-0 ")

#inputs toppings
print()
loop = True
print("After each selction click Enter!")
while loop==True:
    c2 = int(input('\t' "# "))
    if c2 == 0:
        loop = False
    elif 0 < c2 <= 10:
        main(toppings[c2], 2.00)
        ctoppings.append(toppings[c2])
        print('\t', toppings[c2], "- $2.00")
        loop = True
    else:
        loop = True
        print('\t'"Error, this choice DOES-NOT exist!")
        print('\t'"     Please Choose Again!")

print()
print("Your toppings are", ctoppings)
print('\t'"-----------------------------------------------------")


# ADDRESS AND CONTACT INFO.
address = []

print()
print("Input your location and contact info.")
print()

n = input("  1st & Last Name: ")
print()
a = input("  Delivery Address: ")
print()
p = input("  Phone Number: ")
print()
e = input("  E-main: ")
address.append(n)
address.append(a)
address.append(p)
address.append(e)

print()
print('\t', address)
print('\t'"-----------------------------------------------------")
print()


# TIME
#adds time
def solve(s, n):
    h, m = map(int, s[:-2].split(':'))
    h %= 12
    if s[-2:] == 'pm':
        h += 12
    t = h * 60 + m + n
    h, m = divmod(t, 60)
    h %= 24
    suffix = 'a' if h < 12 else 'p'
    h %= 12
    if h == 0:
         h = 12
    return "{:02d}:{:02d}{}m".format(h, m, suffix)


print ("Enter the current time with (am/pm). Eg.(1:30pm):")
t = input('\t'"  ") 

dt = solve(t, 45)
print('\t'"-----------------------------------------------------")


#RECEIPT
print()
print("This E-RECEIPT will be e-mailed to you at", address[3], ";")
print('\t''\t'"________________________________________________")
print('\t''\t''\t''\t',"YETI'S PIZZA")
print()
print('\t''\t', "Size:")
print('\t''\t', "   ", choices[0], "    -    +$",tprice[0])
print('\t''\t', "Toppings:")
for choice in ctoppings:
       print ('\t''\t''\t', choice, "    -    +$ 2.00")
print('\t''\t''\t''\t''\t', "---------------")
#Adds all the prices
totalp = sum(tprice)
print('\t''\t', "Total", '\t''\t',"-", '\t''\t', "$", totalp)
#Adds all the GST
g = totalp * 1.05
g = round(g, 2)
print('\t''\t', "+GST", '\t''\t',"-", '\t''\t', "$", g)
print('\t''\t''\t''\t''\t', "---------------")
print('\t''\t', "Amount Due", '\t',"=", '\t', "$", g)
print('\t''\t'"________________________________________________")
print()
print('\t'"-----------------------------------------------------")


#Gives the user delivery time
print()
print("Your", choices[0], "pizza will be deliverd to", address[1], "around", dt)
print('\t'"-----------------------------------------------------")

#End message
print()
print('\t',"Thank you for using YETI'S PIZZA app!")
input('\t''\t'" 'Always Trying To Please!'")

print()
















