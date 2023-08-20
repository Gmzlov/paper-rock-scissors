import random
import string
()

pwlength =14
pw=''
numbersletters = string.hexdigits
symbols = string.punctuation

alpha = numbersletters + symbols

for i in range(pwlength):
    pw += random.choice(alpha)

print(pw)