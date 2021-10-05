from processor import scrapeUrl
from typing_extensions import final
import numpy
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from seaborn.distributions import histplot;
from reportGenerator import generateReport


def populateDataList(urlLink):
    '''
    Function scrapes the MOSS url and puts it into an appropriate form so that it 
    can be utilised in a Pandas Dataframe.
    Parameters
    urlLink - MOSS url returned from script execution
    '''
    dataList=[]
    histList=[]
    finalList=[]
    rawList = scrapeUrl(urlLink)
    rawList.pop(0)
    for i in rawList:
        currentRecord=[]
        student1 = i[0]
        student2 = i[1]
        student1Index = student1[student1.rfind('/')+1:student1.rfind('.')]
        currentRecord.append(student1Index.strip())
        student1Percent = student1[student1.find('(')+1:student1.find(')')-1]
        currentRecord.append(student1Percent.strip())
        student2Index = student2[student2.rfind('/')+1:student2.find('.')]
        currentRecord.append(student2Index.strip())
        student2Percent = student2[student2.find('(')+1:student2.find(')')-1]
        currentRecord.append(student2Percent.strip())
        currentRecord.append(i[2])
        dataList.append(currentRecord)
        histList.append(int(i[2]))
    finalList.append(dataList)
    finalList.append(histList)
    return finalList

def studentList(exportPathHeat, exportPathHist,url):
    '''
    Function that populates a pandas dataframe in order to generate Heatmaps and Histograms from the MOSS output
    Parameters
    exportPathHeat - Path of generated heatmap png
    exportPathHist - Path of generated histogram png
    url - MOSS url returned from script execution
    '''
    total=0
    studentList ={}
    studentList = set()
    myFilteredList =[]
    mylst = populateDataList(url)
    for i in mylst[0]:
        total=total+int(i[4])
        if int(i[4])>=50:
            myFilteredList.append(i)
            studentList.add(i[0])
            studentList.add(i[2])
    
    init_arr=numpy.zeros((len(studentList),len(studentList)))
    df3 = pd.DataFrame(init_arr, index= studentList, columns=studentList)
    for i in myFilteredList:
        df3[i[0]][i[2]] = i[1]
        df3[i[2]][i[0]] = i[3]
    sns.heatmap(df3, cmap='rocket_r', annot=True, fmt='.0f',  ).set_title("MOSS High Average Lines Matched Heatmap")
    plt.title='Moss'
    plt.tight_layout()
    plt.savefig(exportPathHeat)
    plt.close()

    histlist = mylst[1]
    histlist.sort()
    sns.histplot(histlist, color= 'Blue', bins=[20,40,60,80,100,120,180,190] )
    plt.title='Distribution of Average Matched Lines'
    plt.xlabel("Average lines matched categories", fontsize =12)
    plt.ylabel("Observations", fontsize =12)
    plt.tight_layout()
    plt.savefig(exportPathHist)



def completeReport(fRoot, courseID,jobId,url):
    '''
    Utility driver function called to generate Graphs and Report
    fRoot - Save path
    courseID - courseID associated with user job appended on to files
    jobID -  Unique identifier of submitted job appended on to files
    url - MOSS url returned from script execution
    '''
    studentList(f"{fRoot}/{jobId}_{courseID}_heatmap.png", f"{fRoot}/{jobId}_{courseID}_histogram.png", url)
    generateReport(url, f"{fRoot}/JobReport.pdf", f"{fRoot}/{jobId}_{courseID}_heatmap.png", f"{fRoot}/{jobId}_{courseID}_histogram.png")
