msg= input("Введите строку:\n")
if len(msg) < 2:
    print("Недостаточная длина строки!!!\n")
else:
    if len(msg) % 2 == 0:
        m1 = msg[:len(msg)//2]
    else:
        m1 = msg[:len(msg)//2+1]

    m2 = msg[len(msg) // 2*-1::]
    m3 = m2 + m1
    print(m3)
