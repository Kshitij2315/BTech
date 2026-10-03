# Exception vs Error:
#               Problems that occur during compile time are called Errors or Specifically Syntax Errors.
#               Error is also called as Bug.
# Logical Error ---> Improper Expected Output
# Exception are the errors that occur at Run-Time.
# Eg: ZeroDivisionError: division by zero,
# 	  NameError: name 'm1' is not defined. Did you mean: 'm'?
# KeyWords For Exceptional Handling:
# 							try,
# 							except,
# 							else,
# 							finally,  ---> irrespective to exception, return or break, this block executes.
# 							raise. ---> used to generate the exception forcefully.
# Hierarchy of Exception: Subchild Exception < Child Exception < Parent Exception

# BaseException
# │
# ├── BaseExceptionGroup
# │
# ├── GeneratorExit
# ├── KeyboardInterrupt
# ├── SystemExit
# │
# └── Exception
#     │
#     ├── ArithmeticError
#     │   ├── FloatingPointError
#     │   ├── OverflowError
#     │   └── ZeroDivisionError
#     │
#     ├── AssertionError
#     │
#     ├── AttributeError
#     │
#     ├── EOFError
#     │
#     ├── ImportError
#     │   └── ModuleNotFoundError
#     │
#     ├── LookupError
#     │   ├── IndexError
#     │   └── KeyError
#     │
#     ├── MemoryError
#     │
#     ├── NameError
#     │   └── UnboundLocalError
#     │
#     ├── OSError
#     │   ├── FileNotFoundError
#     │   ├── PermissionError
#     │   ├── IsADirectoryError
#     │   ├── NotADirectoryError
#     │   └── TimeoutError
#     │
#     ├── RuntimeError
#     │   ├── NotImplementedError
#     │   └── RecursionError
#     │
#     ├── StopIteration
#     │
#     ├── SyntaxError
#     │   └── IndentationError
#     │       └── TabError
#     │
#     ├── TypeError
#     │
#     ├── ValueError
#     │   └── UnicodeError
#     │       ├── UnicodeDecodeError
#     │       ├── UnicodeEncodeError
#     │       └── UnicodeTranslateError
#     │
#     └── Warning
#         ├── UserWarning
#         ├── DeprecationWarning
#         ├── RuntimeWarning
#         └── ...

class UserException(Exception):                            # User Defined Exceptions
	def __init__(self, value):
		self.value = value

	def display(self):
		return 'This is user defined exception', self.value

# WAP to print Division of two numbers.

def div(n, m):
	ans = n / m

	return ans

n = int(input("Enter a number: "))     # 5
m = int(input("Enter a number: "))     # 0    This is Exception

# if m == 0:
# 	print('Hey you fool Do not enter zero')
# 	exit()
#
# quo = div(n,m)

# if m != 0:
# 	quo = n / m
# 	print('Quotient: ', quo)
# else:
# 	print('Hey you fool Do not enter zero')

def robust_div(n, m):
	ans = 0
	try:
		ans = n / m
		return ans
	except ZeroDivisionError:
		print('Hey you fool Do not enter zero')
		# exit()
	except NameError:
		print('Use a valid variable')
		# exit()
	except:
		print('Please Check the program, there is an error occurred')

# quo = robust_div(n,'3b')

# print('Quotient: ', quo)

def nested_try(n,m):
	ans = None
	try:
		try:
			ans = n / m
		except ZeroDivisionError as zde:
			print('ZeroDivisionError:',zde)
			print('Hey you fool Do not enter zero')
			# exit()

	except NameError:
		print('Use a valid variable')
		# exit()
	except:
		print('Please Check the program, there is an error occurred')

	else:
		print('This is "else:" block')
		return ans
	finally:
		print('This is "finally:" block')
		raise UserException(100)

try:
	quo = nested_try(n,m)
	print('Quotient: ', quo)
except NameError as ne:
	print('NameError:', ne)
	print('Name Error from nested_try()')
except UserException as ue:
	print('This is UserException')
	print(ue.display())