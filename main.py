import PySimpleGUI as sg
from pytube import YouTube
import os

def baixar_video(link, path):
    try:
        yt = YouTube(link)
        video = yt.streams.get_highest_resolution()
        if video:
            print("Baixando...")
            video.download(output_path=path)
            print("Download Realizado!")
            sg.popup_ok("Download Realizado!")
        else:
            print("Vídeo não disponível em resolução máxima.")
            sg.popup_error("Vídeo não disponível em resolução máxima.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        sg.popup_error(f"Ocorreu um erro: {e}")

def main():
    sg.theme('Reddit')

    layout = [
        [sg.Text("Link do Vídeo: "), sg.InputText(size=(40,1))],
        [sg.Text("Diretório para Salvar:  "), sg.InputText(size=(30,1)), sg.FolderBrowse("Procurar")],
        [sg.Button('Baixar')],
    ]

    window = sg.Window('Baixador de Vídeos do YouTube', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == 'Baixar':
            link = values[0]
            path = values[1]

            if link and path:
                if os.path.exists(path):
                    baixar_video(link, path)
                else:
                    print("Caminho inválido.")
                    sg.popup_error("Caminho inválido.")
            else:
                print("Por favor, preencha todos os campos.")
                sg.popup_error("Por favor, preencha todos os campos.")

    window.close()

if __name__ == "__main__":
    main()
