
cont = 0
for n in range(0, 172):
    cont += 1
    if n != 160 and n != 163 and n != 166 and n != 167 and n != 171 and n != 170 and n != 172:
        print(f'//*[@id="ddActivity_listbox"]/li[{n}]')
        print(type(n))
    else:
        print(f"El numero {n} no es correcto")



