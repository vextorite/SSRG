import dominate
from dominate.tags import *

table_headers =['Code File 1', 'Code File 2', 'Side by side']

def create_page(individualPath, bound, savePath):
    '''
    The function leverages the python library "Dominate" that is used to write HTML documents using python code.
    The function creates a landing page that is used to view the source code comparisons from the non persitent
    MOSS report.
    Parameters:
    individualPath - Path to source html files that were saved
    bound - Integer value that indicates the amount of files present
    savePath - Specified path to save the generated html document
    '''
    doc = dominate.document(title='Historical Moss Request')

    with doc.head:
        link(rel='stylesheet', href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css")
        script(type='text/javascript', src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js")
        script(type='text/javascript', src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js")
        style("""\
            
            h1, h3, th{
                color: #fedb41;
            }

               h1, h3, th, tr{
                font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            }

       body  {
       background-color: #000000;
    
       }

        
    """)
        
    with doc:
        with div(cls='container'):
            h1('MOSS SSRG Persistent code files')
            with table(id='main', cls='table'):
                caption(h3('A table of moss reports'))
                with thead():
                    with tr():
                        for table_head in table_headers:
                            th(table_head)
                with tbody():
                    for i in range(0,bound+1):
                        with tr():
                
                            # td(a(f'Code file {i}-0'.title(), href=f'{individualPath}/record{i}-0.html', target='blank_', style='color: aliceblue'))
                            # td(a(f'Code file {i}-1'.title(), href=f'{individualPath}/record{i}-1.html', target='blank_', style='color: aliceblue' ))
                            # td(a(f'Comparison {i}'.title(), href=f'{individualPath}/Comaprison_Record_{i}.html', target='blank_', style='color: aliceblue' ))
                            newresourcepath = individualPath.replace('/','~')
                            # individualPath = f'../viewReport/{individualPath}'
                            td(a(f'Code file {i}-0'.title(), href=f'../viewReport/{newresourcepath}/record{i}-0.html', target='blank_', style='color: aliceblue'))
                            td(a(f'Code file {i}-1'.title(), href=f'../viewReport/{newresourcepath}/record{i}-1.html', target='blank_', style='color: aliceblue' ))
                            td(a(f'Comparison {i}'.title(), href=f'../viewReport/{newresourcepath}/Comaprison_Record_{i}.html', target='blank_', style='color: aliceblue' ))
    # print(doc)
    f = open(savePath, 'w')
    f.write(str(doc))
    f.close