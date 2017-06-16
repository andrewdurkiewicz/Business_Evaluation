#!usr/bin/python

asking = input('What amount are they asking for?')
equity = input('what is the percent of the business?')
result = 100*int(asking)/int(equity)
def find_exponent(result):
	exponent = 0
	a = result
	while a>=1:
		a = a/10
		exponent+=1
	return exponent -1
exponent = find_exponent(result)

def find_digit(exponent):
	if exponent<=5:
		a = "Thousand Dollars"
	else:
		a =  "Million Dollars"
	return a
suffix = find_digit(exponent)
leading_value = result/(10**(exponent))
if leading_value / int(leading_value) == 1:
	print("This values the business at %d %s"%( leading_value,suffix))
else:
	print("This values the business at %.1f %s"%( leading_value,suffix))
