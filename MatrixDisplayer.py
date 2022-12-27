from fractions import Fraction

red = '\033[91m'
green = '\033[92m'
yellow = '\033[38;2;255;255;0m'
blue = '\033[94m'
violet = '\033[38;2;163;117;255m'
endl = '\033[0m'

def getVerticalElementsLen(Matrix):
    rows = len(Matrix)
    cols = len(Matrix[0])
    VerticalElementsLen = []
    VerticalSign = []
    for i in range(cols):
        sign = 0
        max = len(str(Matrix[0][i]))
        for j in range(rows):
            if len(str(Matrix[j][i])) > max:
                max = len(str(Matrix[j][i]))
            if Matrix[j][i] < 0 and sign == 0:
                sign = 1
        if sign == 1:
            max = max + 1
        VerticalElementsLen.append(max)
        VerticalSign.append(sign)
    return VerticalElementsLen, VerticalSign

def printSingleMatrix(Matrix, colors, index, text):
    index = index + 1
    rows = len(Matrix)
    cols = len(Matrix[0])
    VerticalElementsLen, VerticalSign = getVerticalElementsLen(Matrix)
    for i in range(rows+2):
        if i==round(rows/2):
            print(text, sep='', end='')
        else:
            print(' '*len(text),sep='', end='')
        if i==0:
            print('┌',' '*(sum(VerticalElementsLen)+cols*2),'┐',sep='')
        elif i==rows+1:
            print('└',' '*(sum(VerticalElementsLen)+cols*2),'┘',sep='')
        else:
            print('│',end='')
            for j in range(cols):
                sign = 0
                if(VerticalSign[j] == 1 and Matrix[i-1][j] >= 0):
                    sign = 1
                
                if j==index-1 and i==index and colors:
                    print(blue, ' ',' '*sign, Matrix[i-1][j], ' '*(VerticalElementsLen[j]-len(str(Matrix[i-1][j]))-sign), ' ', endl, sep='', end='')
                elif j==index-1 and i!=index and colors:
                    print(yellow, ' ',' '*sign, Matrix[i-1][j], ' '*(VerticalElementsLen[j]-len(str(Matrix[i-1][j]))-sign), ' ', endl, sep='', end='')
                else:
                    print(' ',' '*sign, Matrix[i-1][j], ' '*(VerticalElementsLen[j]-len(str(Matrix[i-1][j]))-sign), ' ',sep='', end='')
            print('│')

def printDoubleMatrix(Matrix, IdentityMatrix, colors, index, text):
    index = index + 1
    rowsmatrix = len(Matrix)
    colsmatrix = len(Matrix[0])

    rowsidentity = len(IdentityMatrix)
    colsidentity = len(IdentityMatrix[0])

    VerticalElementsLenMatrix, VerticalSignMatrix = getVerticalElementsLen(Matrix)
    VerticalElementsLenIdentity, VerticalSignIdentity = getVerticalElementsLen(IdentityMatrix)

    for i in range(rowsmatrix+2):
        if i==round(rowsmatrix/2):
            print(text, sep='', end='')
        else:
            print(' '*len(text),sep='', end='')
        if i==0:
            print('┌',' '*(sum(VerticalElementsLenMatrix)+sum(VerticalElementsLenIdentity)+(colsmatrix+colsidentity)*2+1),'┐',sep='')
        elif i==rowsmatrix+1:
            print('└',' '*(sum(VerticalElementsLenMatrix)+sum(VerticalElementsLenIdentity)+(colsmatrix+colsidentity)*2+1),'┘',sep='')
        else:
            print('│',end='')
            for j in range(colsmatrix):
                sign = 0
                if(VerticalSignMatrix[j] == 1 and Matrix[i-1][j] >= 0):
                    sign = 1
                if j==index-1 and i==index and colors:
                    print(blue, ' ',' '*sign, Matrix[i-1][j], ' '*(VerticalElementsLenMatrix[j]-len(str(Matrix[i-1][j]))-sign), ' ', endl,sep='', end='')
                elif j==index-1 and i!=index and colors:
                    print(yellow, ' ',' '*sign, Matrix[i-1][j], ' '*(VerticalElementsLenMatrix[j]-len(str(Matrix[i-1][j]))-sign), ' ', endl,sep='', end='')
                else:
                    print(' ',' '*sign, Matrix[i-1][j], ' '*(VerticalElementsLenMatrix[j]-len(str(Matrix[i-1][j]))-sign), ' ',sep='', end='')
            print('│', end='', sep='')
            for j in range(colsidentity):
                sign = 0
                if(VerticalSignIdentity[j] == 1 and IdentityMatrix[i-1][j] >= 0):
                    sign = 1
                print(' ',' '*sign, IdentityMatrix[i-1][j], ' '*(VerticalElementsLenIdentity[j]-len(str(IdentityMatrix[i-1][j]))-sign), ' ',sep='', end='')
            print('│')

def printDeterminant(Matrix, text):
    rows = len(Matrix)
    cols = len(Matrix[0])
    VerticalElementsLen = getVerticalElementsLen(Matrix)

    for i in range(rows):
        if i==round(rows/2)-1:
            print(text, sep='', end='')
        else:
            print(' '*len(text),sep='', end='')

        print('│',end='')
        for j in range(cols):
            print(' ',Matrix[i][j], ' '*(VerticalElementsLen[j]-len(str(Matrix[i][j]))), ' ',sep='', end='')
        print('│')
    
def OperationDisplayer(matrix, index):
    limit = 0
    if(len(matrix) < len(matrix[0])):
        limit = len(matrix)
    else:
        limit = len(matrix[0])
    for j in range(limit):
        if index==j:
            print(f'R{index+1} -> LR{j+1} ÷ {blue}{matrix[index][index]}{endl}')
        else:
            print(f'R{j+1} -> R{j+1} - LR{index+1} ({yellow}{matrix[j][index]}{endl} ÷ {blue}{matrix[index][index]}{endl})')

def Non_Box_Operation(matrix, R, LR, circle, box):
    for i in range(len(matrix[0])):
        matrix[R][i] = matrix[R][i] - (matrix[LR][i]*circle)/box
    return matrix

def Box_Operation(matrix, LR, box):
    for i in range(len(matrix[0])):
        matrix[LR][i] = matrix[LR][i]/box
    return matrix

def swap(matrix, R1, R2):
    matrix[R1], matrix[R2] = matrix[R2], matrix[R1]
    return matrix