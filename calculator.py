#!/usr/bin/env python3

def kalkulator():
	try:
		liczba1 = float(input("Podaj pierwsza liczbe: "))
		operator = input("Podaj operator (+, -, *, /): ")
		liczba2 = float(input("Podaj druga liczbe: "))

		if operator == '+':
			wynik = liczba1 + liczba2
		elif operator == '-':
			wynik = liczba1 - liczba2
		elif operator == '*':
			wynik = liczba1 * liczba2
		elif operator == '/':
			wynik = liczba1 / liczba2
		else:
			print("Bledny wybór")
		return
		print("Wynik: ", wynik)
	except ValueError:
		print("Blad")
kalkulator()
