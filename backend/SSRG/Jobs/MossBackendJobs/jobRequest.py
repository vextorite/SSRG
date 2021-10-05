import os
import glob
from mailer import sendNotification
from heatmap import completeReport
from processor import saveCodeFiles

#path shit
#folderizer path
#mossnet.pl path
#REPLACES THESE WITH ARGS
folderizerRoot = '/Users/suvanth/Desktop/SSRG_SYS/Suvanth/JobID001' #args
folderizerOut ='/Users/suvanth/Desktop/SSRG_SYS/Suvanth/JobID001/Zip' #args



class jobRequest:
    '''
    The function of the jobRequest class is to unzip submission files, form the appropriate
    MOSS shell command, exceute it and receive output. The class handles the various states 
    of the MOSS server.
    '''
    emailSent = False


    def __init__(self, courseID, jobID,submissionLanguage, directoryFormat, baseFile, userEmail, toggleEmail, fRoot, fOut):
        '''
        Constructor of the Job Request that we submit to the MOSS server
        The job object takes 8 parameters namely:
        CourseID(course associated with user account)
        jobID(unique identifier of submitted job)
        submissionLanguage - Coding language utilised for code file submissions to MOSS
        directoryFormat - Format of the archive directory
        baseFile - Paths to boiler plate code provided to the students - Boolean
        userEmail - Email Address associated with the user account
        toggleEmail - User preference for emails
        fRoot - User job Folder path
        fOut - Folder containing unzipped files
        '''
        self.courseID = courseID
        self.jobID = jobID
        self.submissionLanguage = submissionLanguage
        self.directoryFormat = directoryFormat
        self.baseFile = baseFile
        self.userEmail = userEmail
        self.toggleEmail = toggleEmail
        self.fRoot = fRoot
        self.fOut= fOut


    def folderizerCall(self):
        '''
        The function executes the folderizer.py script with the specified arguments received from django webApp
        '''
        print('start unzip')
        os.system(f'python3 folderizer.py {folderizerRoot} {folderizerOut} > folderout.txt')
        print('end unzip')

    def constructMossShellCommand(self):
        '''
        Constructs Moss Shell command adhering to strict structure
        '''
        index = self.fOut[self.fOut.rfind('/'):]
        subPathList = " ".join(glob.glob(f"{self.fOut}{index}/*.{self.submissionLanguage}"))
        if(self.directoryFormat==True) and (self.baseFile==True):
            basePathList = " -b ".join(glob.glob(f"{self.fRoot}/Basefile/*.{self.submissionLanguage}"))
            osCommand = f"perl mossnet.pl -l {self.submissionLanguage} -d -b {basePathList} {subPathList} > myMossRun_{self.jobID}.txt"
        if(self.directoryFormat==False) and (self.baseFile==True):
            basePathList = " -b ".join(glob.glob(f"{self.fRoot}/Basefile/*.{self.submissionLanguage}"))
            osCommand = f"perl mossnet.pl -l {self.submissionLanguage} -b {basePathList} {subPathList} > myMossRun_{self.jobID}.txt"
        if(self.directoryFormat==True) and (self.baseFile==False):
            osCommand = f"perl mossnet.pl -l {self.submissionLanguage} -d {subPathList} > myMossRun_{self.jobID}.txt"
        if(self.directoryFormat==False) and (self.baseFile==False):
            osCommand = f"perl mossnet.pl -l {self.submissionLanguage} {subPathList} > myMossRun_{self.jobID}.txt"

        print(osCommand)
        return osCommand
    
    def jobSender(self):
        '''
        Driver function behind the jobrequests.py script
        This method executes the MOSS shell command and retrieves output in an ordely manner
        Emails are sent out based on the user email toggle setting
        This method was built taking into account the stability of MOSS servers
        '''
        if self.toggleEmail == True and self.emailSent == False:
            print('we will send you mail for this job')
            sendNotification(self.userEmail, self.jobID, 'pending', "")
            self.emailSent = True
        os.system(self.constructMossShellCommand())
        print('executed')
        self.persistenceCheck(f'myMossRun_{self.jobID}.txt')
        print('done')

    def persistenceCheck(self,fileName):
        '''
        The persistence check method retrieves the last line from the MOSS output that was piped to a textfile
        The method deals with the state of the MOSS servers, jobs will be resubmitted automatically if there 
        is a unfavorable state
        The parameter of the method:
        filename - Name of the MOSS text output file
        '''
        url = self.retrieveUrl(fileName).strip()
        if ('http://moss.stanford.edu/results/' in url):
            print('results are present')
            saveCodeFiles(url, self.fRoot, self.jobID)
            completeReport(self.fRoot, self.courseID, self.jobID, url)
            print('report done')

            if(self.toggleEmail == True):
                sendNotification(self.userEmail,self.jobID, 'done', f'{self.fRoot}/JobReport.pdf')
                print('email sent with reports')
        else:
            print('erroneous state state resending job')
            self.jobSender()
    
    def retrieveUrl(self, mossFileName):
        '''
        Function retrieves the last line of the MOSS output textfile.
        The function is optimised for large files so as to not add to exceution time, this was achieved through the seek command
        '''
        with open(mossFileName, "rb") as file:
            file.seek(-2, os.SEEK_END)
            
            while file.read(1) != b'\n':
                file.seek(-2, os.SEEK_CUR) 
               
            return file.readline().decode()
        

job = jobRequest('CSC3002F','j100','java',False, False,'rmrsuv002@myuct.ac.za', True, folderizerRoot, folderizerOut)
job.folderizerCall()
job.jobSender()

#need args