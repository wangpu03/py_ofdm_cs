# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 12:35:06 2016

@author: My402
"""
import numpy as np
import random
from numpy import size,zeros
from function import BMR
    
def BINARY(X,Y):
    n = size(X)     # X(或Y)的二进制序列的长度
    
    if n==1:        #递归过程执行直到剩余一个比特，这个比特就是错误的比特。将Y的该位改正（即取反）
        Y[0] ^= 1
        return
        
    X_front = X[:n/2]            # 将X一分为二，计算前半部分的奇偶校验值
    par_X_front = np.sum(X_front)%2
    
    Y_front = Y[:n/2]            # 将Y一分为二，计算前半部分的奇偶校验值
    par_Y_front = np.sum(Y_front)%2
    
    if par_X_front==par_Y_front: # 如果对比结果一致，说明错误发生在后半段。对后半段递归执行二分法
        BINARY(X[n/2:],Y[n/2:])
    else:                        # 前半段对比结果不一致，说明错误发生在前半段。对前半段递归执行二分法        
        BINARY(X_front,Y_front)
    
def randfunc(n,ki):
    # 构造随机函数，将n个数据随机映射到BL个组上
    BL = int(n/ki)
    re = random.sample(range(n),n)          # 将n个数据打乱顺序重排
    f = zeros((BL,ki),dtype=np.int32)       # 映射函数
    for i in range(BL):                     # 每ki个映射到一个组上
        f[i,:] = re[i*ki:(i+1)*ki]
        f[i,:].sort()
    return f

def cascade(bit_A,bit_B):
    n = size(bit_A)
    q = BMR(bit_A,bit_B)

    ''' 第一轮 '''
    k1 = 10             # 第一轮的块长度
    BL = int(n/k1)      # 划分成BL个block
    # 划分成BL个block
    K1_A = bit_A.reshape(BL,k1)    
    K1_B = bit_B.reshape(BL,k1)
    # 校验位
    par1_A = np.sum(K1_A,axis=1)%2
    par1_B = np.sum(K1_B,axis=1)%2
    # 对校验位不匹配的block进行二分查找，纠正错误
    for v in range(BL):
        if par1_A[v] != par1_B[v]:
            BINARY(K1_A[v,:],K1_B[v,:])
    # 计算BMR        
    K1_A.shape = n
    K1_B.shape = n
    bmr = BMR(K1_A,K1_B)
    
    ''' 以后若干轮 '''
    # 为第二轮迭代做准备
    last_k = k1
    last_Ki_A = K1_A
    last_Ki_B = K1_B
    # 与传统方法相比，此处将bmr=0作为截至条件，而不是指定的迭代轮数作为截至条件
    while bmr!=0:
        ki = 2*last_k       # 第i轮的块长度i，设为上一轮块长度的2倍
        BL = int(n/ki)      # 第i轮的划分的块数

        # 如果n不能被ki整除，会造成错误。比如n=2000,ki=160,计算得BL=12
        # Ki_A = np.zeros((BL,ki))与Ki_A.shape = n会发生矛盾。此时进行差错控制，将下一轮的ki重置为10
        if BL*ki!=n:
            last_k = k1
            continue
        
        f = randfunc(n,ki)  # 随机置换函数
        # 对A、B同时用置换函数重排二进制序列
        Ki_A = zeros((BL,ki),dtype=np.int32)
        Ki_B = zeros((BL,ki),dtype=np.int32)
        for i in range(BL):
            for j in range(ki):
                Ki_A[i,j] = last_Ki_A[f[i,j]]
                Ki_B[i,j] = last_Ki_B[f[i,j]]
        # 校验位       
        pari_A = np.sum(Ki_A,axis=1)%2
        pari_B = np.sum(Ki_B,axis=1)%2
        # 对校验位不匹配的block进行二分查找，纠正错误
        for v in range(BL):
            if pari_A[v] != pari_B[v]:
                BINARY(Ki_A[v,:],Ki_B[v,:])
        # 计算BMR   
        Ki_A.shape = n
        Ki_B.shape = n
        bmr = BMR(Ki_A,Ki_B)
        # 为下一轮迭代做准备
        last_k = ki
        last_Ki_A = Ki_A
        last_Ki_B = Ki_B
    # cascade 后，被改正的Ki_A(或Ki_B)与原始的bit_A(或bit_B)相比，被打乱了顺序
    return Ki_A,Ki_B