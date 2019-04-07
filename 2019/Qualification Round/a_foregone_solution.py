t = input()
for i in range(int(t)):
    n = int(input())
    a = n
    b = 0
    found = False

    while found == False:
        a_pos = str(a).find('4')
        if a_pos > -1:
            pwr = len(str(a)) - a_pos - 1
            tens = 10 ** pwr
            if a > tens:
                a = a - tens
                b = b + tens

        b_pos = str(b).find('4')
        if b_pos > -1:
            pwr = len(str(b)) - b_pos - 1
            tens = 10 ** pwr
            if b > tens:
                b = b - tens
                a = a + tens

        if str(a).find('4') == -1 and str(b).find('4') == -1:
            found = True
            break

    print("Case #"+str(i+1)+": "+str(a)+" "+str(b))
