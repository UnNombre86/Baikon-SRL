import numpy as np
from scipy.io.wavfile import write
from flask import Flask, send_file
import io
import os
import subprocess
from pexpect import popen_spawn

app = Flask(__name__)

# Configuración del servidor
host = '127.0.0.1'
port = 5000

# Parámetros para la generación de audio de latidos del corazón
sample_rate = 44100  # Frecuencia de muestreo en Hz
duration_per_beat = 1.5  # Duración de cada latido en segundos
num_beats = 16  # Número total de latidos a simular

def generate_heartbeat_audio():
    # Frecuencias características del latido cardiaco (en Hz)
    heart_rate = 60  # Frecuencia cardiaca en latidos por minuto
    t = np.linspace(0, duration_per_beat, int(sample_rate * duration_per_beat), endpoint=False)
    
    # Parámetros del latido cardiaco (basados en investigación médica)
    a = 1.5  # Amplitud máxima de la sístole
    b = 0.6  # Duración relativa de la sístole
    c = 0.12  # Duración relativa de la sístole isovolumétrica
    d = 0.35  # Duración relativa de la diástole
    e = 0.05  # Duración relativa de la diástole isovolumétrica
    
    # Generar el patrón de latido cardiaco basado en los parámetros definidos
    heartbeat_pattern = (
        a * np.exp(-b * t) * (1 - np.exp(-heart_rate * (t - c))) * (t <= (c + d)) +
        a * np.exp(-b * t) * np.exp(-heart_rate * (t - c)) * (t > (c + d)) * (t <= (c + d + e))
    )
    
    # Normalizar la señal para valores de 16 bits (rango -32768 a 32767)
    normalized_signal = np.int16(heartbeat_pattern * 32767)
    
    return normalized_signal

heartbeats_audio = np.concatenate([generate_heartbeat_audio() for _ in range(num_beats)])
    
audio_io = io.BytesIO()
write(audio_io, sample_rate, heartbeats_audio)
audio_io.seek(0)

# Enviar el audio como archivo WAV para reproducir en la página web
file_path = os.path.join(os.getcwd(), 'heartbeats.wav')
with open(file_path, 'wb') as file:
    file.write(audio_io.read())

cmd = "cd D:\\pag-serv"
returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix

cmd = "git add heartbeats.wav" 
subprocess.call(cmd, shell=True)

cmd = 'git commit -m "python project update"'
subprocess.call(cmd, shell=True)

cmd = "git push "
subprocess.call(cmd, shell=True)

print('end of commands')