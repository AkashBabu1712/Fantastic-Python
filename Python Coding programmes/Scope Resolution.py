"""
What is Scope Resolution in Python?
Sometimes objects within the same scope have the same name but function differently. In such cases, scope resolution comes into play in Python automatically. A few examples of such behavior are:

Python modules namely 'math' and 'cmath' have a lot of functions that are common to both of them - log10(), acos(), exp() etc. To resolve this ambiguity, it is necessary to prefix them with their respective module, like math.exp() and cmath.exp().

What are Namespaces in Python?
A python namespace is a container where names are mapped to objects, they are used to avoid confusion in cases where the same names exist in different namespaces. They are created by modules, functions, classes, etc.

Scope resolution LEGB rule In Python -
In Python, the LEGB rule is used to decide the order in which the namespaces are to be searched for scope resolution. The scopes are listed below in terms of hierarchy(highest to lowest/narrowest to broadest):

Local(L): Defined inside function/class
Enclosed(E): Defined inside enclosing functions(Nested function concept)
Global(G): Defined at the uppermost level
Built-in(B): Reserved names in Python builtin modules

"""

pi = 'outer pi variable'

def print_pi():
	pi = 'inner pi variable'
	print(pi)

print_pi()
print(pi)

"""
Local Scope in Python
Local scope refers to variables defined in the current function. Always, a function will first look up a variable name in its local scope. Only if it does not find it there, the outer scopes are checked. 

"""

# Local Scope
pi = 'global pi variable'
def inner():
	pi = 'inner pi variable'
	print(pi)

inner()


# Enclosed Scope
pi = 'global pi variable'

def outer():
	pi = 'outer pi variable'
	def inner():
		#pi = 'inner pi variable'
		nonlocal pi
		print(pi)
	inner()

outer()
print(pi)


# Built-in Scope
from math import pi

# pi = 'global pi variable'

def outer():
	# pi = 'outer pi variable'
	def inner():
		# pi = 'inner pi variable'
		print(pi)
	inner()

outer()
