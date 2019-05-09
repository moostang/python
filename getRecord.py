def getRecord(popUpInfo):
    # Program to extract popUpInfo from KMZ file
    # ------------------------------------------
    # INPUT
    #   rowCount
    #   colCount

    # IMPORTANT NOTICE:
    # ----------------
    # CURRENTLY, THE PROGRAM DOES NOT HANDLE EMPTY SPACES ' '  IN FRONT OF HTML
    # TAGS.
    #    ASSUMPTIONS:
    #    -----------
    #    1. There are no spaces before the HTML tags
    #    2. Only <td> and </td> are in the same line, while other tags's start
    #       and end are at different lines.
    #    3. There is always a single header

    # Open popUpInfo text file
    # ------------------------
    #popUpInfo = []
    #with open('C:\\GIS\\TIDEWATER\\SCRIPTS\\kmz_html.html','r') as file:
    #    for line in file:
    #        popUpInfo.append(line)

    rowCount = len(popUpInfo)
    rowIndex = 0
    # Skip <HTML> only
    for i in range(rowIndex,rowCount):
        rowIndex = rowIndex + 1
        if popUpInfo[i][1:5] == 'html' or popUpInfo[i][1:5] == 'HTML':
            print('Skipping row ' + str(i) + '. Contains <HTML> tag.')
            break
    print('rowIndex: ' + str(rowIndex))

    # Skip from <HEAD> to </HEAD>
    for i in range(rowIndex,rowCount):
        rowIndex = rowIndex + 1
        print('i Index: ' + str(i) + ', rowIndex: ' + str(rowIndex))
        if popUpInfo[i][1:5] == 'head' or popUpInfo[i][1:5] == 'HEAD':
            print('Skipping row ' + str(i) + '. Contains <HEAD> tag.')
            for j in range(rowIndex,rowCount):
                rowIndex = rowIndex + 1
                print('     j Index: ' + str(j), ', rowIndex: ' + str(rowIndex))
                if popUpInfo[j][2:6] == 'head':
                    print('  Skipping row ' + str(j) + '. Contains <HEAD> information.')
                    break
            break
    print('rowIndex: ' + str(rowIndex))

    # Skip <BODY> only
    for i in range(rowIndex,rowCount):
        rowIndex = rowIndex + 1
        if popUpInfo[i][1:5] == 'body' or popUpInfo[i][1:5] == 'BODY' :
            print('Skipping row ' + str(i) + '. Contains <BODY> tag.')
            break
    print('rowIndex: ' + str(rowIndex))

    # Skip <TABLE> only
    for i in range(rowIndex,rowCount):
        rowIndex = rowIndex + 1
        if popUpInfo[i][1:6] == 'table' or popUpInfo[i][1:6] == 'TABLE' :
            print('Skipping row ' + str(i) + '. Contains <BODY> tag.')
            break
    print('rowIndex: ' + str(rowIndex))

    # Read header
    # -----------
    # The header information is inside a cell that has all of its columns merged
    # into a single column. Thus, we directly jump to <td> </td>
    for i in range(rowIndex,rowCount):
        rowIndex = rowIndex + 1
        if popUpInfo[i][1:3] == 'td' or popUpInfo[i][1:6] == 'TD' :
            print('Header information found at rowIndex: ' + str(i))
            print(' ')
            header = popUpInfo[i].split('<td>')[1].split('</td>')[0]
            print('Header is: ' + header)
            print(' ')
            break
    print('rowIndex: ' + str(rowIndex))

    # Skip <TD> only
    for i in range(rowIndex,rowCount):
        rowIndex = rowIndex + 1
        if popUpInfo[i][1:3] == 'td' or popUpInfo[i][1:6] == 'TD' :
            print('Skipping row ' + str(i) + '. Contains <TD> tag.')
            break

    fields = []
    for i in range(rowIndex,rowCount):
        if popUpInfo[i][1:3] == 'td' or popUpInfo[i][1:6] == 'TD' :
            text = popUpInfo[i].split('<td>')[1].split('</td>')[0]
            print(i, j, text)
            fields.append(text)

    # Make record
    record = ''
    top = ''
    for i in range(1,len(fields)-1,2):
        top = str(top) + str(fields[i-1]) + ','
        record = str(record) + str(fields[i]) + ','


    record = header + ',' + record[0:-1] + '\n'
    header = 'Name' + ',' + top[0:-1] + '\n'

    print(header)
    print(record)
    return header, record
