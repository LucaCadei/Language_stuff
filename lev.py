"""Levenshtein distance calculator between strings"""
import time
import numpy as np
class Levenshtein:
    def __init__(self, source, target):
        assert isinstance(source,str) and isinstance(target,str)
        self.source, self.target = source, target
        self.distance_matrix = None
    
    def build_matrix(self):
        matrix = [[0 for x in range(len(self.target) + 1)] for y in range(len(self.source) + 1)]
        self.distance_matrix = matrix 

    def compute(self):
        self.build_matrix()
        for i in range(len(self.source) + 1): self.distance_matrix[i][0] = i
        for j in range(len(self.target) + 1): self.distance_matrix[0][j] = j
        
        for i in range(1,len(self.source) + 1):
            for j in range(1,len(self.target) + 1): 
                ins_del = 0 if self.source[i-1] == self.target[j-1] else 2
                    
                self.distance_matrix[i][j] = min(self.distance_matrix[i-1][j] + 1,self.distance_matrix[i-1][j-1] + ins_del, self.distance_matrix[i][j-1] + 1)
                print(np.array(self.distance_matrix))
        return self.distance_matrix[len(self.source)][len(self.target)]

    def compute_with_generators(self):
        pass
if __name__ == '__main__':
    l = Levenshtein('macaco','mammamia')
    l.build_matrix()
    print(l.compute())
