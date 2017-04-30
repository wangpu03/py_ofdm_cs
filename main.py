# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 13:06:28 2016

@author: My402
"""

import os
import matplotlib.pyplot as plt
from channel import channel
from channelEstimation import channelEstimation

os.system('cls')
plt.close('all')
#import numpy
#numpy.random.seed(0)
L = 50                      # 信道长度
K = 6                       # 稀疏度/多径数，满足:K<<L
N = 128                     # 训练序列长度/载波数,满足：L<=N
SNR = [0,5,10,15,20,25,30]  # AWGN信道信噪比

''' 时域的信道脉冲响应'''
h = channel(L, K)

''' LS/MMSE/CS信道估计，得MSE/SER
    比较不同的信噪比SNR '''
(CS_MSE,CS_SER,LS_MSE,LS_SER,MMSE_MSE,MMSE_SER)= channelEstimation(K,h,SNR,N)
    
plt.figure(figsize=(8,5))
plt.plot(SNR,CS_MSE,'ro-',linewidth=1,label='CS')
plt.plot(SNR,LS_MSE,'bp-',linewidth=1,label='LS')
plt.plot(SNR,MMSE_MSE,'gs-',linewidth=1,label='MMSE')
plt.xlabel('SNR(dB)')
plt.ylabel('MSE(dB)')
plt.title('MSE of CS/LS/MMSE')
plt.legend()

''' SER存在问题，具体见function.py。此部分作图暂时取消。但是其他文件仍然保留SER部分，
留作接口。以后调试好SER后，可以减少代码的修改。
plt.figure(figsize=(8,5))
plt.semilogy(SNR,CS_SER,'ro-',linewidth=1,label='CS')
plt.semilogy(SNR,LS_SER,'bo-',linewidth=1,label='LS')
plt.semilogy(SNR,MMSE_SER,'go-',linewidth=1,label='MMSE')
plt.xlabel('SNR(dB)')
plt.ylabel('SER')
plt.title('SER of LS/MMSE')
plt.legend()
'''
print 'Program Finished'