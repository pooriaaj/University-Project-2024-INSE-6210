USL = 6.6853
LSL = 0
C_bar = 4.2580
s = np.sqrt(C_bar)

Cp = (USL - LSL) / (6 * s)
Cpu = (USL - C_bar) / (3 * s)
Cpl = (C_bar - LSL) / (3 * s)
Cpk = min(Cpu, Cpl)

print(f'Process Capability (Cp): {Cp}')
print(f'Process Capability Index (Cpk): {Cpk}')
