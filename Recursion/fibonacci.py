def fibonacci(x,n,i):
    if i == n:
        return x[1]
    else:
        i += 1
        # x.extend([x[len(x)-1]+x[len(x)-2]])
        return fibonacci([x[1], x[0]+x[1]],n,i)

def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n-1) + fibo(n-2))

x = [0,1] # const
i = 1 # const
n = 10 # kolikaty chcu

if n <= 0:
    print('Cant be less than 0')
elif n == 1:
    print('It is 0')
elif n == 2:
    print('It is 1')
else:
    print('Fibonacci seq is:', fibonacci(x,n,i))

print(fibo(n))