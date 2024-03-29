import csv

with open('./csv/naive_bayes2.csv') as file:
    reader = csv.DictReader(file)
    totalYes = 0
    totalNo = 0
    totalData = 0
    confidentData = {}  # {key:[no,yes]}
    studiedData = {}  # {key:[no,yes]}
    sickData = {}  # {key:[no,yes]}

    data = []
    tempRes = 'Result'


    def insertData(colName, collec, row):
        if row[colName] in collec.keys():
            if row.get(tempRes) == 'pass':
                collec[row[colName]][1] += 1
            else:
                collec[row[colName]][0] += 1

        else:
            if row.get(tempRes) == 'pass':
                collec[row[colName]] = [0, 1]
            else:
                collec[row[colName]] = [1, 0]


    for row in reader:
        # ===========>COUNT
        totalData += 1
        if row['Result'] == 'pass':
            totalYes += 1
        else:
            totalNo += 1

        #DEBUG
        #print(row)  #=>{'Confident': 'yes', 'Studied': 'no', 'Sick': 'no', 'Result': 'fail'}

        # ========>CONFIDENT
        insertData('Confident', confidentData,row)

        # ==============>STUDIED
        insertData('Studied', studiedData,row)

        # ==============>SICK
        insertData('Sick', sickData,row)

    # =============>USER_INTERACTION
    chooseSituation = {}


    def insertSituation(type, collec):
        f2 = True
        while f2:
            print("There are these variants for ", type, " : ")
            for key in collec.keys():
                print('\t\t', key)
            print("*Input ", type, " : ")
            temp = input()
            if (temp not in collec.keys()):
                print("Invalid Input\n\tTry again!")
                f2 = True
            else:
                chooseSituation[type] = temp
                f2 = False
                print('\n')


    f1 = True
    while f1:
        print("Now tell me ,what situation you want to predict?")
        print("NOTE: this is a case-sensitive procedure, so be careful!\n \t***So type everything carefully***")
        ready = input("Are you ready?\n\tYES \t NO\n\t")
        if (ready == "YES"):
            insertSituation('Confident', confidentData)
            insertSituation('Studied', studiedData)
            insertSituation('Sick', sickData)

            yesEvent = float(totalYes/totalData * studiedData[chooseSituation['Studied']][1] / totalYes * confidentData[chooseSituation['Confident']][1] / totalYes * sickData[chooseSituation['Sick']][1] / totalYes)
            noEvent = float(totalNo/totalData * studiedData[chooseSituation['Studied']][0] / totalNo * confidentData[chooseSituation['Confident']][0] / totalNo * sickData[chooseSituation['Sick']][0] / totalNo)
            predictYesPercentage = float(yesEvent/(yesEvent+noEvent)) * 100
            predictNoPercentage = float(noEvent/(yesEvent+noEvent)) * 100
            print("Prediction Yes = ",predictYesPercentage,'%')
            print("Prediction No =  ",predictNoPercentage,'%')
            if predictYesPercentage > predictNoPercentage:
                print("This student may pass.")
            elif predictYesPercentage<predictNoPercentage:
                print("The student may not pass.")
            else:
                print("There are 50-50 chance that the student may pass or not.")
            f1 = False
        elif ready == 'NO':
            print("OK, See You Again!")
            f1 = False
        else:
            print("Invalid Input!\n\tLet's try again!")
            f1 = True
    print(chooseSituation)
