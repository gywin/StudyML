#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author: gywin

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
    
    
    
if __name__ == '__main__':
   
    # dataset, labels = data_processing.file_to_matrix('datingTestSet.txt')   
    # norm_dataset, ranges, vals_min = data_processing.auto_norm(dataset)
    # plot(dataset, labels)
    # plot(norm_dataset, labels)
    
    print classify_person(10000, 10, 0.5)
  
    