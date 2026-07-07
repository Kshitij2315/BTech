# WAP to count num of digit and alphabet in 'Nagpur-440010'

s = 'Nagpur-440010'
i=0
alpha = 0
digi = 0

while i < len(s):
    if 65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122:           # s.isalpha()
        alpha+=1
    elif 48 <= ord(s[i]) <= 57:                         # s.isdigit()
        digi+=1
    i+=1

print("Number of Alphabets:",alpha)
print("Number of Digits:",digi)