def tah(pole, cislo_policka, symbol):
	nove_pole = pole[:cislo_policka] + pole[cislo_policka+1:]
	print(nove_pole)
	return nove_pole