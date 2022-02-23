
import math
import sys, traceback
import random
 

#The Extended Euclidian Algorithm
#->say what return is. 
def extGCD(a,b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = extGCD(b%a, a)
		return (g, x-(b//a)*y, y)


#A. Given input of two integers n and m, return either:
##(i) The gcd(m,n) if the gcd is different from 1, or:
##(ii) The inverse of m (mod n) if the gcd is equal to 1.
##Your output should make it clear which of the two has occurred.
def A(m,n):
	g, x, y = extGCD(m,n)
	if g != 1:
		return (0, g)
	else:
		return (1, x%n) # needs to indicate which occured... 


#B. Given input of three integers: (b,c,n) and a pair of ordered pairs (x1,y1) and (x2,y2)
##(i) Determine whether the two points are on the elliptic curve y^2 = x^3 + bx + c (mod n)
##(ii) If they are on the elliptic curve, either:
##(iia) Add them to get a third point, or else
##(iib) Explain that they cannot be added and return the reason why. 
def B(b,c,n,x1,y1,x2,y2):
	
	if x1 == "inf":
		return x2, y2
	if x2 == "inf":
		return x1, y1

	"""
	if (((y1%n)**2)%n) != ((((x1%n)**3)%n + (b*x1)%n + c%n)%n):
		print "The point (x1,y1) is not on the curve"
		sys.exit(0)
	elif (((y2%n)**2)%n) != ((((x2%n)**3)%n + (b*x2)%n + c%n)%n):
		print "The point (x2,y2) is not on the curve"
		sys.exit(0)
	else:
	"""
	# add the points (x1,y1) and (x2,y2) and return (x3,y3).
	
	if (x1==x2 and y1==y2):
		# if we are doubling...
		u = 3*x1**2 + b
		v = 2*y1
	else:         
		u = y1-y2
		v = x1-x2

	v = (v+n)%n #Make v positive.
	if v == 0:
		return "inf", "inf", "inf"

	check, v_inv = A(v,n)
	if check == 0:
		factor1 = v_inv;
		factor2 = int(n/v_inv);
		return "factors", factor1, factor2
		
		sys.exit(0)

	m = (v_inv*u)%n

	x3 = (-x1-x2+m**2)%n
	y3 = (-y1+m*(x1-x3))%n

	return "points", x3, y3

 

#Miller-Rabin primality test.
#~>A return value of False means n is certainly not prime. A return value of
#~>True means n is very likely a prime.
def miller_rabin(n, num_of_trials):
	assert n >= 2
    # special case 2
	if (n == 2):
		return True
    #ensure n is odd
	if n % 2 == 0:
		return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
	s = 0
	d = n-1
	while True:
		quotient, remainder = divmod(d, 2)
		if remainder == 1:
			break
		s += 1
		d = quotient
		assert(2**s * d == n-1)
 
		# test the base a to see whether it is a witness for the compositeness of n
		def try_composite(a):
			print(str(a)+" "+str(d)+" "+str(n))
			if pow(a, d, n) == 1:
				return False
			for i in range(s):
				if pow(a, 2**i * d, n) == n-1:
					return False
			return True # n is definitely composite
 
		for i in range(num_of_trials):
			a = random.randrange(2, n)
			if try_composite(a):
				return False
		return True # no base tested showed n as composite



def lenstra(n, bound):	

	if(miller_rabin(n,50)):
		return "prime", n, n
	while(True):
		#choose random eliptic curve, do lenstra.
		p1 = random.randrange(1,n)
		p2 = random.randrange(1,n)
		b = random.randrange(1, n)
		c = (((p2**2) - (p1**3) - b*p1) + n)%n

		q1,q2, = p1,p2

		i = 0
		while (i<=bound):
			check, q1, q2 = B(b,c,n,p1,p2,q1,q2)
			if(check=="factors"):
				return "comp", q1, q2
			elif(check == "inf"):
				break

def sagefactor(n):
	
	check, a, b, = lenstra(n,1000)
	if(check=="prime"):
		print("Government Prime: " + str(n))
	else:
		factors = []
		while(a!=2 and a%2 == 0):
			factors.append(2)
			a = a//2
		factors.append(a)
		
		while(True):
			check, a, b = lenstra(b,1000)
			
			while(a!=2 and a%2 == 0):
				factors.append(2)
				a = a//2
			
			factors.append(a)
			if(check=="prime"):
				break
	
				
		print("Composite:")
		factors.sort()
		s = str( factors.pop(0) )
		for factor in factors:
			s = s + " * " + str(factor)
		print("n = " + str(n) + " = " + s)




def main():
	print("Welcome. This is Sage's Factoring Program!")
	print("It uses Lenstra's Elliptic Curve Method, ")
	print("along with the Miller-Rabin primality test")
	
	cont = True
	while(cont):
		print(" ")
		n = eval(input( "Enter a number to factor:" ))
		
		sagefactor(n)
			
		print("")
		ans = input("Do you want to try another number (yes/no)?")
		if(ans=="n" or ans == "no"):
			return
		
				
if __name__ == "__main__":
    main()

