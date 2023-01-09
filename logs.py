import PySimpleGUI as sg
# set global options for window
def erro():

    sg.theme('DarkRed1')
    print("ERRO")
    layout = [
        [
            sg.popup_ok('ERRO')
        ]
    ]


def baixan():
    sg.theme('Darkgreen1')
    layout = [
        [
            sg.popup_ok('Fazendo Download...')
        ]
    ]

def concl():
    sg.theme('Darkgreen3')
    layout = [
        [
            sg.popup_ok('Download Conluído...')
        ]
    ]
