import bcrypt

password1 = b"Password1"
password2 = b"Password1"
password3 = b"Password"

hashed1 = bcrypt.hashpw(password1, bcrypt.gensalt())
hashed2 = bcrypt.hashpw(password2, bcrypt.gensalt())
hashed3 = bcrypt.hashpw(password3, bcrypt.gensalt())

print("Password one is: " + password1)
print("Password two is: " + password2)
print("Password three is: " + password3)

print("Password one's hash is: " + hashed1)
print("Password two's hash is: " + hashed2)
print("Password three's hash is: " + hashed3)

