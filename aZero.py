#Student Name: <Loklin Nord>
#Student ID: <873533332>

import pandas as pd
import numpy as np
import scipy

import A0_Utils as A0

## Question 1 - Basics

def add(a, b):
    # if both types are numeric, add them together and return
    if (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return round((a + b), 2)
    # if both types are lists, return the combined list
    elif (isinstance(a, (list)) and isinstance(b, (list))):
        return a + b
    # if types are not valid print, "Error" and return None
    elif not (isinstance(a, (int, float, str, list)) and isinstance(b, (int, float, str, list))):
        print("Error!")
        return None
    #if types are valid but mismatched, concatenate as strings
    else:
        return str(a) + str(b)


def calcMyGrade(AssignmentScores, MidtermScores, PracticumScores, ICAScores, Weights):
    #initialize variables
    AssignmentAvg = 0
    MidtermAvg = 0
    PracticumAvg = 0
    ICAAvg = 0

    #calculate section scores
    for x in AssignmentScores:
        AssignmentAvg += x
    AssignmentAvg = AssignmentAvg / len(AssignmentScores)

    for x in MidtermScores:
        MidtermAvg += x
    MidtermAvg = MidtermAvg / len(MidtermScores)

    for x in PracticumScores:
        PracticumAvg += x
    PracticumAvg = PracticumAvg / len(PracticumScores)

    for x in ICAScores:
        ICAAvg += x
    ICAAvg = ICAAvg / len(ICAScores)

    #calculate the weighted score, and return it (adjusted to be between 0 and 100)
    WeightedScore = (AssignmentAvg * Weights[0]) + (MidtermAvg * Weights[1]) + (PracticumAvg * Weights[2]) + (ICAAvg * Weights[3])
    return round(WeightedScore / 100, 2)

## Question 2 - Classes

class node:
    # constructor?
    def __init__(self, key, value) -> object:
        self.key = key
        self.value = value
        self.leftChild = None
        self.rightChild = None
    #return children method
    def getChildren(self):
        return [self.leftChild, self.rightChild]
    #return key method
    def getKey(self):
        return self.key
    #return value method
    def getValue(self):
        return self.value
    #functions for assigning children
    def assignLeftChild(self, node):
        self.leftChild = node
    def assignRightChild(self, node):
        self.rightChild = node
    #function to recursively return list of values of nodes in the tree in order
    def inOrderTraversal(self):
        tree = []
        #check to see if left child exists first, if so, recursively call
        if self.leftChild is not None:
            tree += self.leftChild.inOrderTraversal()
        #add the current node to the list
        tree.append(self.value)
        #check to see if right child exists, if so recursively call
        if self.rightChild is not None:
            tree += self.rightChild.inOrderTraversal()
        return tree


class queue:
    # constructor, starts with empty list
    def __init__(self) -> object:
        self.que = []
    #adds value to the end of list
    def push(self, value):
        self.que.append(value)
    #removes and returns value from the beginning of the list
    def pop(self):
        if self.checkSize() > 0:
            return self.que.pop(0)
        else:
            print("Cannot pop, the queue is empty!")
            return None
    #returns its size
    def checkSize(self):
        return len(self.que)


## Question 3 - Libraries

def generateMatrix(numRows, numcolumns, minVal, maxVal):
    matrix = []
    for i in range(numRows):
        row = []
        for j in range(numcolumns):
            row.append(float(np.random.randint(minVal, maxVal)))
        matrix.append(row)
    array = np.array(matrix)
    return array


def multiplyMat(m1, m2):
    try:
        new = np.matmul(m1, m2)
        return new
    except:
        print("Incompatible Matrices")

def statsTuple(a, b):
    try:
        sum_a = round(float(np.sum(a)), 2)
        mean_a = float(np.mean(a))
        min_a = float(np.min(a))
        max_a = float(np.max(a))

        sum_b = float(np.sum(b))
        mean_b = float(np.mean(b))
        min_b = float(np.min(b))
        max_b = float(np.max(b))

        pearson = round(float(scipy.stats.pearsonr(a, b)[0]), 2)
        spearman = round(float(scipy.stats.spearmanr(a, b)[0]), 2)

        tup = (sum_a, mean_a, min_a, max_a, sum_b, mean_b, min_b, max_b, pearson, spearman)
        print(tup)
        return tup
    except Exception as e:
        print(f"Error: {e}")
        return None

def pandas_func(fileName):
    df = pd.read_csv(fileName, delim_whitespace=True)
    ListOfMeans = []
    ListOfColumnNames = []
    index = 0
    for column in df:
        if pd.api.types.is_numeric_dtype(df[column]):
            ListOfMeans.append(round(df[column].mean(),2))
        else:
            ListOfColumnNames.append(df.columns[4])
        index += 1

    return ListOfMeans, ListOfColumnNames