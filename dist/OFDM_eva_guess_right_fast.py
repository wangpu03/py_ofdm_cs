# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from numpy import array

P = 36                      # 导频数，P<N
right = range(P+1)          # 非法用户猜对导频数
SNR = 15

lx_MSE = array([
-28.46782655, -28.20738802, -27.80113656, -27.71951844,
-28.23716048, -28.22583213, -28.16432122, -27.86624797,
-27.63220462, -27.65890167, -27.7789152 , -27.9118686 ,
-27.77964823, -28.0629433 , -27.98788457, -27.83450459,
-27.81468328, -28.22948396, -27.75380171, -27.28367584,
-28.13422079, -28.16182952, -27.78186018, -27.63565694,
-27.46189581, -28.31509725, -27.77908429, -27.87516377,
-27.14737967, -28.04538873, -27.90450917, -28.02662909,
-27.74148311, -27.78963884, -28.08668787, -27.90845203, -28.04481696
])

CS_MSE = array([
-27.43007203, -27.56163217, -27.16836235, -26.93826603,
-27.56865015, -27.32467413, -27.40621382, -27.45381431,
-26.67797486, -26.20097075, -26.90201834, -26.89789044,
-26.36924709, -27.4747852 , -26.82324773, -26.73523944,
-27.44959537, -26.7010854 , -27.2510467 , -26.80824894,
-27.30278188, -27.41161044, -26.89000264, -26.53320701,
-26.18998039, -27.81760343, -26.83540719, -26.39842251,
-26.28077279, -27.14812523, -27.21253653, -27.40974778,
-27.07340362, -26.51883154, -26.99336905, -27.07802845, -27.48740063
])

eva_MSE = array([
3.26393651,   3.02622608,   3.06220141,   2.85406115,
3.07815146,   2.86507529,   2.80943499,   2.70259955,
2.67659922,   2.6482193 ,   2.50906378,   2.13664591,
2.24537024,   2.16829079,   2.02055907,   1.76580209,
1.64450867,   1.44836856,   1.27578638,   0.78760396,
0.3722023 ,   0.36514201,  -0.08608719,  -0.42220233,
-0.89468646,  -0.99524812,  -1.80148175,  -2.77250587,
-2.93350736,  -3.95097924,  -4.49592282,  -5.94120535,
-7.11800045,  -8.42295995, -11.63269499, -15.09377049, -27.55924758
])

lx_BER = array([
0.00611345,  0.00582983,  0.00629727,  0.0077416 ,  0.00597164,
0.00614496,  0.00584559,  0.00601891,  0.00648109,  0.00636555,
0.00697479,  0.00620798,  0.0067437 ,  0.00553046,  0.00659139,
0.00653887,  0.00568277,  0.00629202,  0.00723739,  0.00667017,
0.00606618,  0.00565126,  0.00667542,  0.00630252,  0.00774685,
0.00574055,  0.00622374,  0.00651261,  0.00770483,  0.00647059,
0.00681197,  0.00640231,  0.00603466,  0.00684349,  0.00559349,
0.00668067,  0.00605567
])

CS_BER = array([
0.01494223,  0.00813025,  0.01559874,  0.01392332,  0.01372374,
0.0168855 ,  0.01293592,  0.00910714,  0.01569328,  0.02493697,
0.01572479,  0.01654412,  0.01998424,  0.0127521 ,  0.02015756,
0.01935924,  0.01045693,  0.02096113,  0.01402311,  0.01204832,
0.01969538,  0.01339811,  0.01419643,  0.01678571,  0.01560399,
0.01136555,  0.01195378,  0.02676996,  0.02476891,  0.01883403,
0.01170693,  0.01477416,  0.0122479 ,  0.01975315,  0.01856092,
0.01587185,  0.01730042
])

eva_BER = array([
0.49252626,  0.49277836,  0.49561975,  0.49085609,  0.49082458,
0.49156513,  0.48684349,  0.48884979,  0.4889916 ,  0.48344013,
0.48643908,  0.48522059,  0.48691176,  0.48416492,  0.48129202,
0.48101891,  0.47621324,  0.47651261,  0.47587185,  0.47014181,
0.46447479,  0.46780987,  0.46072479,  0.45892857,  0.44994748,
0.45178046,  0.43940651,  0.43498424,  0.42201155,  0.42160189,
0.40454307,  0.376875  ,  0.35969538,  0.33889706,  0.27788866,
0.21030462,  0.0066229
])

lx_SC = array([
0.94789404,  0.94939292,  0.94590322,  0.94067747,  0.94862364,
0.9477689 ,  0.94887676,  0.94760726,  0.94464957,  0.94444444,
0.94140144,  0.94623784,  0.94295062,  0.95051191,  0.94314262,
0.94320744,  0.94912964,  0.94471129,  0.93764751,  0.94023873,
0.94270343,  0.9470749 ,  0.93803776,  0.93880559,  0.92856394,
0.94171286,  0.93294257,  0.92783392,  0.91032723,  0.92009454,
0.90692621,  0.88868909,  0.86940729,  0.83903965,  0.76624865,
0.63692018,  0.00464723
])

CS_SC = array([
0.91785945,  0.93709673,  0.9137188 ,  0.9166285 ,  0.92451382,
0.9101453 ,  0.92625244,  0.93495467,  0.91548642,  0.88700972,
0.90906088,  0.90960336,  0.89711534,  0.92806615,  0.89877431,
0.89507132,  0.93478283,  0.89567808,  0.91412752,  0.92069798,
0.9006879 ,  0.92320876,  0.91102401,  0.90005372,  0.8956064 ,
0.92171706,  0.90935644,  0.86248736,  0.86174058,  0.8776923 ,
0.88779779,  0.86243074,  0.84667513,  0.79571032,  0.72310071,
0.60618858, -0.02801015])

plt.figure(figsize=(8,5))
plt.plot(right,lx_MSE, 'ko-', label='Scheme 1')  # Ideal user
plt.plot(right,CS_MSE, 'k^:', label='Scheme 2')  # Valid user
plt.plot(right,eva_MSE,'ks--',label='Evasdropper')
plt.xlabel('number of right pilots')
plt.ylabel('MSE(dB)')
plt.title('MSE of evasdropper by random guessing(SNR=%d)'%(SNR))
plt.legend()
plt.show()

plt.figure(figsize=(8,5))
plt.semilogy(right,lx_BER, 'ko-', label='Scheme 1')  # Ideal user
plt.semilogy(right,CS_BER, 'k^:', label='Scheme 2')  # Valid user
plt.semilogy(right,eva_BER,'ks--',label='Evasdropper')
plt.xlabel('number of right pilots')
plt.ylabel('BER')
plt.title('BER of evasdropper by random guessing(SNR=%d)'%(SNR))
plt.legend()
plt.show()

plt.figure(figsize=(8,5))
plt.plot(right,lx_SC,'ko-',label='Scheme 1')  # Ideal user
plt.plot(right,CS_SC,'k^:',label='Scheme 2')  # Valid user
plt.xlabel('number of right pilots')
plt.ylabel('Capacity(bit/symbol)')
plt.title('Security Capacity by random guessing(SNR=%d)'%(SNR))
plt.legend()
plt.ylim(0,1)
plt.show()