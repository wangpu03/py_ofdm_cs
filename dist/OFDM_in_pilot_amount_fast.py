# -*- coding: utf-8 -*-

from numpy import arange
import matplotlib.pyplot as plt

P = arange(4,60,4)   # 导频数，P<N

val_MSE = [
    2.039907565013010782e+01,
    1.478051035255984758e+01,
    -2.260990780385335075e+00,
    -1.919630202557677023e+01,
    -2.876777867640224784e+01,
    -3.029162149266434056e+01,
    -3.038199534608603614e+01,
    -3.223367550133659165e+01,
    -3.351060138358628393e+01,
    -3.382283099396373416e+01,
    -3.404367484110679953e+01,
    -3.452844762418092728e+01,
    -3.441502870765231137e+01,
    -3.489217942250103022e+01
]

eva_MSE = [
    2.009703099409624372e+01,
    1.712576235789204659e+01,
    7.379011201879504434e+00,
    5.020971473018921216e+00,
    4.475671885462742416e+00,
    3.949778576712417166e+00,
    3.649725384147544549e+00,
    3.382007692825911072e+00,
    3.020897118109072021e+00,
    2.822189553417949970e+00,
    2.461273792621539780e+00,
    2.136134425177134144e+00,
    2.091840840678347746e+00,
    1.752795632982715679e+00
]

val_BER = [
    4.910482283464565056e-01,
    4.729563492063491581e-01,
    2.869099999999999984e-01,
    1.034576612903226334e-01,
    1.833333333333330567e-02,
    5.630122950819670818e-03,
    6.720041322314049097e-03,
    2.338541666666664551e-03,
    1.817226890756301096e-03,
    1.620762711864404864e-03,
    2.024572649572647931e-03,
    2.025862068965517127e-03,
    1.989130434782607464e-03,
    1.721491228070175499e-03
]

eva_BER = [
    4.950935039370078505e-01,
    4.991418650793651435e-01,
    4.902599999999997515e-01,
    4.894506048387094466e-01,
    4.895782520325202003e-01,
    4.932889344262296194e-01,
    4.916580578512396715e-01,
    4.911822916666667149e-01,
    4.934191176470589246e-01,
    4.922881355932204328e-01,
    4.909188034188033956e-01,
    4.919234913793100183e-01,
    4.929673913043478573e-01,
    4.932730263157895090e-01
]

SC = [
    8.457268052967525538e-04,
    5.049711802393840737e-03,
    1.841272410966526274e-01,
    6.789528278305340114e-01,
    9.247820993558562019e-01,
    9.646435103115384990e-01,
    9.595381435984080554e-01,
    9.771193620759706100e-01,
    9.816731266509447495e-01,
    9.829777290257681877e-01,
    9.792857707008617574e-01,
    9.793492025038567084e-01,
    9.795814236557209842e-01,
    9.821236212682262767e-01
]

plt.figure(figsize=(8,5))
plt.plot(P,val_MSE,'ko-', label='Valid user')
plt.plot(P,eva_MSE,'ks--',label='Evasdropper')
plt.xlabel('Pilot Amount')
plt.ylabel('MSE(dB)')
plt.title('MSE')
plt.legend()
plt.show()

plt.figure(figsize=(8,5))
plt.semilogy(P,val_BER,'ko-', label='Valid user')
plt.semilogy(P,eva_BER,'ks--',label='Evasdropper')
plt.xlabel('Pilot Amount')
plt.ylabel('BER')
plt.title('BER')
plt.legend()
plt.show()

plt.figure(figsize=(8,5))
plt.plot(P,SC,'ko-')
plt.xlabel('Pilot Amount')
plt.ylabel('Capacity(bit/symbol)')
plt.title('Security Capacity')
plt.show()