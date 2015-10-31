# Created with Visual Studios Express 2013
# Python Version: 3.4.3150.1013
# Creator: Von Bailey
# Program Name: ProgResume
# This module is for generic classes & functions and all data
import LogFile
import urllib.request
import os
import time

class ProgData:
    # Version of the App
    def versioning():
        return "3.0"  # Optimized logging process and added saving an image of the search results in the log folder.

    def dateString():
        return time.strftime("%H%M%S%m%d%y")
         
    def logDateString():
        return time.strftime("%H:%M:%S-%m/%d/%y")

    def Header():
            vr=ProgData.versioning()
            return" Created with Visual Studios Express 2013\n Python Version: 3.4.3\n Creator: Von Bailey\n Program Name: ProgResume\n Program Log\n Version: "+vr+"\n"

    def webSites():
        # Web URLs
        i=["http://www.google.com","http://www.bing.com","http://www.yahoo.com"];
        return i;

    def seacrhCriteria():
        # Search Criteria
        i=input("****Please Enter Your Search Criteria****\nEnter 'QUIT' in upper case to quit the program\n>>> ");
        return i;

    def browsers():
        # Browsers
        i=["Internet Explorer","Chrome","Firefox"];
        return i;
    
    def imageFiles():
        # Image file types
        i=[".jpg",".bmp",".gif",".png"];
        return i
    
    def seMenuOpt(i):
        # Menu Options 
        try:
            if(i==0):
                mItem= input("***Pick a Search Engine***\n0= Google\n1= Bing\n2= Yahoo \nQ= Quit Program\n>>> ");
            else:
                mItem= input("***Pick a Browser***\n0= IE\n1= Chrome\n2= Firefox\nQ= Quit Program\n>>> ");
            return mItem
        except:
            print(ErrorSyntax.setMenuOptionsError())
            LogFile.loggingData.writeLog(theLogFile,ErrorSyntax.setMenuOptionsError())

    def searchField(sf):
        # Attempting to identify the search field name for the correct search engine.
        try:
            if(sf==0 or sf==1):
                sfName="q" # Google and Bing
            else:
                sfName="p" # Yahoo
            return sfName
        except:
            print (ErrorSyntax.searchFieldError())
            LogFile.loggingData.writeLog(theLogFile,ErrorSyntax.searchFieldError())

    def searchEngines(se):
        ses = ["Google","Bing","Yahoo"]
        i=ses[se]
        return i

class Menu():
    def menuItems(x):
        try:
            i=ProgData.seMenuOpt(x)
            return i
        except:
            print (ErrorSyntax.menuItems())
            LogFile.loggingData.writeLog(theLogFile,ErrorSyntax.menuItems())

    def validate_MenuItem(x):
        try:
            c=0
            validate = False
            mChoices=['0','1','2'] # Only valid options
            while c < 3:
                if(x==mChoices[c]):
                   validate=True
                   c=4  # Found it.  
                else:
                    c=c+1 # Still looking
            if(validate==True):
                return x  
            else:
                return False
        except:
            print (ErrorSyntax.menuItems())
            LogFile.loggingData.writeLog(theLogFile,ErrorSyntax.validate_MenuItem(x))

class GenericSyntax():
    def images():
        return " images:"

    def searchCriteria():
        return " Instances of the search criteria: "

    def SynRnProg(URL,Browser,SC):
        return " Browser URL: "+ URL+" | Selected Browser:  "+Browser+" | Search Criteria:  "+ SC

    def Success(txt,pk):
        if(pk==0):
            return " Successfully reached: "+txt
        elif(pk==1):
            return " Succesfully created: "+txt
        elif(pk==2):
            return " Succesfully retrieved: "+txt
        else:
            return " Succesfully entered: "+txt

    def quitMsg():
        return " Exiting the program"

    def quitting():
        return "QUIT"

    def quit():
        return "Q"

    def false():
        return "false"

    def true():
        return "true"

    def HTTP():
        return "http"

    def logTitles(x):
        i=[]
        i = [" *CREATING MENU*"," *PICKING SEARCH ENGINE*"," *STARTING APPLICATION*", " *COUNTING IMAGES*","*COUNTING MATCHING TEXT*"];
        return i[x]

class TheURL():
    def get_URL(i):
        if(i>2 or i< 0): return str(i) # takes care of bad selection
        urlsList=[]
        urlsList=ProgData.webSites()
        return urlsList[i]

class Browsers():
    def get_brw(i):
        if(i>2 or i< 0): return str(i) # takes care of bad selection
        bwr=[]
        bwr=ProgData.browsers()
        return bwr[i]    

class getHTTP():
    # Retrieve a single page and report the url and contents
    def retrievePageData(theURL):
        try:
            pageText = urllib.request.urlopen(theURL, timeout=50000)
            return pageText.readall()
        except:
            e=Utility.ErrorSyntax.setBrowserError(b,theName)
            LogFile.loggingData.writeLog(theLogFile,Utility.GenericSyntax.e)

class ErrorSyntax():
    def missingSC(sc):
        # Error when nothing on the search results page matches the search criteria
        return "WARNING:  Could not find an instance of the search criteria '"+sc+"' in the search results."

    def validate_MenuItem(x):
        # Error validating menu choice
        return "ERROR: validate_MenuItem("+x+")"

    def setValidateSearchEngineError(title,se):
        return "ERROR: setValidateSearchEngineError("+title+","+se+")"

    def setMenuOptionsError():
        # Error if there is an issue setting the menu options
        return "ERROR:  setMenuOptionsError()"

    def searchFieldError():
        # Error if program fails to identify the search filed name
        return  "ERROR:  searchFieldError(Failed to identify the search field name)"

    def menuItems():
        # Error if program fails to create one of the menus
        return "ERROR:  doMenu(Failed to create the menu)"

    def menuError():
        # Error if the menu has a problem colleting data
        return "ERROR: Failed Main_MenuOptions()"

    def mainError():
        # Error if the menu accepts data outside it's parameters
        return ["ERROR: Menu Entries incorrect.  Please verify entries and try again. \nNo Entry should be above 2 or below 0\n  URL Entry: ","\n  Search Criteria Entry: ","\n  Browser Entry: "];

    def mainError():
        # Error if there is an issue after all variables have been set and it's not a menu issue.
        return "ERROR: Failed Main()"
        
    def dataColletion():
        # Error collecting data to run the application
        return "ERROR: Failed Main_DataColletion()"

    def setBrowserError(b,theName):
        # Error gathering information regarding setting up the browser.
        return "ERROR: Failed setBrowser("+b+","+theName+")"

    def openBrowserError(theName):
        # # Error opening the browser.
        return "ERROR: Failed openBrowser(Browser"+theName+")"

    def countAspectsError(url):
        # Error counting images in the HTTP request
        return "ERROR:  Failed attempting to find images in countAspects("+url+")"