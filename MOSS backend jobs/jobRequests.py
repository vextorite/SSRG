import os # used to exceute commands in terminal
import datetime 
import random

class jobRequests:

    #constructor of the jobrequests object
    #jobID is to be recieved from Django Database
    #directoryFormat boolean value received from frontend UI
    #basefile filepath received from frontend UI (currently filepath will become name once file structure of archives is explored)
    def __init__(self, jobId, language, directoryFormat, baseFile ):
        self.jobId = jobId
        self.userId = self.generateUserID()
        self.language = language
        self.directoryFormat = directoryFormat
        self.baseFile = baseFile

    #Constructing the shell command needed to contact the moss server
    # TODO: implement as a switch statement    
    def constructMossShellCommand(self):
        if(self.directoryFormat==True) and (len(self.baseFile)>0):
            osCommand = f"perl mossnet.pl -l {self.language} -d -b {self.baseFile}  casper/vectormath.py ghost/vectormath.py >> myMossRun.txt"
        if(self.directoryFormat==True) and (len(self.baseFile)==0):
            osCommand = f"perl mossnet.pl -l {self.language} -d casper/vectormath.py ghost/vectormath.py >> myMossRun.txt"
        if(self.directoryFormat==False) and (len(self.baseFile)==0):
            osCommand = f"perl mossnet.pl -l {self.language} casper/vectormath.py ghost/vectormath.py >> myMossRun.txt"
        return osCommand

    #Method generates a userId as per groups specifications
    def generateUserID(self):
        subTime = datetime.datetime.now().time()
        randomPrependInt = random.randrange(100,999)
        currentJobPrimaryKey = f"{self.jobId}_{subTime}_{randomPrependInt}"
        return currentJobPrimaryKey
    
    #Executes shell command
    #TODO: handle the various moss output such as server offline, Implement Email Notifications
    #Currently assumes server online and working
    def submitJob(self):
        #email job start notification goes here
        os.system(self.constructMossShellCommand())
        print("Report located in the myMossRun.txt ready for scraping")
        #email job end notification goes here
    
    #summary just for testing purposes
    def summaryDetails(self):
        print(f"The details received as params are: {self.jobId}, {self.language}, the bool status of directory structure {self.directoryFormat}, the template code path {self.baseFile}.\nThe following userJobId was generated {self.userId}")

    #TODO: scrape moss piped textfile for url
    def retrieveURL(self):
        print("hello world!")




#static for now TODO: pre process vula archives allowing for full job requests
job = jobRequests("SSRG_team", "python", True, "base/vectormath.py")
job.summaryDetails()
job.submitJob()


#Command line
#perl mossnet.pl -l python -d -b base/vectormath.py casper/vectormath.py ghost/vectormath.py >> myMossRun.txt


