from PySimpleGUI import PySimpleGUI as sg
import mysql.connector
from fvalidadorcpf import validarcpf

conexao = mysql.connector.connect(
       host='localhost',
       database='sistema3',
       user='root',
       password=''
    )


def erro(nome_erro):
    sg.theme('DarkBlue')
    layout = [
        [sg.Text(f'{nome_erro}', font=('bold'))]
    ]
    janela = sg.Window('erro', layout, size=(300, 70), element_justification='c')
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break


def janela_salvo():
    sg.theme('DarkBlue')
    layout = [
        [sg.Text('\tCADASTRO SALVO', font=('bold'))],
        [sg.Text()],
        [sg.Button('NOVO CADASTRO')]
    ]
    janela = sg.Window('salvo', layout, size=(300, 100))
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'NOVO CADASTRO':
            janela_add()
            janela.close()
            break


def janela_add():
    cpf = 'CPF'
    n = 'NOME'
    e = 'E-MAIL'
    t = 'TELEFONE'
    nas = 'NASCIMENTO'
    sg.theme('DarkBlue')
    layout2 = [
        [sg.Text(f'{cpf:<13}'), sg.Input(key='cpf', size=(20, 1))],
        [sg.Text(f'{n:<11}'), sg.Input(key='nome', size=(20, 1))],
        [sg.Text(f'{e:<12}'), sg.Input(key='email', size=(20, 1))],
        [sg.Text(f'{t:<4}'), sg.Input(key='telefone', size=(20, 1))],
        [sg.Text(f'{nas}'), sg.Input(key='nascimento', size=(10, 1))],
        [sg.Checkbox('MASCULINO', key='m'), sg.Checkbox('FEMININO', key='f')],
        [sg.Button('CADASTRAR')]
    ]

    janela2 = sg.Window('cadastrar', layout2)
    while True:
        eventos2, valores2 = janela2.read()
        if eventos2 == sg.WINDOW_CLOSED:
            break
        if eventos2 == 'CADASTRAR':
            if valores2['m']:
                valores2['m'] = 'M'
            if valores2['f']:
                valores2['m'] = 'F'
            add(valores2['cpf'], valores2['m'], valores2['nome'], valores2['email'], valores2['nascimento'],
                valores2['telefone'])
            janela2.close()
            break


def ver():
    cursor = conexao.cursor()
    cursor.execute('select * from cadastro order by nome;')
    comando = cursor.fetchall()

    # criando o layout
    sg.theme('DarkBlue')
    layout_cadastro = []
    provisoria = []
    cpf = 'CPF'
    s = 'SEXO'
    n = 'NOME'
    e = 'E-MAIL'
    nas = 'NASCIMENTO'
    t = 'TELEFONE'
    provisoria.append(sg.Text('FILTRAR POR CPF'))
    provisoria.append(sg.Input(key='filtro', size=(20, 1)))
    provisoria.append(sg.Button('FILTRAR'))
    layout_cadastro.append(provisoria[:])
    provisoria.clear()

    provisoria.append(sg.Text())
    layout_cadastro.append(provisoria[:])
    provisoria.clear()

    provisoria.append(sg.Text(f'{cpf:<19} {s:<7} {n:<40} {e:<40} {nas} {t:>30}'))
    layout_cadastro.append(provisoria[:])
    provisoria.clear()

    for c in comando:
        provisoria.append(sg.Text(f'{c[0]:<15} {c[1]}         {c[2]:<40} {c[3]:<40} {c[4]} {c[5]:>35}'))
        layout_cadastro.append(provisoria[:])
        provisoria.clear()

    # Criando a janela
    janela_cadastro = sg.Window('cadastro', layout_cadastro)

    # Eventos
    while True:
        eventos, valores = janela_cadastro.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'FILTRAR':
            try:
                print('chamando a função filtrar')
                filtrar(valores['filtro'])
            except:
                erro('CADASTRO NÃO ENCONTRADO')


def add(cpf, sexo, nome, email, nascimento, telefone):
    cursor = conexao.cursor()
    cursor.execute('select * from cadastro;')
    comando = cursor.fetchall()

    if validarcpf(cpf):
        #print('CPF VÁLIDO!')
        try:
            inserir = f"""
                        insert into cadastro (cpf, sexo, nome, email, nascimento, telefone)
                        values
                        ('{cpf}', '{sexo}', '{nome}', '{email}', '{nascimento}', '{telefone}')
                        """
            cursor.execute(inserir)
            conexao.commit()
        except mysql.connector.errors.IntegrityError:
            erro('ERRO DE DUPLICIDADE')

        else:
            print('PESSOA CADASTRADA COM SUCESSO')
            janela_salvo()

    else:
        erro('CPF INVÁLIDO')


def filtrar(filtro):
    cursor = conexao.cursor()
    cursor.execute(f"select * from cadastro where cpf = '{filtro}';")
    comando = cursor.fetchone()

    # Layout
    cpf = 'CPF'
    s = 'SEXO'
    n = 'NOME'
    e = 'E-MAIL'
    nas = 'NASCIMENTO'
    t = 'TELEFONE'

    sg.theme('DarkBlue')
    layout = [
        [sg.Text(f'PERFIL DO(A) {comando[2]:>15}', font=('bold'))],
        [sg.Text()],
        [sg.Text(f'DADOS PESSOAIS', font=('bold'))],
        [sg.Text(f'CPF: {comando[0]:<15} SEXO: {comando[1]:<10} DATA DE NASCIMENTO: {comando[4]}')],
        [sg.Text()],
        [sg.Text('CONTATOS', font=('bold'))],
        [sg.Text(f'E-MAIL: {comando[3]:<25} TELEFONE: {comando[5]}')]
    ]
    janela = sg.Window('cadastro', layout)
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
