'''
Created on Aug 25, 2015

@author: seth
'''
from config.swarm_description import SWARM_DESCRIPTION as setup
from config import swarm_setup
import os

DATE_FORMAT = "%m/%d/%Y %H:%M"
INFERENCE_TYPE="multiStepBestPredictions"










def getFileName():
    return os.path.join(os.getcwd(),"..", "swarming/"+setup["streamDef"]["streams"][0]["source"].split("/")[-1])

def getPredictedFiled():
    return setup['inferenceArgs']['predictedField']

def getFields():
    return setup['includedFields']

def getDateFormat():
    return DATE_FORMAT

def getInferenceType():
    return INFERENCE_TYPE
    
