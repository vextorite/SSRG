from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import urllib.parse
from itertools import dropwhile
from persistenceGenerator import create_page
from generateHtml import comparissonFrameConstructor
import codecs


def scrapeUrl(url):
    '''
    The scrape url method scrapes the MOSS url and retrives the useful information from the webpage.
    The method returns a well formatted list of the desired data scraped from the site.
    The beautifulSoup and urrlib libraries were utilised
    Parameters
    url - MOSS url returned from script execution
    '''
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


def saveCodeFiles(url,fRoot,jobID):
    '''
    The function saves all the embeded html code files and labels the files with appropriate names.
    The state of MOSS is handled while saving the embedded html, the function will automatically restart if 
    the server is in an unfavorable state
    Parameters
    url - MOSS url returned from script execution
    fRoot - User job Folder path
    jobID - Unique identifier of submitted job appended to filename
    '''
    workingList=scrapeUrl(url)
    bounds =len(workingList)-1
    print(bounds)
    successSave = False
    
    while successSave is False:
      try:
        saveLinks(url, fRoot, bounds)
        print('Links saved')
        successSave = True
      except:
        print('retrying saving moss connection lost')

    create_page(fRoot, bounds, f'{fRoot}/final_landing.html')

def saveLinks(url, fRoot, bounds):
  '''
  Utility function used to save MOSS html files
  Parameters
  url - MOSS url returned from script execution
  fRoot - User job Folder path
  bounds - integer value indicating amount of links
  '''
  for i in range(0,bounds):
    print(i)
    urlMatch0 = f'{url}/match{i}-0.html'
    response = urllib.request.urlopen(urlMatch0)
    webContent = response.read()
    exportPath0=f'{fRoot}/record{i}-0.html'
    file = open(exportPath0, 'wb')
    file.write(webContent)
    file.close

    urlMatch1 = f'{url}/match{i}-1.html'
    response = urllib.request.urlopen(urlMatch1)
    webContent = response.read()
    exportPath1= f'{fRoot}/record{i}-1.html'
    file = open(exportPath1, 'wb')
    file.write(webContent)
    file.close

    file1 = codecs.open(exportPath0, "r", "utf-8")
    html1String = file1.read()
    file1.close()

    file2 = codecs.open(exportPath1, "r", "utf-8")
    html2String = file2.read()
    file2.close()

  

    comparissonFrameConstructor(html1String, html2String, i, fRoot)