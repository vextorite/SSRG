import os,sys
import glob
from mailNotificationSender import sendMail
from heatmap import completeReport

#my issue is that if the text file is only a line it gets stuck

class jobRequest:
    emailSent = False
    jobSuccess = False

#add job id param
    def __init__(self, courseID, jobID,submissionLanguage, directoryFormat, baseFile, userEmail, toggleEmail, zipPath):
        self.courseID = courseID
        self.jobID = jobID
        self.submissionLanguage = submissionLanguage
        self.directoryFormat = directoryFormat
        self.baseFile = baseFile
        self.userEmail = userEmail
        self.toggleEmail = toggleEmail
        self.zipPath = zipPath
    
    def constructMossShellCommand(self):
        print('unzipping')
        os.system(f"python3 /home/Vextorite/Documents/SSRG/ssrg-ndxsas021-hlnsan005-rmrsuv002/backend/SSRG/Jobs/MossBackendJobs/folderizer.py '{self.zipPath}' > folder_out.txt")
        print("unzipping done")
        #change this glob
        #
        index = self.zipPath[self.zipPath.rfind('/'):]
        subPathList = " ".join(glob.glob(f"{self.zipPath}{index}/*.{self.submissionLanguage}"))
        if(self.directoryFormat==True) and (len(self.baseFile)>1):
            osCommand = f"perl /home/Vextorite/Documents/SSRG/ssrg-ndxsas021-hlnsan005-rmrsuv002/backend/SSRG/Jobs/MossBackendJobs/mossnet.pl -l {self.submissionLanguage} -d -b {self.baseFile} {subPathList} > myMossRun.txt"
        if(self.directoryFormat==True) and (len(self.baseFile)==0):
            osCommand = f"perl /home/Vextorite/Documents/SSRG/ssrg-ndxsas021-hlnsan005-rmrsuv002/backend/SSRG/Jobs/MossBackendJobs/mossnet.pl -l {self.submissionLanguage} -d {subPathList} > myMossRun.txt"
        if(self.directoryFormat==False) and (len(self.baseFile)==0):
            osCommand = f"perl /home/Vextorite/Documents/SSRG/ssrg-ndxsas021-hlnsan005-rmrsuv002/backend/SSRG/Jobs/MossBackendJobs/mossnet.pl -l {self.submissionLanguage} {subPathList} > myMossRun.txt"
        print(osCommand)
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
        #SANELE QUERY
        self.persistenceCheck('myMossRun.txt')
       

       
    def persistenceCheck(self,fileName):
        url = self.retrieveUrl(fileName)
        if ('http://moss.stanford.edu/results/' in url):
            print('results are present')
            #completeReport(self.courseID, url )
            completeReport(self.zipPath, self.courseID, self.jobID, url)
            print('report done')

            
            if(self.toggleEmail == True):
                print('email sent with reports')
                #NEED TO CHANGE
                sendMail(self.userEmail, True, f"{self.zipPath}/{self.jobID}_{self.courseID}_report.pdf")
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
#job = jobRequest("CSC3002F", "J123", "java", False, "", "rsuvanth@gmail.com", True, "/home/Vextorite/Documents/SSRG/ssrg-ndxsas021-hlnsan005-rmrsuv002/backend/SSRG/jobs/root")
job = jobRequest(str(sys.argv[1]), "Job", str(sys.argv[3]), eval(str(sys.argv[4])), str(sys.argv[5]), str(sys.argv[6]), eval(str(sys.argv[7])), str(sys.argv[8]))

job.jobSender()

# def __init__(self, courseID, jobID,submissionLanguage, directoryFormat, baseFile, userEmail, toggleEmail, zipPath):
#print(job.constructMossShellCommand())
#print("go to your text file")
#for arg in sys.argv:
#    print(arg)
# print(str(sys.argv[1]))#user
# print(str(sys.argv[2]))#lang
# print(eval(sys.argv[3]))#bool dir
# print(str(sys.argv[4]))#Bfile
# print(str(sys.argv[5]))#email
# print(eval(sys.argv[6]))#bool toggle


# python3 jobRequest.py "CSC3002F" "java" "False" "" "rmrsuv002@gmail.com" "False"
