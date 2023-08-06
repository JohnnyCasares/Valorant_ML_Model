import csv
import re
import statistics

# opening the CSV file
with open("C:/Users/johnn/Desktop/FIU/Summer 2023/ML/EXTRACTION/file.csv", mode='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)

    # displaying the contents of the CSV file

    csvFileClean = []
    fixedDataCsv = []

    for lines in csvFile:
        modified_lines = []
        for number in lines:
            if "Team" not in number:
                modified_number = re.sub(r'[^0-9]', '', number)
                modified_lines.append(modified_number)
        csvFileClean.append(modified_lines)

    # for lines in csvFileClean:
    #     print(lines)

    size = len(csvFileClean)
    teamsIndex = 3  # teams start to show at the 3rd index (row)

    for indexA, indexB in zip(range(1, size, 12), range(2, size, 12)):  # this goes over who won the match
        teamAOutcome = int(csvFileClean[indexA][0])  # Get team result
        teamBOutcome = int(csvFileClean[indexB][0])
        if teamAOutcome > teamBOutcome:
            # print("A WON")
            teamAOutcome = 1
            teamBOutcome = 0
        else:
            # print("B WON")
            teamAOutcome = 0
            teamBOutcome = 1

        combatA = 0
        kA = 0
        dA = 0
        aA = 0
        combatB = 0
        kB = 0
        dB = 0
        aB = 0

        counter = 10
        while counter != 0:
            if counter <= 5:
                combatB += int(csvFileClean[teamsIndex][0])
                kB += int(csvFileClean[teamsIndex][1])
                dB += int(csvFileClean[teamsIndex][2])
                aB += int(csvFileClean[teamsIndex][3])
                csvFileClean[teamsIndex].append(str(teamBOutcome))  # adds team outcome to the csv
            else:
                # get average of combat score, k, d, a
                combatA += int(csvFileClean[teamsIndex][0])
                kA += int(csvFileClean[teamsIndex][1])
                dA += int(csvFileClean[teamsIndex][2])
                aA += int(csvFileClean[teamsIndex][3])
                # new_csv[teamsIndex].insert(0, "A")
                csvFileClean[teamsIndex].append(str(teamAOutcome))
            teamsIndex += 1
            counter -= 1
        teamsIndex += 2
        combatA /= 5
        kA /= 5
        dA /= 5
        aA /= 5
        combatB /= 5
        kB /= 5
        dB /= 5
        aB /= 5
        teamARow = [combatA, kA, dA, aA, teamAOutcome]
        teamBRow = [combatB, kB, dB, aB, teamBOutcome]
        fixedDataCsv.append(teamARow)
        fixedDataCsv.append(teamBRow)

    for lines in fixedDataCsv:
        print(lines)

    with open('fixedData.csv', mode='w') as fixedData:
        data_writer = csv.writer(fixedData, delimiter=',')
        for lines in fixedDataCsv:
            data_writer.writerow(lines)
