import os as os
import csv 
from school import School

def getFilePath(fileName):
    file_dir = os.path.dirname(__file__)
    #The file exists in Module7. Reusing the same file.
    file_dir = file_dir.replace('Module12', 'Module7')    
    return os.path.join(file_dir, fileName)

def getSchoolData(fileName):    
    fullPath = getFilePath(fileName)
    with open(fullPath, 'r') as schoolFile:
        csv_reader = csv.reader(schoolFile, delimiter=',')

        line_count = 0
        # initialize empty dictionary
        schoolsDict={}
        for row in csv_reader:
            # skip the first line in the file because it is the header
            if line_count == 0:
                line_count += 1
                continue
            # create an item in dictionary  with a key of the object id and a value of the object
            schoolId = row[2]
            schoolName = row[4]
            schoolZip = row[9]
            schoolState = row[8]
            schoolCounty = row[12]
            if(schoolCounty == 'Marshall County' and schoolState == 'AL'):
                schoolsDict[str(schoolId)] = School(schoolName,schoolCounty, schoolZip,  schoolState )
                
    return schoolsDict
    

def printSchoolDetail(schools):
    for value in schools.values():
        print(str(value))
    


if __name__ == "__main__":
   schools =  getSchoolData("Public_School_Locations_2017-18.csv")
   print(f'Total Schools: {len(schools)}')
   printSchoolDetail(schools)
