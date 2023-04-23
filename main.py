num = int(input("Digite um número inteiro:"))

if num <= 0:
    print("inválido, número precisa ser maior que zero.")
else:
    count = 0
    numero = 2
    while count < num:
        primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                primo = False
                break
        if primo:
            print(numero)
            count += 1
        numero += 1