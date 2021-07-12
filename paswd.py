import random
import string

N = 10

upper = string.ascii_uppercase
lower = string.ascii_lowercase
nums = string.digits
symbol = string.punctuation
pswd = upper + lower + nums + symbol

password = ''.join(random.choice(pswd)

for i in range(N))
print(password)

