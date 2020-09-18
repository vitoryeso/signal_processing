import numpy as np
import librosa
import soundfile as sf

# lendo um sinal de entrada no formato .wav, em mono
x, sample_rate = librosa.load('come-on-you-can-do-it.wav', mono=True)

# lendo a resposta ao impulso da igreja, em mono
impulse_response, _ = librosa.load('Church Schellingwoude.wav', mono=True)

# aplicando a convolução
y = np.convolve(x, impulse_response)

# salvando o resultado
sf.write('y.wav', y, sample_rate)
