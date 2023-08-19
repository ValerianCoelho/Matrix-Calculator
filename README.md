# Matrix Calculator
This is a Python program that solves matrices using the Elementary Transformation method. The program can handle both single and double matrices (augmented matrices).

## Prerequisites
- Python 3.10.2 or above
- fractions module (included in Python's standard library)

## Running the program
To run the program, simply execute the file MatrixSolver.py or Download the .exe file From the "Release" Section.

## Usage
### Single Matrix
If you want to solve a single matrix, the program will prompt you to enter the number of rows and columns of the matrix. After that, you will be prompted to enter each element of the matrix. The program will then display the matrix in echelon form.

### Double Matrix (Augmented Matrix)
If you want to solve a double matrix (augmented matrix), the program will prompt you to enter the number of rows and columns for both the first and second matrices. You will then be prompted to enter each element of both matrices. The program will then display the double matrix in echelon form.

## Additional Features
If a zero is encountered on the diagonal of the matrix, the program will ask if you want to swap rows. If you choose to swap rows, the program will perform the swap and display the swapped matrix.
The program uses a custom MatrixDisplayer module that prints matrices in a more visually appealing way.

## Examples
<details>
  <summary>Single Matrix</summary>
  
**Input:**
```
Enter the number of matrices : 1
Enter the number of rows : 6
Enter the number of cols : 6
Enter the Element in the Matrix :
57
23
83
6
99
12
30
41
75
91
85
68
32
89
44
67
57
18
81
54
2
47
79
51
74
25
22
36
63
87
41
38
57
42
8
81
```
**Output:**
```
Solution :-
        ┌                        ┐
        │ 57  23  83  6   99  12 │
        │ 30  41  75  91  85  68 │
Let A = │ 32  89  44  67  57  18 │
        │ 81  54  2   47  79  51 │
        │ 74  25  22  36  63  87 │
        │ 41  38  57  42  8   81 │
        └                        ┘

By Elementary Transformation Method :-

Iteration 1: Set R1 and Leading Row (LR1)
    ┌                        ┐
    │ 57  23  83  6   99  12 │
    │ 30  41  75  91  85  68 │
A = │ 32  89  44  67  57  18 │
    │ 81  54  2   47  79  51 │
    │ 74  25  22  36  63  87 │
    │ 41  38  57  42  8   81 │
    └                        ┘
R1 -> LR1 ÷ 57
R2 -> R2 - LR1 (30 ÷ 57)
R3 -> R3 - LR1 (32 ÷ 57)
R4 -> R4 - LR1 (81 ÷ 57)
R5 -> R5 - LR1 (74 ÷ 57)
R6 -> R6 - LR1 (41 ÷ 57)

Iteration 2: Set R2 and Leading Row (LR2)
    ┌                                                     ┐
    │ 1   23/57     83/57     2/19      33/19     4/19    │
    │ 0   549/19    595/19    1669/19   625/19    1172/19 │
A = │ 0   4337/57  -148/57    1209/19   27/19     214/19  │
    │ 0   405/19   -2203/19   731/19   -1172/19   645/19  │
    │ 0  -277/57   -4888/57   536/19   -1245/19   1357/19 │
    │ 0   1223/57  -154/57    716/19   -1201/19   1375/19 │
    └                                                     ┘
R1 -> R1 - LR2 (23/57 ÷ 549/19)
R2 -> LR2 ÷ 549/19
R3 -> R3 - LR2 (4337/57 ÷ 549/19)
R4 -> R4 - LR2 (405/19 ÷ 549/19)
R5 -> R5 - LR2 (-277/57 ÷ 549/19)
R6 -> R6 - LR2 (1223/57 ÷ 549/19)

Iteration 3: Set R3 and Leading Row (LR3)
    ┌                                                                  ┐
    │ 1  0   1678/1647     -1847/1647      2104/1647     -1072/1647    │
    │ 0  1   595/549        1669/549       625/549        1172/549     │
A = │ 0  0  -140093/1647   -276170/1647   -140324/1647   -248974/1647  │
    │ 0  0  -8482/61       -1606/61       -5243/61       -705/61       │
    │ 0  0  -132563/1647    70795/1647    -98810/1647     134717/1647  │
    │ 0  0  -42749/1647    -45365/1647    -144338/1647    43751/1647   │
    └                                                                  ┘
R1 -> R1 - LR3 (1678/1647 ÷ -140093/1647)
R2 -> R2 - LR3 (595/549 ÷ -140093/1647)
R3 -> LR3 ÷ -140093/1647
R4 -> R4 - LR3 (-8482/61 ÷ -140093/1647)
R5 -> R5 - LR3 (-132563/1647 ÷ -140093/1647)
R6 -> R6 - LR3 (-42749/1647 ÷ -140093/1647)

Iteration 4: Set R4 and Leading Row (LR4)
    ┌                                                               ┐
    │ 1  0  0  -438473/140093     36000/140093     -344844/140093   │
    │ 0  1  0   126583/140093     7405/140093       29234/140093    │
A = │ 0  0  1   276170/140093     140324/140093     248974/140093   │
    │ 0  0  0   34712862/140093   7470829/140093    33000523/140093 │
    │ 0  0  0   28250035/140093   2889606/140093    31498269/140093 │
    │ 0  0  0   3309455/140093   -8635114/140093    10183727/140093 │
    └                                                               ┘
R1 -> R1 - LR4 (-438473/140093 ÷ 34712862/140093)
R2 -> R2 - LR4 (126583/140093 ÷ 34712862/140093)
R3 -> R3 - LR4 (276170/140093 ÷ 34712862/140093)
R4 -> LR4 ÷ 34712862/140093
R5 -> R5 - LR4 (28250035/140093 ÷ 34712862/140093)
R6 -> R6 - LR4 (3309455/140093 ÷ 34712862/140093)

Iteration 5: Set R5 and Leading Row (LR5)
    ┌                                                         ┐
    │ 1  0  0  0   32302969/34712862      17840407/34712862   │
    │ 0  1  0  0  -4915529/34712862      -22574357/34712862   │
A = │ 0  0  1  0   10021303/17356431     -1681577/17356431    │
    │ 0  0  0  1   7470829/34712862       33000523/34712862   │
    │ 0  0  0  0  -790508351/34712862     1150158361/34712862 │
    │ 0  0  0  0  -2316132091/34712862    1743788513/34712862 │
    └                                                         ┘
R1 -> R1 - LR5 (32302969/34712862 ÷ -790508351/34712862)
R2 -> R2 - LR5 (-4915529/34712862 ÷ -790508351/34712862)
R3 -> R3 - LR5 (10021303/17356431 ÷ -790508351/34712862)
R4 -> R4 - LR5 (7470829/34712862 ÷ -790508351/34712862)
R5 -> LR5 ÷ -790508351/34712862
R6 -> R6 - LR5 (-2316132091/34712862 ÷ -790508351/34712862)

Iteration 6: Set R6 and Leading Row (LR6)
    ┌                                        ┐
    │ 1  0  0  0  0   1476585843/790508351   │
    │ 0  1  0  0  0  -676949498/790508351    │
A = │ 0  0  1  0  0   587493176/790508351    │
    │ 0  0  0  1  0   999048291/790508351    │
    │ 0  0  0  0  1  -1150158361/790508351   │
    │ 0  0  0  0  0  -37030634574/790508351  │
    └                                        ┘
R1 -> R1 - LR6 (1476585843/790508351 ÷ -37030634574/790508351)
R2 -> R2 - LR6 (-676949498/790508351 ÷ -37030634574/790508351)
R3 -> R3 - LR6 (587493176/790508351 ÷ -37030634574/790508351)
R4 -> R4 - LR6 (999048291/790508351 ÷ -37030634574/790508351)
R5 -> R5 - LR6 (-1150158361/790508351 ÷ -37030634574/790508351)
R6 -> LR6 ÷ -37030634574/790508351

Matrix in Echelon Form :-
    ┌                  ┐
    │ 1  0  0  0  0  0 │
    │ 0  1  0  0  0  0 │
A = │ 0  0  1  0  0  0 │
    │ 0  0  0  1  0  0 │
    │ 0  0  0  0  1  0 │
    │ 0  0  0  0  0  1 │
    └                  ┘
```
</details>
<details>
  <summary>Double Matrix (Augmented Matrix)</summary>
  
**Input:**
```
Enter the number of matrices : 2
Enter the number of rows in the first matrix : 4
Enter the number of cols in the first matrix : 4
Enter the number of rows in the second matrix : 4
Enter the number of cols in the second matrix : 4
Enter the element in the First Matrix :
49
87
3
22
91
16
70
55
34
11
98
27
42
61
76
8
Enter the element in the Second Matrix :
77
46
20
12
99
92
50
5
80
51
62
9
68
89
39
98
```
**Output:**
```
Solution :-
            ┌                                 ┐
            │ 49  87  3   22 │ 77  46  20  12 │
Let [A:I] = │ 91  16  70  55 │ 99  92  50  5  │
            │ 34  11  98  27 │ 80  51  62  9  │
            │ 42  61  76  8  │ 68  89  39  98 │
            └                                 ┘

By Elementary Transformation Method :-

Iteration 1: Set R1 and Leading Row (LR1)
┌                                 ┐
│ 49  87  3   22 │ 77  46  20  12 │
│ 91  16  70  55 │ 99  92  50  5  │
│ 34  11  98  27 │ 80  51  62  9  │
│ 42  61  76  8  │ 68  89  39  98 │
└                                 ┘
R1 -> LR1 ÷ 49
R2 -> R2 - LR1 (91 ÷ 49)
R3 -> R3 - LR1 (34 ÷ 49)
R4 -> R4 - LR1 (42 ÷ 49)

Iteration 2: Set R2 and Leading Row (LR2)
┌                                                                   ┐
│ 1   87/49     3/49      22/49  │  11/7   46/49   20/49     12/49  │
│ 0  -1019/7    451/7     99/7   │ -44     46/7    90/7     -121/7  │
│ 0  -2419/49   4700/49   575/49 │  186/7  935/49  2358/49   33/49  │
│ 0  -95/7      514/7    -76/7   │  2      347/7   153/7     614/7  │
└                                                                   ┘
R1 -> R1 - LR2 (87/49 ÷ -1019/7)
R2 -> LR2 ÷ -1019/7
R3 -> R3 - LR2 (-2419/49 ÷ -1019/7)
R4 -> R4 - LR2 (-95/7 ÷ -1019/7)

Iteration 3: Set R3 and Leading Row (LR3)
┌                                                                                        ┐
│ 1  0   6042/7133     4433/7133   │ 7381/7133     7268/7133     4030/7133    243/7133   │
│ 0  1  -451/1019     -99/1019     │ 308/1019     -46/1019      -90/1019      121/1019   │
│ 0  0   528333/7133   49492/7133  │ 295970/7133   120213/7133   312156/7133  46618/7133 │
│ 0  0   68703/1019   -12407/1019  │ 6218/1019     49889/1019    21051/1019   91023/1019 │
└                                                                                        ┘
R1 -> R1 - LR3 (6042/7133 ÷ 528333/7133)
R2 -> R2 - LR3 (-451/1019 ÷ 528333/7133)
R3 -> LR3 ÷ 528333/7133
R4 -> R4 - LR3 (68703/1019 ÷ 528333/7133)

Iteration 4: Set R4 and Leading Row (LR4)
┌                                                                                        ┐
│ 1  0  0   5025/9269       │  5193/9269        7658/9269     2/31        -29/713        │
│ 0  1  0  -29425/528333    │  290686/528333    515/9269      102/589      6413/40641    │
│ 0  0  1   49492/528333    │  295970/528333    2109/9269     348/589      3586/40641    │
│ 0  0  0  -3256551/176111  │ -5576988/176111   311606/9269  -11295/589    1129505/13547 │
└                                                                                        ┘
R1 -> R1 - LR4 (5025/9269 ÷ -3256551/176111)
R2 -> R2 - LR4 (-29425/528333 ÷ -3256551/176111)
R3 -> R3 - LR4 (49492/528333 ÷ -3256551/176111)
R4 -> LR4 ÷ -3256551/176111

Matrix in Echelon Form :-
        ┌                                                                                       ┐
        │ 1  0  0  0 │ -133217/361839     1966744/1085517   -60029/120613     2609314/1085517   │
[A:I] = │ 0  1  0  0 │  2102342/3256551  -446395/9769653     250681/1085517  -911746/9769653    │
        │ 0  0  1  0 │  1301878/3256551   3886741/9769653    535904/1085517   4988518/9769653   │
        │ 0  0  0  1 │  1858996/1085517  -5920514/3256551    375245/361839   -14683565/3256551  │
        └                                                                                       ┘
```

</details>

## Credits
This program was developed by Valerian Coelho

## License
This program is licensed under the MIT License.
