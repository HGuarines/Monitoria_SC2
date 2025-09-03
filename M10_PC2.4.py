import control as ct
import numpy as np
import matplotlib.pyplot as plt

m = 10
k = 1
b = 0.5

num = [1]
den = [m, b, k]

G = ct.TransferFunction(num, den)
display(G)

# Definindo tempo da simulação
tempo = np.linspace(0, 200, 100)

tempo_degrau, resposta_degrau = ct.step_response(G, tempo)

plt.figure()
plt.plot(tempo_degrau, resposta_degrau, label='Resposta ao Degrau')
plt.title('Resposta ao Degrau do Sistema Massa-Mola-Amortecedor')
plt.xlabel('Tempo (s)')
plt.ylabel('Deslocamento (m)')
plt.grid()
plt.legend()
plt.show()
plt.savefig('M10_pc2.4.png')