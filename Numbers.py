#Integer
a= 496
print(type(a))
print(a)

#Floats
e = 2.71828
z = 2 - 6.1j
print(type(z)) #complex
print(z.real) #2.0
print(type(z.imag)) #floats

'''
Rules of arithmetic - int, float, complex
operations: +,-
'''

x = 28 #int
y = 28.0 #float
print(float(28))
print(int(3.14))

#ints are narrower than floats
#floats are wider than ints

x = 1.732
print(1.732 + 0j)
complex(1.732 + 0j)
# float(1.732 + 0j) #This gives an error

#floats are narrower than complex numbers
#complex numbers are wider than floats

a = 2 #int
b = 6.0 #float
c = 12+0j #complex number

#Rule: Widen numbers so they're the same type

#Addition
print(a+b)

#Subtraction
print(b-a) #float-i

#Multiplication
print(a*7) #int*int

#Division - in py3 - if we divide 2 numbers value is a float, even if there is no remainder
#if you want remainder, use %
#if you want quotient, use //
print(c/b) #complex/float
print(16/5)
print(20/5)
print(16%5)
print(16//5)







