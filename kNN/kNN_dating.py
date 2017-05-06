#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author: gywin

from __future__ import division
import os, sys

import numpy as np
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import kNN, data_processing


def plot(dataset, labels):
    fig = plt.figure()
    ax = fig.add_subplot(111)  
    ax.scatter(dataset[:, 0], dataset[:, 1], 15.0*np.array(labels), 15.0*np.array(labels))
    plt.show()    

def classify_person(fly, games, ice):
    dataset, labels = data_processing.file_to_matrix('datingTestSet.txt') 
    norm_dataset, ranges, vals_min = data_processing.auto_norm(dataset)
    input_data = ((np.array([fly, games, ice]) - vals_min) / ranges).tolist()
    k = 3    
    return kNN.classifier(input_data, norm_dataset, labels, k)
    
def test_dating():
    ratio = 0.1
    dataset, labels = data_processing.file_to_matrix('datingTestSet.txt') 
    norm_dataset, ranges, vals_min = data_processing.auto_norm(dataset)
    m = norm_dataset.shape[0]
    num = int(m*ratio)
    err_count = 0

    for i in range(num):
        classifer_res = kNN.classifier(norm_dataset[i, :].tolist(), norm_dataset[num:m, :], labels[num:m], 3)
        print "classifier result is %d, real answer is %d" % (classifer_res, labels[i])
        if classifer_res != labels[i]:
            err_count += 1
    print "total error rate is %f" % (err_count / num) 
   
if __name__ == '__main__':
   
    # dataset, labels = data_processing.file_to_matrix('datingTestSet.txt')   
    # norm_dataset, ranges, vals_min = data_processing.auto_norm(dataset)
    # plot(dataset, labels)
    # plot(norm_dataset, labels)
    
    print classify_person(10000, 10, 0.5)   
    
    test_dating()
  
    