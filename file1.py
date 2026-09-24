import random

choice = input("Выберите действие (1 — шифрование, 2 — дешифрование): ")

if choice == "1":
	a = input("Введите текст для шифрования: ")
	b = []
	c = random.randint(0, 10)
	shift = c ** len(a)

	for char in a:
		b.append(chr(ord(char) + shift))

	encrypted_text = "".join(b)

	print(f"Сгенерированное число c: {c}")
	print(f"Зашифрованный текст: {encrypted_text}")

elif choice == "2":
	a = input("Введите зашифрованный текст: ")
	c = int(input("Введите число c: "))
	b = []
	shift = c ** len(a)

	for char in a:
		b.append(chr(ord(char) - shift))

	decrypted_text = "".join(b)

	print(f"Расшифрованный текст: {decrypted_text}")

else:
	print("Неверный выбор! Введите 1 или 2.")
