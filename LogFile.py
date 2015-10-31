# Created with Visual Studios Express 2013
# Python Version: 3.4.3150.1013
# Creator: Von Bailey
# Program Name: ProgResume
# Purpose: Performs all logging aspects of the program
import Utility
import time
import os


class loggingData():
    def createLog(theLogFile):
        cFile=open(theLogFile, 'w')
        cFile.write(Utility.ProgData.Header())
        print(Utility.ProgData.Header())
        cFile.close()

    def writeLog(theLogFile,theLogEntry):
        wFile=open(theLogFile, 'a')
        wFile.write("\n"+Utility.ProgData.logDateString()+":  "+theLogEntry)
        print("\n"+Utility.ProgData.logDateString()+":  "+theLogEntry)
        wFile.close()
        

    def dirName():
        hDirectory=os.path.dirname(os.path.realpath("WebInteraction.py"))
        theFileString=Utility.ProgData.dateString()
        theDir=hDirectory+"\Log_"+theFileString
        os.mkdir(theDir)
        return [theDir,theFileString]

    def fileName(theDir,theFileString):
        theLogFile = theDir+"\LogFile_"+theFileString+".log"
        return theLogFile



        