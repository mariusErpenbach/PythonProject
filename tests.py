hallo = "willkommen"
skill = "noob"
Unterhaltungsgrad = "langer\nSatz"

print( f"{hallo} omethpwmritjüwmizj \n du {skill}")
# ist das gleiche wie
print ("{0} omethpwmritjüwmizj \n du {1} ".format(hallo,skill))

x=12
print(f"{x+12}")
print(Unterhaltungsgrad)

def test():
    global x
    x+=2
    return ("deine mudda")


print(x)
y = test()
print(x)



def test_function():
    a = 1


print(test_function())

# ========


def test_functionTwo(a,b):
    return min(a,b)

zahl1 = float(input("gib float 1"))
zahl2 = float(input("gib float 2"))
print(test_functionTwo(zahl1, zahl2))
