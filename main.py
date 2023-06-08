inflacja1 = 1.592824484
inflacja2 = -0.453509101
inflacja3 = 2.324671717
inflacja4 = 1.261254407
inflacja5 = 1.782526286
inflacja6 = 2.329384541
inflacja7 = 1.502229842
inflacja8 = 1.782526286
inflacja9 = 2.328848994
inflacja10 = 0.616921348
inflacja11 = 2.352295886
inflacja12 = 0.337779545

oprocentowanie_kredytu = float(input("Podaj oprocentowanie kredytu: "))

kwota_poczatkowa_kredytu = float(input("Podaj kwote poczatkowa kredytu: "))

stala_wartosc_raty = float(input("Podaj stala wartosc raty: "))

kwota_po_pierwszej_racie = (1+ ((inflacja1+oprocentowanie_kredytu)/1200)) * kwota_poczatkowa_kredytu - stala_wartosc_raty
print(kwota_po_pierwszej_racie)
