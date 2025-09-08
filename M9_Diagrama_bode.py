import matplotlib.pyplot as plt
from control import tf, bode_plot

# Define a função de transferência
numerador = [1, 4]
# numerador = [1, 4, 100]
denominador = [1, 3, 5]

sistema = tf(numerador, denominador)

# Plota diretamente o diagrama de Bode
bode_plot(sistema, dB=True, Hz=False, deg=True, omega_limits=(0.1, 100))

plt.show()
