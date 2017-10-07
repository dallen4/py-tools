# parse gradebook .csv's to simplify grade submissions
import pandas as pd
import numpy as np

def getGrades(studentID):
    col = list(df.columns.values)
    row = df.loc[studentID, :]
    i = 0
    for x in row:
        if i > 0:
            s = str(col[i]) + "\n" + str(x) + "\n\n"
            i = i + 1
            print(s)
        else:
            i = i + 1

def useStudent():
    for x in df.index.values:
        print(x)
    # print(df.index.values.tolist())
    studentID = input("\n\nPlease enter student's LUC ID...\nstudents/ >> ")
    studentMenu(studentID)

def useAssignment():
    print("This gradebook contains the following assignments:")
    i = 0
    for x in df.columns:
        if i == 0:
            i = i+1
        else:
            print(x)
    assignmentName = input("What assignment would you like to view?\nassignments/ >> ")
    series = df[assignmentName]
    print(series["aahmad8"])

def studentMenu(studentID):
    print("\nAccessing " + df["Student Name"][studentID] + "'s records...")
    print("\nWhat would you like to do?\n0: View Grades\n\n")
    action = eval(input("students/" + studentID + "/ >> "))
    options = { 0 : getGrades(studentID) }
    options[action]

def mainMenu():
    print("main menu")
    menuChoice = eval(input("Enter menu choice: "))
    options = { 0: useStudent, 1: useAssignment }
    options[menuChoice]()

print("Starting grading program...")
gradebookName = input("What is the name of your grade book file (include csv)? ")
df = pd.read_csv(gradebookName, index_col="Student ID")
# df = pd.read_csv('gradebook-COMP_330_001_6005_1176-10_3_17.csv', index_col="Student ID")
mainMenu()