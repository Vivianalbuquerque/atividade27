f = str(input("digite um nome "))
f = f.upper().replace(" ","")
invert = f.upper() [::-1]
invert = invert.replace(" ","")
if f  == invert:
    print("políndromo")
else:
    print("não políndromo")