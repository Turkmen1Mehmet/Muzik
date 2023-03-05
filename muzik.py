import pyaudio
import numpy as np
import matplotlib.pyplot as plt

# PyAudio nesnesi oluşturma
p = pyaudio.PyAudio()

# Mikrofon verilerini okuma
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                input=True,
                frames_per_buffer=1024)

# Grafik ayarlama
fig, ax = plt.subplots()
x = np.arange(0, 2*1024, 2)
line, = ax.plot(x, np.random.rand(1024), 'r-')
ax.set_ylim(-1, 1)
ax.set_xlim(0, 1024)
plt.setp(ax, xticks=[0, 1024], yticks=[-1, 0, 1])

# Verileri okuma ve grafik güncelleme
while True:
    # Verileri okuma
    data = stream.read(1024, exception_on_overflow=False)
    data = np.frombuffer(data, dtype=np.float32)
    
    # Grafik güncelleme
    line.set_ydata(data)
    plt.draw()
    plt.pause(0.001)
