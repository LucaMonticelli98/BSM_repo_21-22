#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:44:47 2022

@author: chiaramarzi
"""

# Complete the libraries importation

def my_plot(x, y, color, title, xlabel, ylabel):
    plt.figure()
    sns.linbeplot(x=x,y=y,color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

# Compliances values from Table III of Albanese et al., 2016
Cl = 0.00127
Ct = 0.00238
Cb = 0.0131
CA = 0.2
Ccw = 
# Unstre0.2455ssed volumes from Table III of Albanese et al., 2016
Vul = 34.4/1000
Vut = 6.63/1000
Vub = 18.7/1000
VuA = 1.263/1000
# Resistances values from Table III of Albanese et al., 2016
Rml = 1.021
Rlt = 0.3369
Rtb = 0.3063
RbA = 0.0817
dt = 0.0002

# Simulation of 20 seconds
Tstart=0
Tend=20
t=np.arrange(Tstart,Tend+dt. dt)
L=np.size(t)

# State variables
P1 =np.zeros(L)
P2 = np.zeros(L)
P3 = np.zeros(L)
P4 = np.zeros(L)
P5 = np.zeros(L)

# Auxiliary variables

Pl = np.zeros(L)
Ppl = np.zeros(L)
Pt = np.zeros(L)
Pb = np.zeros(L)
PA = np.zeros(L)

# Volumes
Vl = np.zeros(L)
Vt = np.zeros(L)
Vb = np.zeros(L)
VA = np.zeros(L)
VD = np.zeros(L)

# Natural breath definition
T = 5 # period of the natural breath
Amus=3
Pmus=Amus*np.cos(2*np*pi*t/T)-3
# Initial conditions

Ppl(0)=-5
VA(0)=2.3
P5(0)=ppl(0)-pmus(0)
P4(0)=VA(0)/CA(0)

for j in range t:
    Pl[j]=P1[j]
    Ppl[j]=P5[j]*Pmus[j]
    Pt[j]=P2[j]+Ppl[j]
    Pb[j]=P3[j]+Ppl[j]
    PA[j]=P4[j]+PPl[j]
    
    Vl[j]=Cl*Pl[j]+Vul
    Vt[j]=Ct*(Pt[j]-Ppl[j])+Vut
    Vb[j]=Cb*(Pb[j]-PPl[j])+Vub
    VA[j]=CA*(PA[j]-Ppl[j])+VuA
    VD[j]=Vl[j]+Vt[j]+Vb[j]
   
    dp1=(Pm(j)-Pl(j))/(Rml*Cl)-(Pl[j]-pt[j])/(Rlt*Cl)
    dp2=(Pl[j]-Pt[j])/(Rlt*Ct)-(Pt[j]-Pb[j])/(Rtb*Ct)
    dp3=(Pt[j]-Pb[j])/(Rtb*Cb)-(Pb[j]-PA[j])/(RbA*Cb)
    dp4=(Pb[j]-PA[j])/RbA*CA)
    dp5= (Pl[j]-Pt[j])/(Rblt*Ccw)
    
    P1[j+1]=P1[j]+dP1
    P2[j+1]=P2[j]+dP2
    P3[j+1]=P3[j]+dP3
    P4[j+1]=P4[j]+dP4
    P5[j+1]=P5[j]+dP5
# Pressures plots
my_plot(t,Pmus,'red','respiratoru muscle pressure','time(s)','$cmH:_20$')
my_plot(t,Ppl,'cyan','Ppl','Time(s)','$cmH:_20$')
my_plot(t,Pl,'green','Pl','time(s)','$cmH:_20$')
my_plot(t,Pt,'magenta','Pt','time(s)','$cmH:_20$')
my_plot(t,Pb,'yellow','Pb','time(s)','$cmH:_20$')
my_plot(t,PA,'Blu','Pb','time(s)','$cmH:_20$')

# Volumes plots


# Alveolar ventilation  (at equilibrium)
Vent = 
print("Ventiliation:", Vent)
