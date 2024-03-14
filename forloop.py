"""num_v=0
num_c=0
for i in 'patrick':
    if i in ['a','e','i','o','u']:
        print(f"{i} is a vowel")
        num_v+=1

    else:
        print(f"{i} is a consonant")
        num_c+=1
print(f"number of vowel is: {num_v}")
print(f"number of consonant is: {num_c}")"""

num_v=0
num_c=0
_string=input("enter your string:")
for i in _string.strip():
    if i in ['a','e','i','o','u']:
        print(f"{i} is a vowel")
        num_v+=1

    else:
        print(f"{i} is a consonant")
        num_c+=1
print(f"number of vowel is: {num_v}")
print(f"number of consonant is: {num_c}")

