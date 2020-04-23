print ('Quants anys estalviaras?')
anys = int(input('Escriu els anys: '))

print('Quants diners hi ha actualment al compte?')
principal = float(input('Escriu la quantitat actual del compte: '))

print('Quant invertiras mensualment?')
inv_mensual = float(input('Escriu la quantitat que invertiras: '))

print("Quin estimes que sera l'interes anual?")
interes = float(input("Escriu l'interes en nombres decimals (10% = 0.1): "))

inv_mensual = inv_mensual * 12
q_final = 0

for i in range(0, anys):
	if q_final == 0:
		q_final = principal

	q_final = (q_final + inv_mensual) * (1 + interes)

print("Aquesta es la quantitat que tindras despres de {} anys: " .format(anys) + "{:.2f}" .format(q_final)) #Mostra només 2 decimails