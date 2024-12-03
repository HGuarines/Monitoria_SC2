import matplotlib.pyplot as plt
from control import tf, bode_plot, bode
a = 10**(9.5/20)
k = 2000*a
# Define a função de transferência
numerador = [k  , k*1000]
denominador = [1, 10010, 100000, 0]

sistema = tf(numerador, denominador)

# Plota diretamente o diagrama de Bode
bode_plot(sistema, dB=True, Hz=False, deg=True, omega_limits=(0.1, 100))

plt.show()
