# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 14:08:54 2016

@author: My402
"""
import numpy as np
import matplotlib.pyplot as plt
from RSSI_sampling import sampling
from RSSI_quantization import quantization
from RSSI_cascade import cascade
from RSSI_tiger import tiger
from RSSI_RC4 import RC4
from function import BMR

plt.close('all')

def agreement(sampling_time,order,P):
    '''
    sampling_time: 采样周期。单位：s
    order: 量化阶数。可取order=2,3
    P: 导频数。
    输出：发送端、接收端、非法用户的导频位置序列
    '''
    
    ''' 采样 '''
    # 总的RSSI采样点为：采样时间/采样周期。每经过一个采样时间，更换一次密钥/导频图样。
    sampling_period = 1     # 采样周期1ms
    RSSI_A = sampling(sampling_period,sampling_time,1)
    RSSI_B = sampling(sampling_period,sampling_time,1)+np.random.randint(0,2,size=(1000,1))
    RSSI_E = sampling(sampling_period,sampling_time,3)
    
    ''' 多比特格雷码量化'''
    # 量化后的比特位数为：RSSI采样点数*量化阶数
    block_num = 1
    bit_A = quantization(RSSI_A,order,block_num)
    bit_B = quantization(RSSI_B,order,block_num)
    bit_E = quantization(RSSI_E,order,block_num)
    
    #print 'BMR_AB = %f'%(BMR(bit_A,bit_B))
    #print 'BMR_AE = %f'%(BMR(bit_A,bit_E))
    
    ''' 信息协调。采用cascade协议消除A、B的误比特 '''
    # A与E不会进行信息交互，E不可能指望通过cascade降低误比特率
    # 经过cascade，bit_A与bit_B的误比特率降为0.但是被改正的bit与原始的bit相比，被打乱了顺序。总位数不变
    bit_A,bit_B = cascade(bit_A,bit_B)
    
    #print '\nAfter cascade:\nBMR_AB = %f'%(BMR(bit_A,bit_B))
    
    ''' 密性放大。采用tiger哈希函数，任意位输入，输出192位密钥 '''
    # 若要产生相同的密钥，必须保证输入的bit是完全一样的。一比特的误差会经哈希输出后，会使误比特率达到0.5
    key_A = tiger(bit_A)
    key_B = tiger(bit_B)
    key_E = tiger(bit_E)
    
    ''' 生成导频。采用RC4，生成P个导频位置，每个位置取值0~512 '''
    pos_A = RC4(key_A,P)
    pos_B = RC4(key_B,P)
    pos_E = RC4(key_E,P)
    
    ''' 画图。画出RSSI的前100个采样点 
    plt.figure(figsize=(8,5))
    plt.plot(RSSI_A[0:100],'bo-',label='Sender device')
    plt.plot(RSSI_B[0:100],'g*-',label='Receiver device')
    plt.plot(RSSI_E[0:100],'rp-',label='Eavesdropper')
    plt.title('RSSI generated by communication parties(front 100 sampling)')
    plt.xlabel('Probes')
    plt.ylabel('RSSI(dBm)')
    plt.legend()'''
    
    return pos_A,pos_B,pos_E