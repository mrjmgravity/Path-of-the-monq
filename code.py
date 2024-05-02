def stars(rows):
    for i in range(rows*2 - 1):
        if i < rows:
            riadok = rows - i
            print(riadok * "*")
        else:
            riadok = i - rows + 2
            print(riadok * "*")

stars(5)

# Dostanem text a vypisat kolko krat sa vnom nachadza jednotlive pismena v ABCD v anj