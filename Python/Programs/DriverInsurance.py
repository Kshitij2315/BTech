# Granting insurance to drivers of a company

marital_status = input("Marital Status: ")
age = int(input("Age: "))
gender = input("Gender (M/F): ")
gender = gender[0]

if marital_status == 'Married' or marital_status == 'married':
    print("Insurance Granted")
elif marital_status == 'Unmarried' or marital_status == 'unmarried':
    if gender == "M" or gender == "m":
        if age >= 30:
            print("Insurance Granted")
        else:
            print("Insurance Ungranted")
    elif gender == "F" or gender == "f":
        if age >= 25:
            print("Insurance Granted")
        else:
            print("Insurance Ungranted")
