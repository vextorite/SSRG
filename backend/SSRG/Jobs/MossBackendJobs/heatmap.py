from processor import scrapeUrl
from typing_extensions import final
import numpy
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from seaborn.distributions import histplot;
from reportGenerator import generateReport


def populateDataList(urlLink):
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
        print(f'{i[0]}  and {i[1]} and {i[2]} and {i[3]}')
        df3[i[0]][i[2]] = i[1]
        df3[i[2]][i[0]] = i[3]
    #print(df3)
    sns.heatmap(df3, cmap='rocket_r', annot=True, fmt='.0f',  ).set_title("MOSS High Average Lines Matched Heatmap")
    plt.title='Moss'
    plt.tight_layout()
    plt.savefig(exportPathHeat)
    plt.close()
    print('heat done')

    histlist = mylst[1]
    histlist.sort()
    for i in histlist:
        print(i)
    sns.histplot(histlist, color= 'Blue', bins=[20,40,60,80,100,120,180,190] )
    plt.title='Distribution of Average Matched Lines'
    plt.xlabel("Average lines matched categories", fontsize =12)
    plt.ylabel("Observations", fontsize =12)
    plt.tight_layout()
    plt.savefig(exportPathHist)
    print('hist done')



def completeReport(zipPath, courseID,jobId,url):
    studentList(f"{zipPath}/{jobId}_{courseID}_heatmap.png", f"{zipPath}/{jobId}_{courseID}_histogram.png", url)
    #studentList(f'/Users/suvanth/Desktop/test/Suvanth/{jobId}heatmap.png', f'/Users/suvanth/Desktop/test/Suvanth/{jobId}histogram.png', url )
    print('check test for your pics')
    generateReport(url, f"{zipPath}/{jobId}_{courseID}_report.pdf", f"{zipPath}/{jobId}_{courseID}_heatmap.png", f"{zipPath}/{jobId}_{courseID}_histogram.png")
    print('check test for your pdfs')