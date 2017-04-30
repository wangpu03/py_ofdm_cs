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
import pdb
plt.close('all')

sampling_period,sampling_time = 1,1
RSSI_A = sampling(sampling_period,sampling_time,1)
RSSI_B = sampling(sampling_period,sampling_time,1)+np.random.randint(0,2,size=(1000,1))
RSSI_E = sampling(sampling_period,sampling_time,3)

order,block_num = 2,1
bit_A = quantization(RSSI_A,order,block_num)
bit_B = quantization(RSSI_B,order,block_num)
bit_E = quantization(RSSI_E,order,block_num)

print 'bmr_AB = %f'%(BMR(bit_A,bit_B))
print 'bmr_AE = %f'%(BMR(bit_A,bit_E))

bit_A,bit_B = cascade(bit_A,bit_B)
print '\nafter cascade:\nbmr_AB = %f'%(BMR(bit_A,bit_B))

key_A = tiger(bit_A)
key_B = tiger(bit_B)

pos_A = RC4(key_A,36)
pos_B = RC4(key_B,36)

plt.figure(figsize=(8,5))
plt.plot(RSSI_A[0:100],'bo-',label='Sender device')
plt.plot(RSSI_B[0:100],'g*-',label='Receiver device')
plt.plot(RSSI_E[0:100],'rp-',label='Eavesdropper')
plt.title('RSSI generated by communication parties(front 100 sampling)')
plt.xlabel('Probes')
plt.ylabel('RSSI(dBm)')
plt.legend()