#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author: gywin

import numpy as np


def creat_dataset():
    group = np.array([[1.0, 1.1],
                      [1.0, 1.0],
                      [0. , 0. ],
                      [0. , 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels
 
def get_label_id(label):
    if label == 'largeDoses':
        return 3
    elif label == 'smallDoses':
        return 2
    elif label == 'didntLike':
        return 1
 
def file_to_matrix(file_name):
    with open(file_name, 'r') as fin:
        lines = fin.readlines()
        
    data_set = np.zeros((len(lines), 3))
    class_labels = []
    for index, line in enumerate(lines):
        list_from_line = line.strip().split('\t')       
        data_set[index, :] = list_from_line[0: 3]
        class_labels.append(get_label_id(list_from_line[-1]))
        # class_labels.append(list_from_line[-1])
    return data_set, class_labels
    
def auto_norm(dataset):
    vals_min = dataset.min(axis=0)
    vals_max = dataset.max(axis=0)
    ranges = vals_max - vals_min
    norm_dataset = np.zeros(dataset.shape)
    m = dataset.shape[0]
    _1 = dataset - np.tile(vals_min, (m, 1))
    _2 = np.tile(ranges, (m, 1))
    norm_dataset = _1 / _2
    return norm_dataset, ranges, vals_min

    
