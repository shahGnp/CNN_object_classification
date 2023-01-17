import os 
import shutil
import random

def getDatasetPath():
    dataPath=input("Enter Dataset Path: ")
    return dataPath

def getClassLabels(dataPath):
    return os.listdir(dataPath)

def createTrainTestFolders():
    try:
        trainPath=os.path.join(dataPath,'Train')
        testPath=os.path.join(dataPath,'Test')
        os.mkdir(trainPath)
        os.mkdir(testPath)
        print('Success Train Test folders created')
    except Exception as e:
        print('Error: ',e)
        pass

def createLabelFolders(labels,dataPath):
    try:
        for label in labels:
            os.mkdir(os.path.join(dataPath,'Train',label))
            os.mkdir(os.path.join(dataPath,'Test',label))
            print('Success Label folders created')
        pass
    except Exception as e:
        print('Error: ',e)

def getTrainTestPercentage():
    Train=input('Enter Traning ratio: ')
    return float(Train)

def transferFiles(trainRatio,labels,dataPath):
    for label in labels:
        if label=='Test' or label=='Train':
            pass
        else:
            files=os.listdir(os.path.join(dataPath,label))
            TrainSamples=random.sample(files,round(len(files)*trainRatio))
            TestSamples=list(set(files)-set(TrainSamples))
            # print('No of Train Samples: ',len(TrainSamples), ' in lable: ',label)
            # print('No of Test Samples: ',len(TestSamples), ' in lable: ',label)

            for TrainSample in TrainSamples:
                currPath=os.path.join(dataPath,label,TrainSample)
                newPath=os.path.join(dataPath,'Train',label,TrainSample)
                try:
                    shutil.move(currPath,newPath)
                    # print('Moving Training Files for lable: ',label)
                except Exception as e:
                    print('***Error***')
                    print('Cannot move File From: ',currPath, ' to ',newPath)
                    print('Error Message: ',e)
            
            for TestSample in TestSamples:
                currPath=os.path.join(dataPath,label,TestSample)
                newPath=os.path.join(dataPath,'Test',label,TestSample)
                try:
                    shutil.move(currPath,newPath)
                    # print('Moving Testing Files for lable: ',label)
                except Exception as e:
                    print('***Error***')
                    print('Cannot move File From: ',currPath, ' to ',newPath)
                    print('Error Message: ',e)
    print('All data Successfully moved')

def purgeDatasetPrevLabels(dataPath,labels):
    print('Removing previous folders')
    for label in labels:
        if label=='Test' or label=='Train':
            pass
        else:
            os.rmdir(os.path.join(dataPath,label))


if __name__=="__main__":
    dataPath = getDatasetPath()
    labels = getClassLabels(dataPath)
    createTrainTestFolders()
    createLabelFolders(labels,dataPath)
    Train=getTrainTestPercentage()
    transferFiles(Train, labels,dataPath)
    purgeDatasetPrevLabels(dataPath,labels)