import serial, wave, struct
import numpy as np

#config serial com
p_serial = serial.Serial ('COM4', 115200)
val_normal = []  
#funcion convertir de val anag a wav
def val_aud (val_anag, nombre_archivo):    
    #crea un nuevo archivo wav
    with wave.open (nombre_archivo, 'wb') as archivo_wav:
        archivo_wav.setnchannels (1)
        archivo_wav.setsampwidth (2)
        archivo_wav.setframerate (2000)
        for x in val_anag:
            data = struct.pack('<h', int(x))
            archivo_wav.writeframesraw(data)
        archivo_wav.close()

#lee datos arduino y guarda en lista
data_arduino = []
t_total = 20000
samplespersecond = 1
samples_total = t_total * samplespersecond

for _ in range (samples_total):
    if(p_serial.in_waiting != 0):
        a = int(''.join(filter(str.isdigit, str(p_serial.readline()))))
        b = np.interp(a, [0,4095], [-32000, 32000])
        data_arduino.append(b)
print(data_arduino)

#genera el audio wav
nombre_archivo = 'audio_arduino.wav'
val_aud (data_arduino,nombre_archivo)

def map_range(x, a, b, c, d):
    return (x-a)*(d-c)//(b-a)+c