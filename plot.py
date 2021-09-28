import numpy             as np
import matplotlib.pyplot as plt
import seaborn           as sns
sns.set(rc={'axes.facecolor':'whitesmoke'})


pour_plot = np.linspace(2,25,100)

voltage = [2.0 ,  5.0,  7.2,  8.9, 11.1, 12.9, 15.1,  17.1,  19.1,  21.0,  23.0,  23.9]
I1      = [8.9 , 15.6, 27.2, 35.8, 57.8, 72.1, 96.6, 116.0, 133.2, 148.2, 159.0, 162.0]

error_I1_plus = []
error_I1_minus = []
rapport_intensite = []
for i in range(len(voltage)):
    error_I1_plus.append(100*(I1[i]/205.5)+4.5)
    error_I1_minus.append(100*(I1[i]/205.5)-4.5)
    rapport_intensite.append((I1[i]/205.5)*100)
#print(rapport_intensite)
poly0 = np.polyfit(voltage,rapport_intensite,deg=3)
poly1_plot = []
for i in range(len(voltage)):
    poly1_plot.append(poly0[3]+poly0[2]*voltage[i]+poly0[1]*voltage[i]*voltage[i]+poly0[0]*voltage[i]*voltage[i]*voltage[i])


plt.plot(voltage,rapport_intensite,color='red',label='plot 100Mhz')
plt.plot(voltage,poly1_plot,color='gray')
plt.scatter(voltage,rapport_intensite,color='red')

voltage1 = [5.0, 7.0,  9.0, 11.1, 13.2, 15.1, 17.0, 19.0, 21.1, 23.1, 25.0]
I11      = [5.6, 8.3, 12.8, 19.3, 25.8, 32.6, 40.7, 49.1, 59.3, 68.0, 75.7]
I01      = [195.1,191.8, 185.4, 176.8, 167.7,160.9, 150.6, 140.4, 132.3, 119.5, 109.5]

rapport_intensite1 = []
for i in range(len(voltage1)):
    #rapport_intensite1.append(100*(I11[i]/I01[i]))
    rapport_intensite1.append(100*(I11[i]/200.6))
#print(rapport_intensite1)
poly01 = np.polyfit(voltage1,rapport_intensite1,deg=3)
poly1_plot1 = []
for i in range(len(voltage1)):
    poly1_plot1.append(poly01[3]+poly01[2]*voltage1[i]+poly01[1]*voltage1[i]*voltage1[i]+poly01[0]*voltage1[i]*voltage1[i]*voltage1[i])

plt.plot(voltage1,rapport_intensite1,color='blue',label='plot 61Mhz')
plt.plot(voltage1,poly1_plot1,color='gray')
plt.scatter(voltage1,rapport_intensite1,color='blue')


voltage2 = [5.0, 7.0,  8.9, 11.0, 13.0, 15.0, 17.0, 19.0, 20.0]
I12      = [10.2, 19.0, 31.9, 48.8, 71.0, 92.4, 115.7, 135.7, 142.3]
I02      = [190.8, 181.7, 168.8, 152.1, 129.6, 108.9, 85.6, 65.7, 57.9]

rapport_intensite2 = []
for i in range(len(voltage2)):
    #rapport_intensite2.append(100*(I12[i]/I02[i]))
    rapport_intensite2.append(100*(I12[i]/198.8))
#print(rapport_intensite2)
poly02 = np.polyfit(voltage2,rapport_intensite2,deg=3)
poly1_plot2 = []
for i in range(len(voltage2)):
    poly1_plot2.append(poly02[3]+poly02[2]*voltage2[i]+poly02[1]*voltage2[i]*voltage2[i]+poly02[0]*voltage2[i]*voltage2[i]*voltage2[i])

plt.plot(voltage2,rapport_intensite2,color='green',label='plot 140Mhz')
plt.scatter(voltage2,rapport_intensite2,color='green')
plt.plot(voltage2,poly1_plot2,color='gray')
#plt.plot(voltage,error_I1_plus,color='blue')
#plt.plot(voltage,error_I1_minus,color='green')
#plt.fill_between(voltage, error_I1_minus,error_I1_plus,color='green',alpha=0.2,label='error')
plt.legend()
plt.title('Efficiency (%) in function of the voltage (V)')
plt.xlabel('Voltage (V)')
plt.ylabel('efficiency (%)')
plt.savefig('voltage vs efficiency.png',dpi=300)
#plt.show()

'''
################################################################################
'''

plt.clf()
fig, axs = plt.subplots(2, 1)
plt.suptitle('Intensity of $I_0$ and $I_1$ ($\mu$W) in function of the voltage ($V$) ')

voltage3 = [5,7,9, 11.1,13.2,15.1,17,19,21.1,23.1,25.0]
I13 = [5.6,8.3,12.8,19.3,25.8,32.6,40.7,49.1,59.3,68,75.7]
I03 = [195.1,191.8,185.4,176.8,168.7,160.9,150.6,140.4,132.3,119.5,109.5]

axs[0].plot(voltage2,I12,color='red',label='$I_1 140 Mhz$')
axs[0].plot(voltage2,I02,color='blue',label='$I_0 140 Mhz$')

axs[1].plot(voltage3,I13,color='green',label='$I_1 61 Mhz$')
axs[1].plot(voltage3,I03,color='purple',label='$I_0 61 Mhz$')

axs[0].scatter(voltage2,I12,color='red')
axs[0].scatter(voltage2,I02,color='blue')

axs[1].scatter(voltage3,I13,color='green')
axs[1].scatter(voltage3,I03,color='purple')

axs[0].set_ylabel('Intensity ($\mu$W)')
axs[1].set_ylabel('Intensity ($\mu$W)')
axs[1].set_xlabel('Voltage (V)')
axs[0].legend()
axs[1].legend()
plt.savefig('I0 vs I1.png',dpi=300)

'''
################################################################################
'''

plt.clf()

frequency = [70,   80,    90,   100,   110,   120,   130,   140]
spacing   = [8.51, 9.62, 10.70, 12.11, 13.07, 14.42, 14.59, 16.37]
poly1 = np.polyfit(frequency,spacing,deg=1)
poly1_plot = []
for i in range(len(spacing)):
    poly1_plot.append(poly1[1]+poly1[0]*frequency[i])

plt.plot(frequency,spacing, color='red',label='plot')
plt.scatter(frequency,spacing, color='red')
plt.plot(frequency,poly1_plot, color='gray',label='fit')
plt.title('Spacing (mm) in function of the frequency (Mhz)')
plt.xlabel('Frequency (Mhz)')
plt.ylabel('Spacing (mm)')
plt.legend()
plt.savefig('spacing vs frequency.png',dpi=300)
#plt.show()

'''
################################################################################
'''

plt.clf()

frequency1 = [60, 70, 80, 90, 100, 110, 120, 130, 140]
IT1        = [200.1, 200.1, 200.1, 199.5, 199.3, 199.6, 199.8, 199.4, 199.2]
I1oui      = [16.8, 25.0, 50.7, 97.2, 41.2, 36.2, 64.2, 49.0,39.8 ]

rapport_oui = []
for i in range(len(frequency1)):
    rapport_oui.append(100*(I1oui[i]/IT1[i]))
#print(rapport_oui)

plt.scatter(frequency1,rapport_oui)
plt.plot(frequency1,rapport_oui)
plt.xlabel('frequency (Mhz)')
plt.ylabel('Efficiency $I_1/I_T$ (%)')
plt.title('Efficiency (%) in function of the frequency (Mhz)')
plt.savefig('intensity vs frequency.png',dpi=300)
#plt.show()
