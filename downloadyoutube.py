from pytube import YouTube
import moviepy.editor as mp
import re
import os

print('\033[31m* \033[m' * 50)
print('''Este código faz download de video do youtube.'''.center(100))
print('\033[31m* \033[m' * 50)

link = str(input('Digite o link do vídeo que deseja baixar: '))
path = input('Digite o caminho: ')
yt = YouTube(link)

print('Baixando...')
ys = yt.streams.filter(only_audio=False).first().download(path)
print('Download completo!')