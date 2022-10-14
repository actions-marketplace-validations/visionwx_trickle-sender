import os
import uuid

# Get para from env para
def getEnvPara(parameterName, default=None, 
    raiseExceptionIfNone=True):
    parameterValue = os.environ.get(parameterName, default)
    if parameterValue is None and raiseExceptionIfNone:
        raise Exception(parameterName + " not defined")
    return parameterValue

# uuid
def generateUUID():
    return str(uuid.uuid1())