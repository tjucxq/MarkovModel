#coding=utf-8
import sys
import re
import numpy as np
import copy

#A:状态转移矩阵， B:状态预测矩阵， Pai：初始状态分布，T：观测序列的个数， O：观测序列， N：状态个数
def Forward_Algorithm(A, B, Pai, T, O, N):
    startList = []
    nextList = []
    #计算时刻1的观测概率
    for i in range(N):
        temp = Pai[i]*B[i][O[0]]
        startList.append(temp)
    print startList
    #遍历从2到N的情况, 计算每一轮的结果
    for i in range(1,T):
        for m in range(N):
            temp = 0.0
            for n in range(N):
                #第i轮，需要第i-1轮的每个状态n转移到当前状态m,并计算m的预测的概率
                temp += A[n][m]*startList[n]*B[m][O[i]]
            nextList.append(temp)
        startList = copy.copy(nextList)
        nextList = []
        print startList
    return startList



if __name__ == "__main__":
    #Forward Algorithm
    #对应统计学习方法，P177的例子
    A = [[0.5, 0.2, 0.3], [0.3, 0.5, 0.2], [0.2, 0.3, 0.5]]
    B = [[0.5, 0.5], [0.4, 0.6], [0.7, 0.3]]
    Pai = [0.2, 0.4, 0.4]
    O = [0, 1, 0]
    T = 3
    result = Forward_Algorithm(A, B, Pai, T, O, 3)
    print sum(result)