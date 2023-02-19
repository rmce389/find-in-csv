import os
import re
import string

try:
    # ask the user what file they wish to search
    fileName = input("Enter the file name: ")
    
    with open("..\\" + fileName + ".csv", "r") as file:

        # ask the user what word they wish to find
        word = input("Enter a word to find: ")

        # if "..\\cveJava.csv" exists, delete it
        if os.path.exists("..\\results.csv"):
            os.remove("..\\results.csv")
        resultsFile = open("..\\results.csv", "w")

        # read the file line-by-line
        print("Finding records...")
        for line in file:
            # if the word is found, write the line to the results file
            pattern = fr"(?<!\S){word}(?!\S)"
            match = re.search(pattern, line)

            if match:
                resultsFile.write(line)


        print("Records found and written to file.")
except IOError:
    print("Error opening file.")
finally:
    # close the file if it is open
    if file:
        file.close()
