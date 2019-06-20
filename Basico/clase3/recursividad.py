#Recursividad

#factorial iterativo
def factorial(num):
	fact = 1
	for x in range(1,num+1):
		fact *= x
	return fact

print(factorial(5))

#factorial recursivo

def factorialRec(num):
	if num==0 or num==1:
		return 1

	else:
		return num*factorialRec(num-1)
		

print(factorialRec(4))