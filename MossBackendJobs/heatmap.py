from datetime import date
import glob
import numpy
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from seaborn.distributions import histplot;
from bs4 import BeautifulSoup
import urllib.request
from itertools import dropwhile




def scrapeUrl(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    for script in soup(["script", "style"]):
        script.decompose()
    strips = list(soup.stripped_strings)

    element = 'Lines Matched'
    mycleanlst=list(dropwhile(lambda x: x != element, strips))
    mycleanlst.pop(0)

    out=['File 1', 'File 2', 'Lines Matched']
    finalJbList=[]
    finalJbList.append(out)
    out=[]
  
    for i in range(len(mycleanlst)):
        if mycleanlst[i].isdigit():
            out.append(mycleanlst[i])
            finalJbList.append(out)
            out=[]
        else:
            out.append(mycleanlst[i])
    return finalJbList

def initDataframe():
    subPathList = glob.glob(f"jobOutput/jobOutput/*.java")

    studentsList=[]
    for i in range(len(subPathList)):
        firstIndex = subPathList[i].rfind('/')+1
        studentsList.append(subPathList[i][firstIndex:].strip())
    studentsList.sort()
    init_arr=numpy.zeros((len(studentsList),len(studentsList)))
    randi_arr = numpy.random.randint(0, 101, (len(studentsList),len(studentsList)))
    df3 = pd.DataFrame(init_arr, index= studentsList, columns=studentsList)
    print(df3)
    data = populateDataList()
    for i in data:
        df3[i[0]][i[2]]=i[1]
        df3[i[2]][i[0]]=i[3]
    print(df3)

    #now to scrape the url
    sns.heatmap(df3, cmap='gist_heat', annot=True, linewidths=1, fmt='.0f',  ).set_title("MOSS Pairwise Similarity Heatmap")
    plt.title='Moss'
    #plt.show()
    plt.autoscale= True
    plt.savefig('heatmap.png')
    

def populateDataList():
    dataList=[]
    rawList = scrapeUrl('http://moss.stanford.edu/results/0/35346207182')
    rawList.pop(0)
    for i in rawList:
        currentRecord=[]
        student1 = i[0]
        student2 = i[1]
        student1Index = student1[student1.rfind('/')+1:student1.find('(')]
        currentRecord.append(student1Index.strip())
        student1Percent = student1[student1.find('(')+1:student1.find(')')-1]
        currentRecord.append(student1Percent.strip())
        student2Index = student2[student2.rfind('/')+1:student2.find('(')]
        currentRecord.append(student2Index.strip())
        student2Percent = student2[student2.find('(')+1:student2.find(')')-1]
        currentRecord.append(student2Percent.strip())
        dataList.append(currentRecord)
    return dataList


#DEBUG       
# def printDataList():
#     dataList = populateDataList()
#     print(len(dataList))
#     for i in dataList:
#         print(i)

initDataframe()

