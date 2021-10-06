# The libraries used for the hash_file function include:
# difflib
# hashlib
# Hashes of two pdfs are created and compared, matching hashes indicate that the contents
# of the two files are identical.
# For purposes of testing we used a pdf of a jobReport that was verified for correctness and compared 
# that pdf to a recently generated pdf that is based on the same input given to MOSS
# Source : https://www.geeksforgeeks.org/check-if-two-pdf-documents-are-identical-with-python/

import hashlib
from difflib import SequenceMatcher


def hash_file(fileName1, fileName2):

	# Use hashlib to store the hash of a file
	h1 = hashlib.sha1()
	h2 = hashlib.sha1()

	with open(fileName1, "rb") as file:

		# Use file.read() to read the size of file
		# and read the file in small chunks
		# because we cannot read the large files.
		chunk = 0
		while chunk != b'':
			chunk = file.read(1024)
			h1.update(chunk)
			
	with open(fileName2, "rb") as file:

		# Use file.read() to read the size of file a
		# and read the file in small chunks
		# because we cannot read the large files.
		chunk = 0
		while chunk != b'':
			chunk = file.read(1024)
			h2.update(chunk)

		# hexdigest() is of 160 bits
		return h1.hexdigest(), h2.hexdigest()