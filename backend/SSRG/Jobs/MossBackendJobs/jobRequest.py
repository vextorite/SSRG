import os
import sys
import glob
from mailNotificationSender import sendMail

#my issue is that if the text file is only a line it gets stuck

class jobRequest:
    count = 0
    emailSent = False
    jobSuccess = False

    def __init__(self, courseID, submissionLanguage, directoryFormat, baseFile, userEmail, toggleEmail):
        self.courseID = courseID
        self.submissionLanguage = submissionLanguage
        self.directoryFormat = directoryFormat
        self.baseFile = baseFile
        self.userEmail = userEmail
        self.toggleEmail = toggleEmail
    
    def constructMossShellCommand(self):
        print('unzipping')
        os.system("python3 /home/Vextorite/Documents/Capstone/ssrg-ndxsas021-hlnsan005-rmrsuv002/backend/SSRG/Jobs/MossBackendJobs/folderizer.py > folder_out.txt")
        print("unzipping done")
        subPathList = " ".join(glob.glob(f"jobOutput/jobOutput/*.{self.submissionLanguage}"))
        if(self.directoryFormat==True) and (len(self.baseFile)>1):
            osCommand = f"perl mossnet.pl -l {self.submissionLanguage} -d -b {self.baseFile} {subPathList} > myMossRun.txt"
        if(self.directoryFormat==True) and (len(self.baseFile)==0):
            osCommand = f"perl mossnet.pl -l {self.submissionLanguage} -d {subPathList} > myMossRun.txt"
        if(self.directoryFormat==False) and (len(self.baseFile)==0):
            osCommand = f"perl mossnet.pl -l {self.submissionLanguage} {subPathList} > myMossRun.txt"
        return osCommand
    
    def jobSender(self):
        #email
        #code to send off a job
        if self.toggleEmail == True and self.emailSent == False:
            print('we will send you mail for this job')
            sendMail(self.userEmail, False, "")
            self.emailSent = True
        ##important
        os.system(self.constructMossShellCommand())
        #code to check for success
        self.persistenceCheck('myMossRun.txt')
       

       
    def persistenceCheck(self,fileName):
        #self.count=self.count+1
        #print(self.count)
        #if ('http://moss.stanford.edu/results/' in self.retrieveUrl(fileName)) or self.count==7 :
        if ('http://moss.stanford.edu/results/' in self.retrieveUrl(fileName)):
            print('results are present')
            if(self.toggleEmail == True):
                print('email sent with reports')
                sendMail(self.userEmail, True, "/Users/suvanth/Subjects/Midway meeting work/MossBackendJobs/Exports/SSRG_0_test.pdf")
        else:
            print('lastline wasnt a url we will resend')
            self.jobSender()

    
    def retrieveUrl(self, mossFileName):
        with open(mossFileName, "rb") as file:
            file.seek(-2, os.SEEK_END)
            
            while file.read(1) != b'\n':
                file.seek(-2, os.SEEK_CUR) 
               
            return file.readline().decode()



#job = jobRequest("CSC3002F", "c", False, "", "rmrsuv002@myuct.ac.za", True)
job = jobRequest("CSC3002F", "java", False, "", "rsuvanth@gmail.com", True)
job.jobSender()
print("go to your text file")

print(str(sys.argv[1]))#user
print(str(sys.argv[2]))#lang
print(eval(sys.argv[3]))#bool dir
print(str(sys.argv[4]))#Bfile
print(str(sys.argv[5]))#email
print(eval(sys.argv[6]))#bool toggle


