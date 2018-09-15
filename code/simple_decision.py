import numpy as np
from decision_tree import DecisionTree

class SimpleDecisionTree(DecisionTree):
    def predict(self, X):
        M, D = X.shape
        y = np.zeros(M)

        # GET VALUES FROM MODEL
        splitVariable = self.splitModel.splitVariable
        splitValue = self.splitModel.splitValue

        sub1_splitValue = self.subModel1.splitModel.splitValue
        sub1_splitVariable = self.subModel1.splitModel.splitVariable
        sub1_splitSat = self.subModel1.splitModel.splitSat
        sub1_splitNot = self.subModel1.splitModel.splitNot

        sub0_splitValue = self.subModel0.splitModel.splitValue
        sub0_splitVariable = self.subModel0.splitModel.splitVariable
        sub0_splitSat = self.subModel0.splitModel.splitSat
        sub0_splitNot = self.subModel0.splitModel.splitNot


        yhat = np.zeros(M)

        for m in range(M):
            if X[m, splitVariable] > splitValue:
                if X[m, sub1_splitVariable] > sub1_splitValue:
                    yhat[m] = sub1_splitSat
                else:
                    yhat[m] = sub1_splitNot
            else:
                if X[m, sub0_splitVariable] > sub0_splitValue:
                    yhat[m] = sub0_splitSat
                else:
                    yhat[m] = sub0_splitNot
        return yhat
