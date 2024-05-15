import PySimpleGUI as sg
from DB import BancoDados


def tela(x=0):

    if x == 0:
        x = BancoDados('ALL', 0, '', 0)
    elif x != 0:
        x = list(x) 


    head = [f'{"ID".center(10)}', f'{"NOME".center(30)}', f'{"IDADE".center(10)}']
    root = [

        [sg.Text('')],
        [sg.Text('')],
        [sg.Table(values=x, headings=head, auto_size_columns= True, display_row_numbers= True, enable_events=True, justification='center', num_rows=10, key='-TABLE-', row_height=35,)],
        [sg.Text('')],
        [sg.Button('Excluir', key='-EXCLUIR-', border_width=5), sg.Button('Editar', key='-EDITAR-', border_width= 5),sg.Button('Voltar', key = '-VOLTAR-', border_width= 5)]
    ]

    window_table = sg.Window('Tabela', layout=root, size=(900,600), element_justification='c', modal=True)

    while True:
        event, values = window_table.read()
        if event == sg.WIN_CLOSED:
            break
        
        elif window_table and event == '-VOLTAR-':
            break
        
        

        elif event == '-TABLE-':
            row = values['-TABLE-']


        try:
            id = x[row[0]][0]
            if event == '-EXCLUIR-' and row != '':
                if sg.popup_yes_no('Tem certeza que dejesa editar o usuário?') == 'Yes':
                    del x[row[0]]
                    BancoDados('Excluir', id)
                    window_table['-TABLE-'].update(x)
                else:
                    pass
        except:
            pass

        try:
            if event == '-EDITAR-':
                lista = ['edit', id, 'Po']
                window_table.close()
                return lista
        except:
            pass
        #retornar a tabela editar ao clicar no botao
            
    window_table.close()
    return 'Voltar'






