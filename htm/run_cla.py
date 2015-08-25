'''
Created on Aug 15, 2015

@author: seth
'''
import csv
import datetime
from config import cla_setup
from model_params import cla_model_params
from nupic.frameworks.opf.modelfactory import ModelFactory
from utils import nupic_output
from nupic.data.inference_shifter import InferenceShifter
import os



def createModel():
    model = ModelFactory.create(cla_model_params.MODEL_PARAMS)
    model.enableInference(
            {"predictedField": cla_setup.getPredictedFiled()})
    return model

def runModel(model):
    inputFilePath = cla_setup.getFileName()
    inputFile = open(inputFilePath, "rb")
    csvReader = csv.reader(inputFile)
    csvReader.next()
    csvReader.next()
    csvReader.next()
    
#    shifter = InferenceShifter()
#    output = nupic_output.NuPICPlotOutput(["Data"])
    
    c = 0
    prediction = None
    for row in csvReader:
        if(c%100==0):
            print "read lines=",c
        fieldVals = {}
        r = 0
        for fld in cla_setup.getFields():
            if fld["fieldType"]=="float":
                fieldVals[fld["fieldName"]]=float(row[r])
            elif fld["fieldType"]=="datetime":
                fieldVals[fld["fieldName"]]=datetime.datetime.strptime(row[r], cla_setup.getDateFormat())
            elif fld["fieldType"]=="string":
                fieldVals[fld["fieldName"]]=row[r]
            else:
                raise ValueError("This type of value needs to be added for support: "+row[r])
            r = r+1
        
        result = model.run(fieldVals)
        
#        result = shifter.shift(result)
        
        prediction = result.inferences[cla_setup.getInferenceType()]
#        output.write([timestamp], [cost], [prediction])
        c = c+1
        print prediction
        
    inputFile.close()
#    output.close()
    
def runSrvCenterTest():
    model = createModel()
    runModel(model)
    
if __name__ == '__main__':
    runSrvCenterTest()