import os as os

def getFilePath(fileName):
    file_dir = os.path.dirname(__file__)
    return os.path.join(file_dir, fileName)

def getSchoolData(fileName):
    schools = list()
    fullPath = getFilePath(fileName)
    with open(fullPath, 'r') as schoolFile:
        for line in schoolFile:
            school = line.split(',')
            schoolName = school[4]
            schoolZip = school[9]
            schoolState = school[8]
            schoolCounty = school[12]
            schoolDetail = (schoolName, schoolZip, schoolCounty)
            if(schoolCounty == 'Marshall County' and schoolState == 'AL'):
                schools.append(schoolDetail)
                
    return schools
    

def printSchoolDetail(schools):
    for i in schools:
        print(i)
    


if __name__ == "__main__":
   schools =  getSchoolData("Public_School_Locations_2017-18.csv")
   print(f'Total Schools: {len(schools)}')
   printSchoolDetail(schools)
