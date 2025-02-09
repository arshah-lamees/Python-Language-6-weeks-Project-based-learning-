def is_prime(n):#it takes number and check by taking modulous 
    if n <= 1:
        return print(f"the number {n} is not prime\n")  
    for i in range(2, int(n**0.5) + 1):#for the upper limit of range we took sqrt of number and add 1 in it 
        if n % i == 0:
            return print(f"the number {n} is not prime\n")  
    return print(f"the number {n} is prime\n and its fibonacci series : {fibonacci(n)}")  
def fibonacci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    if n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib
def main():
    num = int(input("Enter a number: "))
    is_prime(num)
main()