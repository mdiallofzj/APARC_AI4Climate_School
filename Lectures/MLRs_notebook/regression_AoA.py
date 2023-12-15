#!/usr/bin/python
from netCDF4 import Dataset
from os.path import join


#import matplotlib.pyplot as plt
import numpy as np
#import numpy.matlib

######################## ANALYSIS ####################################
# Path allowing to access to the netcdf file
#path='/home/icg176/Documents/art_work/papers/Presentations/FP_lecture/Exercise/'
path='/media/icg176/KINGSTON/usb2019/Documents/art_work/papers/Presentations/FP_lecture/stat_lecture_exo/'
# Define the netcdf to be red
ncfile="AoA_CLaMS_timeseries_era.nc"
# Create the netcdf file path
fname = join(path,ncfile)
# Read the netcdf file
data = Dataset(fname,'r')
# Get variable contained in the netcdf file
AOA = data.variables['AoA'][:]
#AOA_deseas= data.variables['AoA_deseas'][:]
#AOA_ac= data.variables['Seas_cyc'][:]
mei= data.variables['ENSO_index'][:]
time=data.variables['time'][:]
data.close()

# Seasonal cycle:
ca=np.empty(12)
#l=0
for it in range(12):
    k=range(it,288,12)
    ca[it]=np.mean(AOA[k],axis=0) 
   
# Deseasonalizing AoA:
Ny=24
NN=12*Ny
AoA_des = np.arange(288)
seas_cyc=np.squeeze(np.transpose(np.matlib.repmat(ca,1,Ny)))
AoA_des=AOA-seas_cyc 

# Detrending AoA with polyfit:
delt=1/12
k=range(NN) #t is in year
t=delt*np.array(k)
tt=t-np.mean(t)
fit= np.polyfit(tt,AoA_des, 1)
trend=fit[0]
mean=fit[1]

# ENSO effect on AOA
AoA_des_detr=AoA_des-trend*(time-np.mean(time))- mean

# We can rewrite the line equation as AoA = Ap, where A = [[mei 1]] and p = [[m], [c]]. 
# Now use lstsq to solve for p:
# Fit a line, AoA = m.mei + c, through some noisy data-points:

A = np.vstack([mei, np.ones(len(mei))]).T
m, c = np.linalg.lstsq(A, AoA_des_detr, rcond=None)[0]

################### FIGURE ######################
# AoA & Seasonal cycle
zerol=0*np.empty(288)

plt.plot(time,zerol, '--', color='k', lw=1)
plt.plot(time,AOA-np.mean(AOA), '.', color='b', markersize=12, label='AoA')
plt.plot(time,2*(seas_cyc-np.mean(AOA)), '-', color='g', lw=4, label='2*Seasonal cycle')
plt.ylim(-0.5,0.5)
plt.xlim(1989, 2013)
plt.xlabel('year')
plt.ylabel('mean age of air anomalies (yr)')
plt.title('Temporal evolution of the different components of mean age')
plt.legend(loc='upper right', shadow=True, fontsize='x-large')
plt.show()

# Deseas_Detr_AoA & Trend
plt.plot(time,zerol, '--', color='k', lw=1)
plt.plot(time,AoA_des-np.mean(AoA_des), '.', color='b', markersize=12, label='Deseasonalized AoA')
plt.plot(time,trend*(time-np.mean(time)) + mean, '--', color='red', lw=4, label='AoA trend')
plt.ylim(-0.5,0.5)
plt.xlim(1989, 2013)
plt.xlabel('year')
plt.ylabel('mean age of air anomalies (yr)')
plt.title('Temporal evolution of the different components of mean age')
plt.legend(loc='upper right', shadow=True, fontsize='x-large')
plt.show()

# ENSO impact on AOA
plt.plot(time,zerol, '--', color='k', lw=1)
plt.plot(time,AoA_des_detr-np.mean(AoA_des_detr), '.', color='k', markersize=6, label='Deseasonalized and detrended AoA')
plt.plot(time,5*(m*(mei-np.mean(mei)) + c), '-', color='red', lw=4, label='5*ENSO impact on AoA')
plt.ylim(-0.5,0.5)
plt.xlim(1989, 2013)
plt.xlabel('year')
plt.ylabel('mean age of air variations (yr)')
plt.title('Temporal evolution of the different components of mean age')
plt.legend(loc='upper right', shadow=True, fontsize='x-large')
#plt.xticks([])
#plt.yticks([])
plt.show()




