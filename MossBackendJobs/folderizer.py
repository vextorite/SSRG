import os
import shutil
import zipfile
import sys
from pyunpack import Archive
from shutil import copyfile


rootdir = '/Users/suvanth/Subjects/final/MossBackendJobs'
outputDir = '/Users/suvanth/Subjects/final/MossBackendJobs/jobOutput'


if len(sys.argv) > 2:
    rootdir = str(sys.argv[1])
    outputDir = str(sys.argv[2])

verbose = False  # For debugging purposes, set verbose to True
# MOSS can be a pain to deal with if you need to upload a lot of files. Set this to true if you want the folderizer
# to stich all of a student's submitted code into one file  called STUDENT_NAME.stitch
# NOTE: Only use this flag if all of the students' code has been programmed in one programming language
stitch = False 


python_dir = outputDir + "/python"
java_dir = outputDir + "/java"
c_dir = outputDir + "/c"
cpp_dir = outputDir + "/cpp"

ext_list = [".py", ".java", ".cpp", ".c", ".h", ".cxx"]
lib_folder_list = ['git', 'doc', 'org', 'lib']
excl_path = ['Eigen', 'eigen-master']
rootcounter = 0
counter = 0

print('=============================Extracting Student Folders=====================================================')

for item in os.listdir(rootdir): # Get a list of all items in the root directory
    studentDir = os.path.join(rootdir,item)
    if os.path.isdir(studentDir) and not item.startswith("."): # Check if item is a directory and not hidden
        
        dir_path = os.path.join(outputDir, item)
        if not os.path.exists(dir_path): # If the student's folder doesnt exist in outputDir, create it.
            if verbose: print('Creating %s' % dir_path)
            os.makedirs(dir_path)

        # Extract all archive files

        for root, subdirs, files in os.walk(studentDir):
            for filename in files:
                file_path = os.path.join(root, filename)
                if not os.path.splitext(file_path)[1] == '.txt': # Assumes that the only files submitted are archives or
                    if verbose: print("Extracting file %s to %s" % (file_path, dir_path))
                    try:
                        Archive(file_path).extractall(dir_path)
                    except Exception as e:
                        print("Unzip Failed. Reason: " + str(e))


print('=================================Pulling out code=========================================================')

for item in os.listdir(outputDir): # Get a list of all items in the root directory
    studentDir = os.path.join(outputDir,item)

    if os.path.isdir(studentDir):

        # Extract all files necessary files to the student directory
        for root, subdirs, files in os.walk(studentDir):
            for filename in files:
                file_path = os.path.join(root, filename)
                ext = os.path.splitext(file_path)[1] 
                if ext in ext_list and not filename.startswith('.'):
                    # Some students don't have any project structure and their code is all in one folder.
                    # This check prevents unnecessary move operations
                    if not os.path.join(studentDir, filename) == file_path:
                        if verbose: print('Moving %s to %s' % (file_path, studentDir))
                        try:
                            shutil.move(file_path, studentDir)
                        except Exception as e:
                            print("Failed to move file> Reason: " + str(e))


print('=================================Cleaning Up Folders=========================================================')

# Cleans up the submission folders to only include student code.
for item in os.listdir(outputDir): # Get a list of all items in the root directory
    studentDir = os.path.join(outputDir,item)

    if os.path.isdir(studentDir):

        for studentItem in os.listdir(studentDir):
            item_path = os.path.join(studentDir, studentItem)

            if os.path.isdir(item_path): # We don't need to check file extensions if item is a directory
                if verbose: print('Removing directory %s' % item_path)
                try:
                    shutil.rmtree(item_path) # We need to use this to get rid of git files and other binary that the students submit.
                except Exception as e:
                    print("Failed to delete subdir> Reason: " + str(e))
            # If the item is a file, we must make sure it is not one of the files we want to examine
            else:
                ext = os.path.splitext(item_path)[1]
                if not ext in ext_list or studentItem.startswith('.'):
                    if verbose: print('Removing file %s' % item_path)
                    try:
                        os.remove(item_path)
                    except Exception as e:
                        print("Failed to delete file Reason: " + str(e))

if stitch:
    print('=================================Stitching Student files=========================================================')
    for directory in os.listdir(outputDir):
        studentDir = os.path.join(outputDir, directory)

        if os.path.isdir(studentDir):

            submitted_code = os.listdir(studentDir) # You need to do this before opening the .stitch file or else if will be included in the os.listdir call

            new_file_name = directory + ".stitch"
            with open(os.path.join(studentDir, new_file_name), 'w') as stich_file:
                for file in submitted_code:
                    file_path = os.path.join(studentDir, file)

                    with open(file_path, 'r') as to_read:
                        stich_file.write('\n\n--%s--\n\n' % file)
                        stich_file.write(to_read.read())

                
