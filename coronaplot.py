import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.title('Growth Of Corona In India (Top 7 States)', fontdict={'fontweight':'bold', 'fontsize': 18})

patients = pd.read_csv(r"C:\Users\t4nis\Desktop\datascience\coronamh\patients_data.csv")
mh = patients.loc[(patients['detected_state'] == 'Maharashtra')]
tn = patients.loc[(patients['detected_state'] == 'Tamil Nadu')]

gj = patients.loc[(patients['detected_state'] == 'Gujarat')]
dl = patients.loc[(patients['detected_state'] == 'Delhi')]
mp = patients.loc[(patients['detected_state'] == 'Madhya Pradesh')]
raj = patients.loc[(patients['detected_state'] == 'Rajasthan')]
up = patients.loc[(patients['detected_state'] == 'Uttar Pradesh')]

mh.reset_index(drop=True, inplace=True)
gj.reset_index(drop=True, inplace=True)
dl.reset_index(drop=True, inplace=True)
mp.reset_index(drop=True, inplace=True)
raj.reset_index(drop=True, inplace=True)
up.reset_index(drop=True, inplace=True)
tn.reset_index(drop=True, inplace=True)


mh.to_csv('mhdata.csv')
tn.to_csv('tndata.csv')
gj.to_csv('gjdata.csv')
dl.to_csv('dldata.csv')
mp.to_csv('mpdata.csv')
raj.to_csv('rajdata.csv')
up.to_csv('updata.csv')

mhdatatotal = pd.read_csv(r'C:\Users\t4nis\Desktop\datascience\coronamh\mhdatatot.csv')
tndatatotal = pd.read_csv(r'C:\Users\t4nis\Desktop\datascience\coronamh\tndatatot.csv')

updatatotal = pd.read_csv(r'C:\Users\t4nis\Desktop\datascience\coronamh\updatatot.csv')
mpdatatotal = pd.read_csv(r'C:\Users\t4nis\Desktop\datascience\coronamh\mpdatatot.csv')
rajdatatotal = pd.read_csv(r'C:\Users\t4nis\Desktop\datascience\coronamh\rajdatatot.csv')
gjdatatotal = pd.read_csv(r'C:\Users\t4nis\Desktop\datascience\coronamh\gjdatatot.csv')
dldatatotal = pd.read_csv(r'C:\Users\t4nis\Desktop\datascience\coronamh\dldatatot.csv')


'''plt.xticks(mhdatatotal.date_announced[::3])

plt.xticks(tndatatotal.date_announced[::3])'''


plt.xlabel('Dates')
plt.ylabel('Patient Count')
plt.xticks(rotation=270)


plt.plot(mhdatatotal.date_announced,mhdatatotal.mh_count ,label='Maharashtra',)
plt.plot(tndatatotal.date_announced,tndatatotal.tn_count, label='Tamil Nadu',)
plt.plot(updatatotal.date_announced,updatatotal.up_count, label='Uttar Pradesh')
plt.plot(rajdatatotal.date_announced,rajdatatotal.raj_count, label='Rajasthan')
plt.plot(gjdatatotal.date_announced,gjdatatotal.gj_count, label='Gujarat')
plt.plot(dldatatotal.date_announced,dldatatotal.dl_count, label='Delhi')
plt.plot(mpdatatotal.date_announced,mpdatatotal.mp_count, label='Madhya Pradhesh')

plt.legend()
plt.show()

