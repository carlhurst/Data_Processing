import os
import csv as cs
import mysql.connector
import pandas as pd

def Column_Names(Path):

    columns = list(pd.DataFrame(pd.read_csv(Path,nrows=3)))
    list2 = []
    list3 = []
    for i in columns:
        list2.append(i.replace(" ", "_"))

    for i in list2:
        list3.append(i.upper())
    print(list(list3))

def FileFinder(path):
    """
    This Function returns a array object with all the file paths
    """
    # Store Array for file paths

    FilePaths = []

    for root, folder, file in os.walk(path):
        for files in file:
            FilePaths.append(os.path.join(root,files))

    return FilePaths

def FileOrganiser(FilePaths):

    """
    File organiser seperates the file paths into 3 arrays of outcomes, street, stopandsearch.
    It accepts one paramater which is the FilePaths to be sorted
    """

    outcomes= []
    Street = []
    StopAndSearch = []

    for f in FilePaths:

        if 'outcomes.csv' in f:
            outcomes.append(f)
        elif 'street.csv' in f:
            Street.append(f)
        else:
            StopAndSearch.append(f)

    return outcomes, Street, StopAndSearch

def MysqlConnection(cnx,line):

    # cnx = mysql.connector.connect(user='carl', password='lewisj',host='127.0.0.1', database='test')
    cursor = cnx.cursor()

    addEntry = ("INSERT INTO outcome "
                "(CRIME_ID, MONTH, REPORTED_BY, FALLS_WITHIN, LONGITUDE,"
                "LATITUDE, LOCATION, LSOA_CODE, LSOA_NAME, OUTCOME )"
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

    Value = ('8aa986b0d91bef6a3f84083b89aa21ab3d5cb5642dc0c0e0c1b724365d7f41cd',	'2015-04',	'Avon and Somerset Constabulary',	'Avon and Somerset Constabulary',	'-2.691152',	'51.3554',	'On or near THE BATCH',	'E01014383',	'Bath and North East Somerset 021B',	'Investigation complete; no suspect identified',
)

    cursor.execute(addEntry, line)
    # cnx.commit()





def main():

    fails = open(r'C:\Users\thor\Desktop\outcome Fails.txt', 'w')
    cnx = mysql.connector.connect(user='carl', password='lewisj', host='127.0.0.1', database='test')
    Issues = []

    path = r"C:\Users\thor\Documents\UK_Crime_Stats"
    paths = FileFinder(path)

    outcomes, Street, StopAndSearch = FileOrganiser(paths)

    Column_Names(outcomes[0])

    # for p in outcomes:
    #     for l in (open(p).readlines()[1:]):
    #         values = l.split(',')
    #         print(values)
    #         if values.__len__() > 10:
    #             Issues.append(values)
    #         else:
    #             MysqlConnection(cnx,values)
    #
    #     cnx.commit()
    #
    # for i in Issues:
    #     fails.writelines(i)
    #     fails.close()
    #
    # cnx.close()

if __name__ == '__main__':
    main()
