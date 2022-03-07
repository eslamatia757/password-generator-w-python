import random

upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lower_letters = upper_letters.lower()

digits = "0123456789"

symbols = "[]{(})'@~#:; >/?,<"

upps, lows, nums, syms = True, True, True, False

alll = ""

if upps:
	alll +=upper_letters
if lows:
	alll +=lower_letters
if nums:
	alll +=digits
if syms:
	alll +=symbols

length = 10

amount = 10

for i in range(amount):
	password = "".join(random.sample(alll,length ))
	print(password)
