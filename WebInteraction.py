# Created with Visual Studios Express 2013
# Python Version: 3.4.3150.1013
# Creator: Von Bailey
# Program Name: ProgResume
# Purpose: Interact with various web browsers and search engines 
#              to display ability to creating a program that can interact
#              with websites on the internet.

import Utility
import selBin
import os
import LogFile

class startMe():
    def doMenu(ms,theLogFile,theDir):
        try:
            # Taking Menu Options
            if(ms==0):
                y=Utility.Menu.menuItems(0)
            elif(ms==1):
                y=Utility.Menu.menuItems(1)
            x=Utility.Menu.validate_MenuItem(y)
            if(y.upper()==Utility.GenericSyntax.quit() or x==False):
                LogFile.loggingData.writeLog(theLogFile,Utility.ErrorSyntax.validate_MenuItem(y))
                os._exit(0)
            LogFile.loggingData.writeLog(theLogFile,Utility.GenericSyntax.Success("Menu Item: ",1)+str(ms))
            return y
        except:
            print(Utility.ErrorSyntax.menuError(),theDir)
            LogFile.loggingData.writeLog(theLogFile,Utility.ErrorSyntax.menuError())
            os._exit(0)

    def doDataCollection(u,theLogFile,theDir):
        try:
            # Verifying data collection
            gotSC=str(Utility.ProgData.seacrhCriteria()) # Getting the search criteria
            LogFile.loggingData.writeLog(theLogFile,Utility.GenericSyntax.Success(" Search Criteria: "+gotSC,2))
            if(gotSC.upper()==Utility.GenericSyntax.quitting()):
                LogFile.loggingData.writeLog(theLogFile,Utility.ErrorSyntax.dataColletion(gotSC))
                os._exit(0)
            gotURL= Utility.TheURL.get_URL(int(u)) # Getting the URL
            LogFile.loggingData.writeLog(theLogFile,Utility.GenericSyntax.Success(" URL: "+gotURL,2))
            return [gotURL, gotSC]
        except:
            print(Utility.ErrorSyntax.dataColletion())
            LogFile.loggingData.writeLog(theLogFile,Utility.ErrorSyntax.dataColletion())
            os._exit(0)

    def Main(URL,SC,brow,u,theLogFile,theDir):
        try:
            # Running program
            if(len(URL) <3 or len(SC) < 3 or len(brow) < 3): 
                eList=[]
                eList=Utility.ErrorSyntax.mainError()
                print(eList[0]+URL+eList[1]+SC+eList[2]+brow)
                LogFile.loggingData.writeLog(theLogFile,eList[0]+URL+eList[1]+SC+eList[2]+brow)
                return Utility.GenericSyntax.false()
            else:
                goodData=Utility.GenericSyntax.SynRnProg(URL,brow,SC)
                print(goodData)
                LogFile.loggingData.writeLog(theLogFile,goodData)
            # Opening Browser and processing search results
                selBin.sel_Interaction.doSearch(b,URL,SC,brow,u,theLogFile,theDir)
        except:
            e=Utility.ErrorSyntax.mainError()
            print(e)
            LogFile.loggingData.writeLog(theLogFile,e)

# Creating log file and directory
dirComp=[]
dirComp=LogFile.loggingData.dirName()
theDir=dirComp[0]
theLogFile=LogFile.loggingData.fileName(theDir, dirComp[1])
LogFile.loggingData.createLog(theLogFile)

#Adding header to log
LogFile.loggingData.writeLog(theLogFile,Utility.GenericSyntax.logTitles(0))

mi=0 # Getting the values to define the Search Engine and browser.
while (mi<2):  
    m1=startMe.doMenu(mi,theLogFile,theDir)
    if(mi==0):
        u=m1 # assigning Search Engine
    else:
        b=m1 # assigning browser
    mi=mi+1

LogFile.loggingData.writeLog(theLogFile,Utility.GenericSyntax.logTitles(1))
se=Utility.ProgData.searchEngines(int(u))  # Assigning search engine
dc=[];dc=startMe.doDataCollection(u,theLogFile,theDir) # getting theURL and the Search Criteria
###########################
#RUNNING THE APPLICATION
LogFile.loggingData.writeLog(theLogFile,Utility.GenericSyntax.logTitles(2))
startMe.Main(dc[0],dc[1],se,u,theLogFile,theDir)

# Exiting program
print(Utility.GenericSyntax.quitMsg())
LogFile.loggingData.writeLog(theLogFile,Utility.GenericSyntax.quitMsg(),)

