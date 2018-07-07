import csv
import os
from datetime import datetime


for f in os.listdir('.'):

    filename = f
    date = datetime.strptime(filename, 'aea_panel_point_log_%m-%d-%y_%H-%M.csv') # assuming 24h time
    insert_str = date.strftime('%m/%d/%y %H:%M EST' )
    print(insert_str)

    skipRow1 = [' ****************************************************************************************************']
    skipRow2 = 'Supplied Field Panel number out of range'
    skipRow3 = ' ****************************************** End of Report *******************************************'
    skipRow4 = 'Field Panel is failed'
    skipRow5 = 'Timeout Waiting For Net Response'
    skipRow6 = 'Configured Trunk Currently Not Connected'
	
    cleanData = []
    counter = 0
    skips = 0

    f = open(filename)
    csv_f = csv.reader(f)

    for row in csv_f:
        counter = counter +1
        if row == skipRow1:
            skips = skips + 1
        elif skipRow2 in row[0]:
            skips = skips + 1
        elif skipRow3 in row[0]:
            skips = skips + 1
        elif skipRow4 in row[0]:
            skips = skips + 1
        elif skipRow5 in row[0]:
            skips = skips + 1
        elif skipRow6 in row[0]:
            skips = skips + 1
        else:
            cleanData.append([row[0],insert_str,row[4]])

    filenameNew = 'mod_'+filename
    with open(filenameNew, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(cleanData)
        


