# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 16:46:36 2018

@author: pnola
"""

from cRidge_passing_times import *
import numpy as np
import h5py as hp

'''
a=hr_1_thresh_0()
thresh_rhodot = 0
thresh_s1 = 0
#'''
'''
a=hr_1_percentile_50()
thresh_rhodot = -np.percentile(-rhodot[rhodot<0],50)
thresh_s1 = -np.percentile(-s1[s1<0],50)
#'''
'''
a=hr_1_percentile_90()
thresh_rhodot = -np.percentile(-rhodot[rhodot<0],90)
thresh_s1 = -np.percentile(-s1[s1<0],90)
#'''

with hp.File('850mb_300m_10min_NAM_Rhodot_Origin_t=0-215hrs_Sept2017.hdf5','r') as data:
    rhodot = data['rhodot'][:].squeeze()
    s1 = data['s1'][:].squeeze()
    t = data['t'][:].squeeze()
    data.close()



rhodot_true_positive = 0
rhodot_false_positive = 0
rhodot_true_negative = 0
rhodot_false_negative = 0
for tt in range(1267):
    if len([x for x in a if x == tt])!=0:
        if rhodot[tt]<thresh_rhodot:    
            rhodot_true_positive += 1
        else:
            rhodot_false_negative += 1
    else:
        if rhodot[tt]<thresh_rhodot:    
            rhodot_false_positive += 1
        else:
            rhodot_true_negative += 1

rhodot_total_true = rhodot_true_positive+rhodot_true_negative
rhodot_total_false = rhodot_false_positive+rhodot_false_negative
rhodot_total_positive = rhodot_true_positive+rhodot_false_positive
rhodot_total_negative = rhodot_true_negative+rhodot_false_negative
rhodot_TPR=rhodot_true_positive/(rhodot_true_positive+rhodot_false_negative)
rhodot_FPR=rhodot_false_positive/(rhodot_false_positive+rhodot_true_negative)
print((rhodot_TPR,rhodot_FPR))

s1_true_positive = 0
s1_false_positive = 0
s1_true_negative = 0
s1_false_negative = 0
for tt in range(1267):
    if len([x for x in a if x == tt])!=0:
        if s1[tt]<thresh_s1:    
            s1_true_positive += 1
        else:
            s1_false_negative += 1
    else:
        if s1[tt]<thresh_s1:    
            s1_false_positive += 1
        else:
            s1_true_negative += 1

s1_total_true = s1_true_positive+s1_true_negative
s1_total_false = s1_false_positive+s1_false_negative
s1_total_positive = s1_true_positive+s1_false_positive
s1_total_negative = s1_true_negative+s1_false_negative
s1_TPR=s1_true_positive/(s1_true_positive+s1_false_negative)
s1_FPR=s1_false_positive/(s1_false_positive+s1_true_negative)
print((s1_TPR,s1_FPR))



#'''