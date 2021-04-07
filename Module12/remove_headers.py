import os as os
import csv 

def createDirectory(folder):    
    dirName = os.path.join(os.path.dirname(__file__), folder)
    if os.path.isdir(dirName) == False: 
        os.makedirs(dirName)

def listFiles(folder):
    dirName = os.path.join(os.path.dirname(__file__), folder)
    return os.listdir(dirName)

def getData(fileName):    
    fullPath = os.path.join(os.path.dirname(__file__), 'csv', fileName)
    csv_rows = []

    with open(fullPath, 'r') as csvFile:
        csv_reader = csv.reader(csvFile, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
            
            # skip the first line in the file because it is the header
            if line_count == 0:
                line_count += 1
                continue
            csv_rows.append(row)
    return csv_rows

def writeData(fileName, data):    
    fullPath = os.path.join(os.path.dirname(__file__), 'modified_csv', fileName)
    with open(fullPath, 'w', newline='') as csvFile:
        csv_writer = csv.writer(csvFile)
        for row in data:
            csv_writer.writerow(row)                

if __name__ == "__main__":
   createDirectory("modified_csv")
   for f in listFiles("csv"):
       data = getData(f)
       writeData(f, data)
