from tkinter import Tk, Label, Entry, Button, StringVar, Radiobutton
from pytube import Playlist, YouTube
import os
import time

# Funciones del script original
def limpiar_nombre(nombre):
    caracteres_no_permitidos = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
    for caracter in caracteres_no_permitidos:
        nombre = nombre.replace(caracter, '_')
    return nombre

def descargar_audio():
    for i in range(len(playlist.video_urls)):
        yt = YouTube(playlist.video_urls[i])
        print("Audios restantes:", len(playlist.video_urls) - i)
        print(f"{yt.title} se está descargando...")

        clean_title = limpiar_nombre(yt.title)
        video_filename = f"{clean_title}.mp3"

        stream = yt.streams.get_by_itag(251)

        if stream:
            try:
                stream.download(output_path=carpeta_destino, filename=video_filename)
                print(f"{clean_title} se ha descargado correctamente.")
            except Exception as e:
                print(f"Error al descargar {clean_title}: {e}")
                print("Esperando 30 segundos antes de volver a intentar...")
                time.sleep(30)
        else:
            print(f"No se pudo encontrar una transmisión adecuada para {clean_title}.")

def descargar_video():
    for i in range(len(playlist.video_urls)):
        yt = YouTube(playlist.video_urls[i])
        print("Videos restantes:", len(playlist.video_urls) - i)
        print(f"{yt.title} se está descargando...")

        clean_title = limpiar_nombre(yt.title)
        video_filename = f"{clean_title}.mp4"

        stream = yt.streams.get_by_itag(22)

        if stream:
            try:
                stream.download(output_path=carpeta_destino, filename=video_filename)
                print(f"{clean_title} se ha descargado correctamente.")
            except Exception as e:
                print(f"Error al descargar {clean_title}: {e}")
                print("Esperando 30 segundos antes de volver a intentar...")
                time.sleep(30)
        else:
            print(f"No se pudo encontrar una transmisión adecuada para {clean_title}.")

def opciones():
    print('1. Descargar audio')
    print('2. Descargar video')

# Interfaz gráfica
def descargar():
    global nombre_carpeta
    url_playlist = entry_url.get()
    nombre_carpeta = entry_carpeta.get()
    global carpeta_destino
    carpeta_destino = os.path.join(os.getcwd(), nombre_carpeta)
    os.mkdir(carpeta_destino)
    global playlist
    playlist = Playlist(url_playlist)

    if selected_option.get() == "audio":
        descargar_audio()
    elif selected_option.get() == "video":
        descargar_video()

    result_label.config(text=f"Todos los videos se han descargado en la carpeta '{nombre_carpeta}'.")

# Configuración de la interfaz gráfica
root = Tk()
root.title("Descargador de Playlist")
root.iconbitmap('img\logo.ico')
root.geometry('400x500')
root.resizable(False,False)

# Etiquetas y entradas
Label(root, text="URL de la Playlist:").grid(row=0, column=0, padx=10, pady=10)
entry_url = Entry(root)
entry_url.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Nombre de la Carpeta:").grid(row=1, column=0, padx=10, pady=10)
entry_carpeta = Entry(root)
entry_carpeta.grid(row=1, column=1, padx=10, pady=10)

Label(root, text="Seleccione la opción:").grid(row=2, column=0, padx=10, pady=50)

# Botones de opción
selected_option = StringVar()
selected_option.set("audio")
Radiobutton(root, text="Descargar audio", variable=selected_option, value="audio").grid(row=2, column=1, pady=10)
Radiobutton(root, text="Descargar video", variable=selected_option, value="video").grid(row=2, column=2, pady=10)

Button(root, text="Descargar", command=descargar).grid(row=3, column=0, columnspan=3, pady=10)
Button(root, text="Salir", command=root.destroy).grid(row=4, column=0, columnspan=3, pady=10)

result_label = Label(root, text="")
result_label.grid(row=5, column=0, columnspan=3, pady=10)

root.mainloop()