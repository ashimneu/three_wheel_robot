#! /usr/bin/python

#-------------Kalman definitions -----------------

# covariance matrices
#Process covariance
#si decrementas suaviza pero es mas lenta su respuesta

R1 = 0.000002
R2 = 0.000003
R3 = 0.000004

R = [[R1,0,0],
     [0,R2,0],
     [0,0,R3]]

#Measurment covariance
#entre mas pequeno le cree mas a la medida

Q1 = 0.0007
Q2 = 0.0006
Q3 = 0.0008


Q = [[Q1,0,0],
     [0,Q2,0],
     [0,0,Q3]]

# kalman gains definition

k_1 = 0.0
k_2 = 0.0
k_3 = 0.0


K = [[K_1,0,0],
     [0,K_2,0],
     [0,0,k_3]]