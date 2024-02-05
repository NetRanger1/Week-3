#region functions
def BuildAMatrix(element00, nRows=2, nCols=2):
    '''
    I'm creating a function to build a nRowsXnCols matrix to demonstrate list comprehension.
    Step 1: use a for loop to iterate through the rows of the matrix I want to create.
    Step 2: use a list comprehension to build the values for the columns in each row.  Set odd to negative, even to positive
    :param nRows: number of rows
    :param nCols: number of columns
    :return: a matrix of nRowsXnCols
    '''
    A=[] #empty list called A
    row=[] #a list for temporary storage
    c0=element00
    f=1.0
    y=lambda x: x**3;
    for r in range(nRows):
        row=[(c+c0)*(1.0 if (c+c0)%2==0 else -1.0) for c in range(nCols)]
        #  row=[y(c) for c in range(nCols)]
        # for c in range(nCols):
        #     f=1.0 if (c+c0)%2==0 else -1.0 #ternary operator
        #     row.append(f*(c+c0))
        A.append(row)
        c0+=nCols
    return A

def ElementByElementMult(a,b):
    C=[]
    for i in range(len(a)):
        C.append([])
        for j in range(len(a[i])):
            C[i].append(a[i][j]*b[i][j])
    return C

def Main():
    A=BuildAMatrix(1, nRows=10,nCols=10)
    B=BuildAMatrix(10, nRows=10, nCols=10)
    C=ElementByElementMult(A,B)
    print(A)
    print(C)
#endregion

if __name__ == "__main__":
    Main()