# WAp to find the Type of Triangle---> Equilateral, Isosceles, Scalene

s1 = int(input("Enter the first Side: "))
s2 = int(input("Enter the second Side: "))
s3 = int(input("Enter the third Side: "))

if s1 == s2 and s3 == s1:
    print("The Triangle is Equilateral Triangle")
elif s1 == s2 or s3 == s2 or s1 == s3:
    print("The Triangle is Isosceles Triangle")
else:
    print("The Triangle is Scalene Triangle")