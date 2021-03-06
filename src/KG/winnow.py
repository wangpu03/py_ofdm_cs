# -*- coding: utf-8 -*-

import sys
import random
import numpy as np
from numpy import size,array,transpose,zeros,shape,mod,split,hstack

sys.path.append('../')
from util.from_to import from2seq_to10

def xor_dot(seq,matrix):
    n = size(seq)
    row,col = shape(matrix)
    assert row==n,'seq and matrix do not match'
    result = zeros(col)
    for i in range(col):
        temp = matrix[:,i]
        for j in range(row):
            result[i] += (seq[j]*temp[j])
        result[i] = mod(result[i],2)
    return result

def split_into_block(bits,block_size):
    block_num = size(bits)/block_size
    bits = bits[0:block_num*block_size]  # 如果bits不能被size整除，则忽略bits最后无法被整除的点
    bits = split(bits,block_num)
    return bits
    
def get_parity_per_block(bits):
    parity = [np.sum(x)%2 for x in bits]
    return array(parity)

def compare_parity_per_block(my_parity,his_parity,my_bits):
    diff_bl = []
    for i in range(size(my_parity)):
        if my_parity[i] != his_parity[i]:
            diff_bl.append(i)               # 取出奇偶校验结果不同的段
        my_bits[i] = my_bits[i][1:]         # 舍弃第一个比特，维持数据的保密性
    return my_bits,diff_bl

def get_S_in_diff_block(bits,diff_bl,H):
    S = array([])
    for i in diff_bl:
        S = np.r_[S,xor_dot(bits[i],transpose(H))]
    S = split(S,size(diff_bl))
    return S

def get_Sc_in_diff_block(diff_bl,Sa,Sb):
    Sc = array([])
    for i in range(size(diff_bl)):
        Sc = np.r_[Sc, array([mod(Sa[i][j]+Sb[i][j],2) for j in range(3)])]
    Sc = split(Sc,size(diff_bl))
    return Sc

def correct_bits_by_Sc(bits,diff_bl,Sc):
    for i in range(size(diff_bl)):
        pos = from2seq_to10(Sc[i])
        if pos!=0:
            bits[diff_bl[i]][pos-1] = mod(bits[diff_bl[i]][pos-1]+1,2)
    return bits

def reorgnize_bits(bits,order):
    result = zeros(bits.shape)
    for i in range(size(bits)):
        result[i] = bits[order[i]]
    return result
        
def winnow(bits_A,bits_B,iteration): 
    for inter in range(iteration):
        
        # 迭代停止的条件：
        # 1.达到指定的迭代次数。此时bits_A与bits_B仍有可能存在误码
        # 2.BMR=0。说明bits_B的误比特已经被改正，不必再进行后续迭代。
        #if BMR(bits_A,bits_B)==0:
        #    return bits_A,bits_B
        
        ''' 进行第inter次迭代 '''

        # 二进制序列按照相同的随机顺序进行排序，使错误均匀地随机分布
        order = random.sample(range(size(bits_A)),size(bits_A))
        bits_A = reorgnize_bits(bits_A,order)
        bits_B = reorgnize_bits(bits_B,order)
        
        # 两端同时进行分组，每组的数据长度为2**m（m>2)，通常取m=3
        m = 3
        block_size = 2**m       
        bits_A = split_into_block(bits_A,block_size)
        bits_B = split_into_block(bits_B,block_size)
        
        # 计算各组的奇偶校验值
        parityA = get_parity_per_block(bits_A)    
        parityB = get_parity_per_block(bits_B)
        
        # 第一次信息交互
        # 通信的双方在公共信道中交换各组的奇偶校验位，并进行比较
        # 记录奇偶校验不同的分组
        bits_A,diff_bl = compare_parity_per_block(parityA,parityB,bits_A)
        bits_B,diff_bl = compare_parity_per_block(parityB,parityA,bits_B)
        
        # 后续计算校正子，都是针对奇偶校验不同的分组
        # 若所有分组的奇偶校验都一样，则不必再计算校正子了，可直接进行下次迭代
        if size(diff_bl) != 0:
        
            # 对于奇偶校验不同的组，计算各组的伴随式
            H = array([[0,0,0,1,1,1,1],[0,1,1,0,0,1,1],[1,0,1,0,1,0,1]])    
            Sa = get_S_in_diff_block(bits_A,diff_bl,H)
            Sb = get_S_in_diff_block(bits_B,diff_bl,H)
            
            # 第二次信息交互
            # Alice通过公开信道将其校正子Sa发送给 Bob
            # 对于奇偶校验不同的组，Bob计算Sc = Sa（异或）Sb
            Sc = get_Sc_in_diff_block(diff_bl,Sa,Sb)
            
            # Sc表示 Alice 和 Bob 第 i 个分组中错误比特的位置。
            # Bob 通过将该位置的位数值取反，纠正该分组的错误
            bits_B =  correct_bits_by_Sc(bits_B,diff_bl,Sc)
        
        bits_A = hstack(bits_A)
        bits_B = hstack(bits_B)
        
    return bits_A,bits_B