# WAP to find whether a trangle is possible or not

a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if a + b + c == 180:
    print("Triangle is possible")
else:
    print("Triangle is not possible")