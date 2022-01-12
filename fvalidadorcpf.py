#Validadorcpf1.0 criado com sucesso
#hospedagem do código: https://replit.com/@nathan00100/VALIDADORdeCPF#main.py
#validando um código para saber se pode ser um cpf ou não
#135246789, número que foi usado para desenvolver o programa
#cpf = [1, 3, 5, 2, 4, 6, 7, 8, 9, 5, 5]
def validarcpf(nums):
    cpf = []
    #nums = str(input('\033[33mDIGITE O CPF (APENAS OS NÚMEROS):\033[m ')).strip()
    for n in nums:
        i = int(n)
        cpf.append(i)

    if len(cpf) != 11:
        print('\033[31mO NÚMERO DE DÍGITOS INDICA QUE É UM CPF INVÁLIDO.\033[m')
    else:
        produto = []
        d = 0
        for c in range(10, 1, -1):
            produto.append(c * cpf[d])
            d += 1
        soma = sum(produto)

        n = 0
        p = []
        for x in range(11, 1, -1):
            p.append(x * cpf[n])
            n += 1
        s = sum(p)
        #soma = sum(produto)

        if soma % 11 >= 2:
            pdv = 11 - soma % 11
            if cpf[9] != pdv:
                print('\033[31mCPF INVÁLIDO\033[m')
                num = False
            else:
                if s % 11 >= 2:
                    sdv = 11 - s % 11
                    if cpf[10] != sdv:
                        print('\033[31mCPF INVÁLIDO\033[m')
                        num = False
                    else:
                        print('\033[32mCPF VÁLIDO\033[m')
                        num = True
                else:
                    sdv = 0
                    if cpf[10] != sdv:
                        print('\033[31mCPF INVÁLIDO\033[m')
                        num = False
                    else:
                        print('\033[32mCPF VÁLIDO\033[m')
                        num = True

        else:
            pdv = 0
            if cpf[9] != pdv:
                print('\033[31mCPF INVÁLIDO\033[m')
                num = False
            else:
                if s % 11 >= 2:
                    sdv = 11 - s % 11
                    if cpf[10] != sdv:
                        print('\033[31mCPF INVÁLIDO\033[m')
                        num = False
                    else:
                        print('\033[32mCPF VÁLIDO\033[m')
                        num = True
                else:
                    sdv = 0
                    if cpf[10] != sdv:
                        print('\033[31mCPF INVÁLIDO\033[m')
                        num = False
                    else:
                        print('\033[32mCPF VÁLIDO\033[m')
                        num = True
    return num
