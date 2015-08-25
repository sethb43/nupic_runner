'''
Created on Aug 15, 2015

@author: seth
'''
import pprint
import os
from nupic.swarming import permutations_runner
from config.swarm_description import SWARM_DESCRIPTION
from config import swarm_setup

def saveModelParams(modelParams):
    outDir = os.path.join(os.getcwd(),"..", "model_params")
    if not os.path.isdir(outDir):
        os.mkdir(outDir)
    outPath = os.path.join(outDir, "cla_model_params.py")
    pp = pprint.PrettyPrinter(indent=2)
    with open(outPath, "wb") as outFile:
        modelPString = pp.pformat(modelParams)
        outFile.write("MODEL_PARAMS = \\\n%s" % modelPString)
    return outPath
    
def swarm():
    swarmWorkDir = os.path.abspath("swarm_results")
    if not os.path.exists(swarmWorkDir):
        os.mkdir(swarmWorkDir)
        
    modelParams = permutations_runner.runWithConfig(
                  SWARM_DESCRIPTION, 
                  {"maxWorkers": swarm_setup.MAX_WORKERS, "overwrite": True}, 
                  outputLabel="cla_model", 
                  outDir=swarmWorkDir, 
                  permWorkDir=swarmWorkDir, 
                  verbosity=0)
    saveModelParams(modelParams)


if __name__=="__main__":
    swarm()