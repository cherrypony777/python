import random

a = input("Введите текст: ")
b = []
c = random.randint(0, 10)

shift = c ** len(a)

for char in a:
    b.append(chr(ord(char) + shift))

encrypted_text = "".join(b)

decrypted_list = []

for char in encrypted_text:
    decrypted_list.append(chr(ord(char) - shift))

decrypted_text = "".join(decrypted_list)

print(a)
print(encrypted_text)
print(decrypted_text)

