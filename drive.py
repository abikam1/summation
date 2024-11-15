age = 25
has_license = True
a = input('Enter age:')
b = input('Has license(True/False):')

if int(a)>= 18 and b.lower() == 'true':
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")