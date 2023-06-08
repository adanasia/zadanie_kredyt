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

kwota_po_drugiej_racie = (1+ ((inflacja2+oprocentowanie_kredytu)/1200)) * kwota_po_pierwszej_racie - stala_wartosc_raty

kwota_po_trzeciej_racie = (1+ ((inflacja3+oprocentowanie_kredytu)/1200)) * kwota_po_drugiej_racie - stala_wartosc_raty

kwota_po_czwartej_racie = (1+ ((inflacja4+oprocentowanie_kredytu)/1200)) * kwota_po_trzeciej_racie - stala_wartosc_raty

kwota_po_piatej_racie = (1+ ((inflacja5+oprocentowanie_kredytu)/1200)) * kwota_po_czwartej_racie - stala_wartosc_raty

kwota_po_szostej_racie = (1+ ((inflacja6+oprocentowanie_kredytu)/1200)) * kwota_po_piatej_racie - stala_wartosc_raty

kwota_po_siodmej_racie = (1+ ((inflacja7+oprocentowanie_kredytu)/1200)) * kwota_po_szostej_racie - stala_wartosc_raty

kwota_po_osmej_racie = (1+ ((inflacja8+oprocentowanie_kredytu)/1200)) * kwota_po_siodmej_racie - stala_wartosc_raty

kwota_po_dziewiatej_racie = (1+ ((inflacja9+oprocentowanie_kredytu)/1200)) * kwota_po_osmej_racie - stala_wartosc_raty

kwota_po_dziesiatej_racie = (1+ ((inflacja10+oprocentowanie_kredytu)/1200)) * kwota_po_dziewiatej_racie - stala_wartosc_raty

kwota_po_jedenastej_racie = (1+ ((inflacja11+oprocentowanie_kredytu)/1200)) * kwota_po_dziesiatej_racie - stala_wartosc_raty

kwota_po_dwunastej_racie = (1+ ((inflacja12+oprocentowanie_kredytu)/1200)) * kwota_po_jedenastej_racie - stala_wartosc_raty

print(f"Twoja pozostała kwota kredytu to {kwota_po_pierwszej_racie}, to {kwota_poczatkowa_kredytu - kwota_po_pierwszej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_drugiej_racie}, to {kwota_po_pierwszej_racie - kwota_po_drugiej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_trzeciej_racie}, to {kwota_po_drugiej_racie - kwota_po_trzeciej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_czwartej_racie}, to {kwota_po_trzeciej_racie - kwota_po_czwartej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_piatej_racie}, to {kwota_po_czwartej_racie - kwota_po_piatej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_szostej_racie}, to {kwota_po_piatej_racie - kwota_po_szostej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_siodmej_racie}, to {kwota_po_szostej_racie - kwota_po_siodmej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_osmej_racie}, to {kwota_po_siodmej_racie - kwota_po_osmej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_dziewiatej_racie}, to {kwota_po_osmej_racie - kwota_po_dziewiatej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_dziesiatej_racie}, to {kwota_po_dziewiatej_racie - kwota_po_dziesiatej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_jedenastej_racie}, to {kwota_po_dziesiatej_racie - kwota_po_jedenastej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_dwunastej_racie}, to {kwota_po_jedenastej_racie - kwota_po_dwunastej_racie} mniej niż w poprzednim miesiącu.")


