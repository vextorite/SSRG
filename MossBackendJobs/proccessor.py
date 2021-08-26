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