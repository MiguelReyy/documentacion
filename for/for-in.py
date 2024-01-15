for i in [0,1,2,3,4]:
    print("hola")

for i in [0,1,2,3,4]:
    print(i)

for i in [0,1,2,3,4]:
    print("Hola", end = " ")


email = False

for i in "santagmail.com":

    if i == "@":
        
        email = True

if email == True:
    print("El email es correcto")
else:
    print("El email no es correcto")