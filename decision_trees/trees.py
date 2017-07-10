#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author: gywin

from __future__ import division

import operator
import numpy as np


def creat_dataset():
    dataset = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no' ],
               [0, 1, 'no' ],
               [0, 1, 'no' ]]
    labels = ['no surfacing', 'flippers']
    return dataset, labels

def calculate_entropy(dataset):
    num = len(dataset)
    label_counts = {}
    for feature_vector in dataset:
        curr_label = feature_vector[-1]
        if curr_label not in label_counts.keys():
            label_counts[curr_label] = 0
        label_counts[curr_label] += 1
    entropy = 0
    for key in label_counts:
        prob = label_counts[key] / num
        entropy -= prob * np.log2(prob)
    return entropy
	
dataset, labels = creat_dataset()
# print calculate_entropy(dataset)
# dataset[0][-1] = 'maybe'
# print calculate_entropy(dataset)


def split_dataset(dataset, axis, value):
    rest_dataset = []
    for feature_vector in dataset:
        if feature_vector[axis] == value:
            rest_vector = feature_vector[:axis]
            rest_vector.extend(feature_vector[axis+1:])
            rest_dataset.append(rest_vector)
    return rest_dataset
	
print split_dataset(dataset, 1, 1)

def choose_best_feature(dataset):
    feature_num = len(dataset[0]) - 1
    base_entropy = calculate_entropy(dataset)
    best_infogain = 0
    for i in range(feature_num):
        feature_values = [vector[i] for vector in dataset]
        unique_values = set(feature_values)
        new_entropy = 0
        for value in unique_values:
            sub_dataset = split_dataset(dataset, i, value)
            prob = len(sub_dataset) / len(dataset)
            new_entropy += prob * calculate_entropy(sub_dataset)
        infogain = base_entropy - new_entropy
        if infogain > best_infogain:
            best_infogain = infogain
            best_feature = i
    return best_feature

print choose_best_feature(dataset)
	

def majority_label(labels):
    labels_count = {}
    for vote in labels:
        if vote not in labels_count.keys():
            labels_count[vote] = 0
        labels_count[vote] += 1
    sorted_labels_count = sorted(labels_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_labels_count[0][0]
	
print majority_label(labels)

# def creat_tree(dataset, labels):
    # class_ls = [vector[-1] for vector in dataset]
    # if class_ls.count(class_ls[0]) == len(class_ls):
        # return class_ls[0]
    # if len(dataset[0]) == 1:
        # return majority_label(class_ls)
    # best_feature = choose_best_feature(dataset)
    # best_feature_label =labels[best_feature]
    # my_tree = {best_feature:{}}
    # del(labels[best_feature])
    # feature_values = [vector[best_feature] for vector in dataset]
    # unique_values = set(feature_values)
    # for value in unique_values:
        # sub_labels = labels[:]
        # my_tree[best_feature_label][value] = creat_tree(split_dataset(dataset, best_feature, value), sub_labels)
    # return my_tree

def create_tree(dataset, labels):
    class_list = [vector[-1] for vector in dataset]
    if class_list.count(class_list[0]) == len(class_list): 
        return class_list[0]
    if len(dataset[0]) == 1: 
        return majority_label(class_list)
    best_feat = choose_best_feature(dataset)
    best_feat_label = labels[best_feat]
    my_tree = {best_feat_label:{}}
    del(labels[best_feat])
    feat_values = [vector[best_feat] for vector in dataset]
    unique_vals = set(feat_values)
    for value in unique_vals:
        sub_labels = labels[:]      
        my_tree[best_feat_label][value] = create_tree(split_dataset(dataset, best_feat, value), sub_labels)
    return my_tree    
	
if __name__ == '__main__':
    dataset, labels = creat_dataset()
    # print createTree(dataset, labels)
    print create_tree(dataset, labels)
	
	
	
    # print dataset
    # print calculate_entropy(dataset)
    # dataset[0][-1] = 'maybe'
    # print dataset
    # print calculate_entropy(dataset)
    # print split_dataset(dataset, 0, 1)
    # print choose_best_feature(dataset)