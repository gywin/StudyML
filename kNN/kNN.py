#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author: gywin

import os, sys
import numpy as np
import operator

def classifier(ix, dataset, labels, k):
    """
    This func is about k Nearest Neighbors algorithm:
    ix is the data needed to be classified;
    dataset is the training data;
    labels is
    k is     
    """
    
    # calculate the distances between ix and all dataset
    ix = np.array(ix)
    dataset_size = dataset.shape[0]
    diff_matrix = np.tile(ix, (dataset_size,1)) - dataset
    sq_diff_matrix = diff_matrix ** 2
    sq_distances = sq_diff_matrix.sum(axis=1)
    distances = sq_distances ** 0.5
    sorted_distance_indices = distances.argsort()
    
    # select k smallest distances point    
    class_count = {}
    for i in range(k):
        selected_label = labels[sorted_distance_indices[i]]
        class_count[selected_label] = class_count.get(selected_label, 0) + 1
    sorted_class_count = sorted(class_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]
    
    


if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    import data_processing
    
    dataset, labels = data_processing.creat_dataset()
    print classifier([1, 0], dataset, labels, 3)
