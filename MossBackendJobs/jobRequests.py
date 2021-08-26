import os # used to exceute commands in terminal
import sys
import glob # aids in constructing submission concatenated file paths for MOSS shell command
import pdfkit # module to save webpage url as pdf - pip install
from mailNotificationSender import sendMail
from contextlib import contextmanager
from reportGenerator import generateReport

@contextmanager
def suppress_stdout(): # called to prevent console output
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout


class jobRequests:

    #submissionLanguage - used for the l MOSS flag
    #directoryFormat - used for the d MOSS flag
    #baseFile - used for the b MOSS flag
    def __init__(self, userID, submissionLanguage, directoryFormat, baseFile, userEmail):
        self.userID = userID
        self.userEmail = userEmail
        self.submissionLanguage = submissionLanguage
        self.directoryFormat = directoryFormat
        self.baseFile = baseFile

    #Constructing the shell command that is used to exceute the perl script
    def constructMossShellCommand(self):
        print("Unzipping Bulk Archive...")
        os.system("python3 folderizer.py > folderizerOut.txt") # preprocceing bulk vula archive with the use of folderizer.py
        print("Unzipping Complete")
        subPathList = " ".join(glob.glob(f"jobOutput/jobOutput/*.{self.submissionLanguage}")) # looking for code files in the jobOutput directory with the relevant extension

        if(self.directoryFormat==True) and (len(self.baseFile)>1):
            osCommand = f"perl mossnet.pl -l {self.submissionLanguage} -d -b {self.baseFile} {subPathList} > myMossRun.txt"
        if(self.directoryFormat==True) and (len(self.baseFile)==0):
            osCommand = f"perl mossnet.pl -l {self.submissionLanguage} -d {subPathList} > myMossRun.txt"
        if(self.directoryFormat==False) and (len(self.baseFile)==0):
            osCommand = f"perl mossnet.pl -l {self.submissionLanguage} {subPathList} > myMossRun.txt"
        return osCommand
    
    #executes the shell command
    def submitJob(self):
        sendMail(self.userEmail, False, "")
        os.system(self.constructMossShellCommand()) # executing the MOSS shell command
        print("find info in myMossRun.txt")
        self.retrieveUrl()
        print("Complete")
    
    #reads url from last line of perl script output stored in myMossRun.txt and exports report webpage to pdf
    def retrieveUrl(self):
        with open('myMossRun.txt') as f:
            for line in f:
                pass
            last_line = line
        with suppress_stdout():
            exportPath = f"Exports/{self.userID}_test.pdf"
            generateReport(last_line, exportPath)
            #pdfkit.from_url(last_line, exportPath)
        sendMail(self.userEmail, True, exportPath)
       

#SANELE IMPORTANT INFO HOW TO CREATE A JOB OBJ AND SEND IT OFF
job = jobRequests("SSRG_0", "java", False, "", "rmrsuv002@myuct.ac.za")
job.submitJob()