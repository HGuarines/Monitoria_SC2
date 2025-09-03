import control as ct
import scipy.signal as signal

num = [1, 1]
den = [3, 10, 2]

FT = ct.TransferFunction(num, den)
# print(FT)
display(FT)

EE = ct.tf2ss(num, den)
display(EE)
print(EE)

zero, polo, ganho = signal.tf2zpk(num, den)

print(f"Zeros: {zero}")
print(f"Pólos: {polo}")
print(f"Ganho: {ganho}")

