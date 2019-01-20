
import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag
import pandas as pd



dane = pd.read_csv(r"C:\Users\NataliaA\Desktop\hci\sub-01_trial-04_3.csv",delimiter=',',engine='python')
czestProbk=200
t=np.linspace(0, 37.96, 200*37.96)
sygnal=dane['Kol1']
zfiltrem=ag.pasmowozaporowy(sygnal,czestProbk,49,51 )
zfiltrem2=ag.pasmowoprzepustowy(sygnal, czestProbk,1,50)
plt.plot(t,sygnal)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.show()

plt.plot(t,zfiltrem)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.show()

plt.plot(t,zfiltrem2)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.show()


print(dane)
