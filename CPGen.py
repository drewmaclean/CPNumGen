import random
import csv
import sys

FIRST_NAME_FILE = "First_Names.csv"
LAST_NAME_FILE = "Last_Names.csv"
first_list = []
last_list = []


def chooseName(name):
    if name == FIRST_NAME_FILE:
        strName = random.choice(first_list)
    else:
        strName = random.choice(last_list)
    #print(str(strFirst).strip('[\'\']'))
    return strName


def main(run_num):
    homeAreaCode = "406"
    areaCodeArray = ["208", "775", "307", "509", "970"]
    notprefix = ['0','1','4','9']
    strNumber = ""
    prefix = 0
    sufix = 0
    strFirst = ""
    strLast = ""
    repeatMTN_rand = 0
    iteration = 0
    writeArray = []

    repArray = ["Drew", "Deryk", ""]

    for z in range(int(run_num)):
        # generate name

        if iteration >= repeatMTN_rand or iteration == 0:
            repeatMTN_rand = random.randint(1, 4)
            if random.randint(0, 9) > 1:
                strFirst = chooseName(FIRST_NAME_FILE)
                if random.randint(0, 9) > 4:
                    strLast = chooseName(LAST_NAME_FILE)
                else:
                    strLast = ""
            else:
                strFirst = ""
                strLast = ""
            strName = str(strFirst).strip('[\'\']') + " " + str(strLast).strip('[\'\']')

            # generate pw/ssn
            if random.randint(0, 9) < 2:
                strPass = ""
            else:
                if random.randint(0, 9) > 2:
                    strPass = str(int(random.random() * 10000))
                else:
                    strPass = str(chooseName(FIRST_NAME_FILE)).strip('[\'\']')
                    while len(strPass) < 3 or len(strPass) > 5:
                        strPass = str(chooseName(FIRST_NAME_FILE)).strip('[\'\']')

            #generate rep
            strRep = random.choice(repArray)

            iteration = 0

        # generate MTN
        prefix = int(random.randint(200, 899))
        while str(prefix)[0] in notprefix:
            prefix = int(random.random() * 1000)
        if len(str(prefix)) < 3:
            prefix = prefix * 10
        sufix = int(random.random() * 10000)
        if len(str(sufix)) < 4:
            sufix = sufix * 10

        if random.randint(0, 9) == 0:
            strNumber = random.choice(areaCodeArray) + str(prefix) + str(sufix)
        else:
            strNumber = homeAreaCode + str(prefix) + str(sufix)


        #generate date
        day = random.randint(1, 28)
        month = random.randint(1, 12)
        year = random.randint(2014, 2016)
        strDate = str(month) + "/" + str(day) + "/" + str(year)

        #writeArray[iteration] = [strName, strNumber, strSSN, strDate, strRep]

        with open('output.csv', 'a', newline='') as csvfile:
            fw = csv.writer(csvfile, delimiter=',')
            fw.writerow([strName, strNumber, strPass, strDate, strRep])
        #print([strName, strNumber, strPass, strDate, strRep])
        #print(iteration, repeatMTN_rand)
        iteration = iteration + 1


if __name__ == "__main__":
    #def readFile():
    with open(FIRST_NAME_FILE, 'r') as f:
        reader = csv.reader(f)
        first_list = list(reader)
    with open(LAST_NAME_FILE, 'r') as f:
        reader = csv.reader(f)
        last_list = list(reader)
    #main(sys.argv[1])
    main(150)