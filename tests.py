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