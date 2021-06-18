def vyhodnot(retezec):
	if 'xxx' in retezec:
		return('x')
	elif 'ooo' in retezec:
		return('o')
	elif '-' not in retezec:
		return '!'
	else:
		return '-'


def tah_hrace(pole, symbol):
	cislo_policka = int(input("Zadej policko, kam chces hrat: "))
	return tah(pole, cislo_policka, symbol)

def piskvorky():
	hraci_pole = 20 * '-'
	symbol_hrace = 'x'
	symbol_pocitace = 'o'
	while vyhodnot(hraci_pole) == '-':
		tah_hrace(hraci_pole, symbol_hrace)
		tah_pocitace(hraci_pole, symbol_pocitace)

piskvorky()
		
 
