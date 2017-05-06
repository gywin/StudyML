#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author: gywin

from __future__ import  division
import os
import numpy as np
import time

import kNN

__version__ = '1.0.0.170504'

def image_to_vector(filename):
    vectors = np.zeros((1, 1024))
    with open(filename, 'r') as fin:
        for i in range(32):
            line = fin.readline()
            for j in range(32):
                vectors[0, 32*i+j] = int(line[j])
    return vectors

def test_handwriting():
    # processing data
    labels = []
    training_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'trainingDigits')
    training_file = os.listdir(training_dir)
    training_mat = np.zeros((len(training_file), 1024))

    for index, filename in enumerate(training_file):
        labels.append(filename.split('.')[0].split('_')[0])
        training_mat[index, :] = image_to_vector(training_dir + '\\' + filename)[0]

    # testing classifier
    err_count = 0
    testing_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testDigits')
    testing_file = os.listdir(testing_dir)
    for index, filename in enumerate(testing_file):
        vector = image_to_vector(testing_dir + '\\' + filename)[0].tolist()
        result = kNN.classifier(vector, training_mat, labels, 3)
        # print "testing is %s, real is %s" % (result, filename.split('.')[0].split('_')[0])
        if result != filename.split('.')[0].split('_')[0]:
            err_count += 1
    print "error counts is %d" % err_count
    print "total error rate is %f" % (err_count / len(testing_file))

if __name__ == '__main__':

    start = time.clock()
    test_handwriting()
    end = time.clock()
    print start
    print end
    print 'spend time: %f' % (end - start)






   

