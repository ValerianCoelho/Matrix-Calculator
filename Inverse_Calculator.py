from fractions import Fraction
import MatrixDisplayer as mat
import os

while True:
    No_Of_Matrices = int(input('Enter the number of matrices : '))

    # Working with Non-Augmented Matrix (Single Matrix)
    if No_Of_Matrices ==  1:
        rows = int(input('Enter the number of rows : '))
        cols = int(input('Enter the number of cols : '))

        matrix = []

        print('Enter the Elements in the Matrix : ')
        for i in range(rows):
            subMatrix = []
            for j in range(cols):
                while True:
                    try:
                        element = Fraction(input())
                        break
                    except:
                        continue
                subMatrix.append(element)
            matrix.append(subMatrix)
        
        os.system('cls')
        print(mat.green, 'Solution :-', mat.endl, sep='')
        mat.printSingleMatrix(matrix, False, 0, 'Let A = ')
        print(mat.violet, '\nBy Elementary Transformation Method :-', mat.endl)

        limit = 0
        if(len(matrix) < len(matrix[0])):
            limit = len(matrix)
        else:
            limit = len(matrix[0])

        for i in range(limit):
            print(mat.violet, f'\nIteration {i+1}: Set R{i+1} and Leading Row (LR{i+1})', mat.endl)
            mat.printSingleMatrix(matrix, True, i, 'A = ')
            if matrix[i][i] == 0:
                print(mat.red, '\nZero Encountered in the diagonal Element\n', mat.endl)
                choice = input('Do You wish to swap rows ? (y/n) : ')
                if(choice.lower() == 'y'):
                    R1 = int(input('Enter Row 1 : '))
                    R2 = int(input('Enter Row 2 : '))
                    matrix = mat.swap(matrix, R1-1, R2-1)
                    mat.printSingleMatrix(matrix, True, i, 'Swapped Matrix : ')
                else:
                    break
            mat.OperationDisplayer(matrix, i)
            for j in range(rows):
                if i == j:
                    matrix = mat.Box_Operation(matrix, j, matrix[i][i])
                else:
                    matrix = mat.Non_Box_Operation(matrix, j, i, matrix[j][i], matrix[i][i])
        print(mat.green, '\nMatrix in Echelon Form :-')
        mat.printSingleMatrix(matrix, False, 0, 'A = ')
        print(mat.endl)

    elif No_Of_Matrices == 2:
        rowsmatrix = int(input('Enter the number of rows in the first matrix : '))
        colsmatrix = int(input('Enter the number of cols in the first matrix : '))

        rowsidentity = int(input('Enter the number of rows in the second matrix : '))
        colsidentity = int(input('Enter the number of cols in the second matrix : '))

        matrix = []

        print('Enter the element in the First Matrix : ')

        for i in range(rowsmatrix):
            subMatrix = []
            for j in range(colsmatrix):
                while True:
                    try:
                        element = Fraction(input())
                        break
                    except:
                        continue
                subMatrix.append(element)
            matrix.append(subMatrix)

        identity = []

        print('Enter the element in the Second Matrix : ')

        for i in range(rowsidentity):
            subMatrix = []
            for j in range(colsidentity):
                while True:
                    try:
                        element = Fraction(input())
                        break
                    except:
                        continue
                subMatrix.append(element)
            identity.append(subMatrix)

        os.system('cls')
        print(mat.green, 'Solution :-' ,mat.endl, sep='')
        mat.printDoubleMatrix(matrix, identity, False, 0, 'Let [A:I] = ')
        print(mat.violet, '\nBy Elementary Transformation Method :-', mat.endl)

        limit = 0
        if(len(matrix) < len(matrix[0])):
            limit = len(matrix)
        else:
            limit = len(matrix[0])

        for i in range(limit):
            print(mat.violet,f'\nIteration {i+1}: Set R{i+1} and Leading Row (LR{i+1})',mat.endl)
            mat.printDoubleMatrix(matrix, identity, True, i, '')
            if matrix[i][i] == 0:
                print(mat.red, '\nZero Encountered in the diagonal Element\n', mat.endl)
                choice = input('Do You wish to swap rows ? (y/n) : ')
                if(choice.lower() == 'y'):
                    R1 = int(input('Enter Row 1 : '))
                    R2 = int(input('Enter Row 2 : '))
                    matrix = mat.swap(matrix, R1-1, R2-1)
                    identity = mat.swap(identity, R1-1, R2-1)
                    mat.printDoubleMatrix(matrix, identity, True, i, 'Swapped Matrix : ')
                else:
                    break
            mat.OperationDisplayer(matrix, i)
            if matrix[i][i] == 0:
                break
            for j in range(rowsmatrix):
                if i == j:
                    box = matrix[i][i]
                    matrix = mat.Box_Operation(matrix, j, box)
                    identity = mat.Box_Operation(identity, j, box)
                else:
                    circle = matrix[j][i]
                    box = matrix[i][i]
                    matrix = mat.Non_Box_Operation(matrix, j, i, circle, box)
                    identity = mat.Non_Box_Operation(identity, j, i, circle, box)

        print(mat.green, '\nMatrix in Echelon Form :-')
        mat.printDoubleMatrix(matrix, identity, False, 0, '[A:I] = ')
        print(mat.endl)
    else:
        print(mat.violet, "Error : Matrix Limit Exceeded\n", mat.endl, sep='', end='')
    Continue = input('Do you want to run the Program again ? (y/n) : ')
    if Continue == 'n':
        break
    else:
        os.system('cls')
os.system('pause')