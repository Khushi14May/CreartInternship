#calculate simple interest
def Si(x,y,z):
	si=(x*y*z)/100
	print('Simple interest is: ',si)


amt=int(input('Enter value of amount:'))
rate=int(input('Enter value of rate:'))
year=int(input('Enter value of year:'))	

Si(amt,rate,year)