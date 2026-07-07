# WAP to find Absolute value of a number

n = float(input("Enter a number: "))
ans = n

if n < 0:
    ans = n * -1

print("Absolute value of",n,"is:",ans)