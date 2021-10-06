from pdfCompare import hash_file
def testJobRequests(validatedPDF, generatedPDF):
    '''
    Tests whether job requests are performed correctly by comparing the output pdfs of a known to be correct pdf with a generated pdf.
    This tests that appropriate links were scraped from the MOSS url
    Matplotlib graphs were generated correctly
    PDF generation performed deterministicly
    '''
    status = False
    msg1, msg2 = hash_file(validatedPDF, generatedPDF)

    if(msg1 != msg2):
	    status = False
    else:
        status = True
    return status





