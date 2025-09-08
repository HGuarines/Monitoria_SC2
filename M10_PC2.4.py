""" Resolução da questão PC2.4 do Dorf"""

import control as ct
import numpy as np
import matplotlib.pyplot as plt

# Dados do problema
m = 10
k = 1
b = 0.5

# Função de transferência do sistema massa-mola-amortecedor
num = [1]
den = [m, b, k]
G = ct.TransferFunction(num, den)

# Definindo tempo de simulação
tempo = np.linspace(0, 200, 500)

# Resposta ao degrau unitário
tempo_degrau, resposta_degrau = ct.step_response(G, T=tempo)

# Plotando a resposta ao degrau
plt.figure()
plt.plot(tempo_degrau, resposta_degrau, label='Resposta ao Degrau Unitário')
plt.title('Resposta ao Degrau Unitário do Sistema Massa-Mola-Amortecedor')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()
plt.show()