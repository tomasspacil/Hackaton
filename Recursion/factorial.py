#  In this exercise, you'll understand the concepts of recursion using selected programs - Fibonacci sequence, Factorial and others. We will also use Turtle graphics to simulate recursion in graphics.
#
#     Factorial
#     Fibonacci
#     Greatest common divisor
#
# Once we understand the principles of recursion, we can do fun stuff with Turtle graphics and DRAW:
#
#     a square
#     a nautilus
#     a spiral
#     a circles (many circles)
#     a hexagram
#     a Koch star
#     a snowflake
#     a tree
def makeFactorial(x):
    if x == 1:
        return x
    else:
        return x*makeFactorial(x-1)


number = 4

if number < 0:
    print('factorial doesn exist!')
elif number == 0:
    print ('factorial of 0 is 1!')
else:
    print ('Factorial of', number, 'is', makeFactorial(number))

