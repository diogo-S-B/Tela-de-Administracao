import PySimpleGUI as sg
from DB import BancoDados
import tabela


names = []


def Menu():
    sg.theme ('darkblue2')
    menu = [
        [sg.Text('')],
        [sg.Text('Administração - Usuários cadastrados em sistema',background_color="gray",text_color="white" ,font=(28),)],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Text(f'Consulta ID:        '), sg.Input(key='id_usuario', size=(30,1)),sg.Button("Buscar", key='id')],
        [sg.Text('Consulta NOME: '), sg.Input(key='nome_usuario', size=(30,1)),sg.Button("Buscar", key='nome')],
        [sg.Text('Consulta IDADE: '), sg.Input(key='idade_usuario', size=(30,1)),sg.Button("Buscar", key='Idade')],
        [sg.Text(key='erro')],
        [sg.Text(""),sg.Button("Cadastrar", size=(10,1))],
    ]
    return sg.Window('Administração', layout= menu, finalize=True, element_justification ="c", size=(800,470))

def Editar():
    edit = [
        [sg.Text('')],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Text('Nome:'),sg.Input(key='nome_edit')],
        [sg.Text('Idade:'),sg.Input(key='idade_edit')],
        [sg.Button('Voltar'),sg.Button('Editar')]
    ]

    return sg.Window('Editar', layout= edit, finalize=True, element_justification ="c", size=(800,470))

def Cadastrar():
    cadastro = [
        [sg.Text('')],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Text('id:         '), sg.Input(key='id')],
        [sg.Text('Nome:   '), sg.Input(key='nome')],
        [sg.Text('idade:    '), sg.Input(key='idade')],
                [sg.Text('')],
        [sg.Button('Voltar'),sg.Button("cadastrar")]
    ]
    return sg.Window('cadastrar', layout= cadastro, finalize=True, element_justification ="c", size=(800,470))

def Excluir():
    exclusao = [
        [sg.Text("Tem certeza que deseja excluir o usuário?")],
        [sg.Button('Sim', size=(8,1)), sg.Button('Nao', size=(8,1))],
        [sg.Text('', key='msg_exclusao')]
    ]
    return sg.Window('excluir', layout= exclusao, finalize=True, element_justification ="c", size=(300,100))

def Popups(msg):
    popup = [
        [sg.Text(f"Usuario {msg} com sucesso")],
        [sg.Button('Voltar', size=(8,1))],
        [sg.Text('', key='msg_exclusao')]
    ]
    return sg.Window('popcad', layout= popup, finalize=True, element_justification ="c", size=(300,100))




def GuiErro(tipo):        
    error = [
        sg.Text('Linha não selecionada')
    ]

window_menu, window_cadastro, window_editar, window_excluir, window_popup, window_erro, window_tabela = Menu(), None, None, None, None, None, None



while True:
    window, event, values = sg.read_all_windows()
    if window == window_menu and event == sg.WIN_CLOSED:
        break
    elif window == window_cadastro and event == sg.WIN_CLOSED:
        break
    elif window == window_editar and event == sg.WIN_CLOSED:
        break
    elif window == window_excluir and event == sg.WIN_CLOSED:
        break
    elif window == window_popup and event == sg.WIN_CLOSED:
        break
    elif window == window_erro and event == sg.WIN_CLOSED:
        break
    elif window == window_tabela and event == sg.WIN_CLOSED:
        break
    

    #Buscar pela idade:
    if window == window_menu and event == 'Idade':
        resp = values['idade_usuario']
        if resp == '':
            window['erro'].update('Usuário não encontrado')
        else:
            banco = [BancoDados('BuscaIdade', 0, '', resp)]
            if banco == 'Usuário não encontrado' or banco == [[]]:
                window['erro'].update('Usuário não encontrado')
            else:
                names = []
                for c in range(len(banco[0])):
                    names.append((banco[0][c]))


                window['erro'].update('')
                window_menu.close()


                pt = tabela.tela(tuple(names))
                if  pt == 'Voltar':
                    window_menu = Menu()
                elif pt[0] == 'edit':
                    window_editar = Editar()

    elif window == window_editar and event == 'Editar':
        nome = values['nome_edit']
        idade = values['idade_edit']
        banco = BancoDados('Editar', pt[1], nome, idade)

    
    #Busca pelo Nome:
    elif window == window_menu and event == 'nome':
        resp = values['nome_usuario']
        names = []

        if resp == '':
            window['erro'].update('Usuário não encontrado')
            
        else:
            banco = BancoDados('BuscaNome', 0, resp, 0)

            if banco == 'Usuário não encontrado' or banco == [[]]:
                window['erro'].update('Usuário não encontrado')

            else:
                window_menu.close()

                pt = tabela.tela(tuple(banco))
        
                if pt == 'Voltar':
                    window_menu = Menu()

                elif pt[0] == 'edit':
                     window_editar = Editar()

    #Busca pelo ID: 
    elif window == window_menu and event == 'id':
        resp = values['id_usuario']
        names = []
        if resp == '':
            window['erro'].update('Usuário não encontrado')
        else:
            banco = BancoDados('BuscaID', resp, '', 0)
            if banco == 'Usuário não encontrado' or banco == [[]]:
                window['erro'].update('Usuário não encontrado')
            else:
                window_menu.close()
                pt = tabela.tela(tuple(banco))
                if pt == 'Voltar':
                    window_menu = Menu()
                elif pt[0] == 'edit':
                     window_editar = Editar()
                     

    elif window == window_cadastro and event == 'Voltar':
        window_cadastro.hide()
        window_menu.un_hide()


#Cadastrar
    if window == window_menu and event == 'Cadastrar':
        window['erro'].update('')
        window_menu.hide()
        window_cadastro = Cadastrar()

    elif window == window_cadastro and event == 'cadastrar':
        id_cadastro = values['id']
        nome_cadastro = values['nome']
        idade_cadastro = values['idade']
        banco = BancoDados('Cadastrar', id_cadastro, nome_cadastro, idade_cadastro)
        window_popup = Popups('Cadastro')

    elif window == window_popup and event == 'Voltar':
        window_popup.hide()

    elif window == window_editar and event == 'Voltar':
        window_editar.close()
        t = tabela.tela()
        if t == 'Voltar':
            window_menu = Menu()

    #Editar
    elif window == window_editar and event == 'Editar':
        window_popup = Popups('editados')

    elif window == window_popup and event == 'Voltar':
        window_popup.close()







