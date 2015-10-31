# Created with Visual Studios Express 2013
# Python Version: 3.4.3150.1013
# Creator: Von Bailey
# Program Name: ProgResume
# Purpose: Performs all selenium functions for ProgResume

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time
import Utility
import LogFile

class sel_Interaction():   
    def doSearch(b,u,sc,se,sen,theLogFile,theDir): #Brower, URL, Search Criteria, Search Engine, Search Engine ID
        try:
            bName=[] # List of Browser names
            bName=Utility.ProgData.browsers()
            theName=bName[int(b)]
            currentURL = ""
            sfName=Utility.ProgData.searchField(int(sen))
            # Opening Browser
            if(b=="0"):
                driver=webdriver.Ie()
            elif(b=="1"):
                driver=webdriver.Chrome()
            else:
                driver=webdriver.Firefox()
            # Going to Search Engine,  Maximizing window, submitting search criteria
            driver.get(u)
            driver.maximize_window()
            # Verifying reached correct search engine
            if(driver.title==se):
                print(Utility.GenericSyntax.Success(driver.title,0))
                LogFile.loggingData.writeLog(theLogFile,Utility.GenericSyntax.Success(driver.title,0))
            else:
                e=Utility.ErrorSyntax.setValidateSearchEngineError(driver.title,se)
                print(e)
                LogFile.loggingData.writeLog(theLogFile,Utility.GenericSyntax.e,)
            theElement = driver.find_element(By.NAME, sfName)  # Finding the search filed
            theElement.send_keys(sc+Keys.ENTER) # Entering the search criteria
            LogFile.loggingData.writeLog(theLogFile,Utility.GenericSyntax.Success(sc,3))
            time.sleep(2)
            driver.get_screenshot_as_file(theDir+"\\SearchResults_"+sc+".png")
            currentURL=driver.current_url # Getting the URL of the results of the search
            driver.close()
            sel_Interaction.countAspects(currentURL,0,sc,3,theLogFile,theDir)
            sel_Interaction.countAspects(currentURL,1,sc,4,theLogFile,theDir)
            return 
        except:
            e=Utility.ErrorSyntax.setBrowserError(b,theName)
            LogFile.loggingData.writeLog(theLogFile,Utility.GenericSyntax.e)

    def countAspects(url,tp,sc,x,theLogFile,theDir):
        try:
            # Send url via HTTP and get the HTML for the page.
            LogFile.loggingData.writeLog(theLogFile,Utility.GenericSyntax.logTitles(x))
            pgData=str(Utility.getHTTP.retrievePageData(url))
            if(tp==0):
                # Check the HTML for references to the following:  imageFiles()
                img=0
                i=[]
                i=Utility.ProgData.imageFiles()
                while(img<4):
                    cnt=pgData.count(i[img])
                    LogFile.loggingData.writeLog(theLogFile,i[img] + Utility.GenericSyntax.images() + str(cnt))
                    img=img+1
            else:
                cnt=pgData.count(sc)
                LogFile.loggingData.writeLog(theLogFile,Utility.GenericSyntax.searchCriteria() + sc + " = "+str(cnt))
                if(cnt<1):
                    LogFile.loggingData.writeLog(theLogFile,Utility.ErrorSyntax.missingSC(sc))
        except:
            e=Utility.ErrorSyntax.countImages(url)
            LogFile.loggingData.writeLog(theLogFile,Utility.ErrorSyntax.countAspectsError(url))
