import ast
import math

def string2Val(mess):
    sum = 0
    for i in range(0,len(mess)):
        sum += ord(mess[i])
    return sum


def isNumeric(matrix, colIndex):
    for i in range(0,len(matrix)):
        if matrix[i][colIndex] is None or type(matrix[i][colIndex]) == float or type(matrix[i][colIndex]) == int:
            return True
        if type(matrix[i][colIndex]) == str:
            return False

def column_wise(matrix, index,f):
    for i in range(0,len(matrix)):
        try:
            matrix[i][index] = f(matrix[i][index]); # Tránh trường hợp casting cho "" nên phải có try catch
        except ValueError:
            matrix[i][index] = None;

def read_csv(path, delimeter=",", isHeader=False, getFeatures=False): 
    with open(path, "r") as file:
        rows = file.readlines()
        startIndex = 0
        features = []
        if isHeader == True: 
            startIndex +=1
            features = [el for el in rows[0].strip().split(delimeter)]
        db = [[el for el in rows[i].strip().split(delimeter)] for i in range(startIndex,len(rows))]
        lenCol = len(db[0])
        i =0
        while i < lenCol:
            try:
                evalI = 0
                while evalI < len(db) and len(db[evalI][i]) == 0:
                    evalI +=1
                    if(evalI >= len(db)): 
                        for el in db:
                            del el[i]
                        evalI = 0
                        lenCol -= 1  
                        if isHeader == True:
                            del features[i] 
                if type(ast.literal_eval(db[evalI][i])) == float:
                    column_wise(db,i,lambda x : float(x))
                elif type(ast.literal_eval(db[evalI][i])) == int:
                    column_wise(db,i,lambda x : int(x))
            except ValueError:
                dummy = 0; # Để cho compiler nó hài lòng
            except SyntaxError:
                dummy = 0; # Để cho compiler nó hài lòng
            i += 1
        if getFeatures == False:
            return db
        return db,features
    
def isMissing(val):
    if (type(val) == str and len(val) == 0) or val is None:
        return True;
    return False;

def deleteColumn(matrix, colIndex):
    for i in range(0,len(matrix)):
        del matrix[i][colIndex];

def deleteRow(matrix, rowIndex):
    del matrix[rowIndex]
        

def calMean(matrix, colIndex):
    sum = 0
    size = 0
    for i in range(0,len(matrix)):
        try:
            if matrix[i][colIndex] is None :
                continue
            sum += matrix[i][colIndex]
        except TypeError:
            sum += string2Val(matrix[i][colIndex])
        size += 1
    return (sum * 1.0) / size


def calMedian(matrix, colIndex):
    colVals = [matrix[i][colIndex] for i in range(0,len(matrix))]
    colVals.sort()
    startIndex = 0
    if colVals[len(colVals)-1] is None:
        return -1
    while(startIndex < len(colVals) and colVals[startIndex] is None):
        startIndex += 1
    try:
        median = colVals[int((len(colVals)-startIndex)/2)]
    except TypeError:
        median = string2Val(colVals[int((len(colVals)-startIndex)/2)])
    if (len(colVals) - startIndex) % 2 == 0:
        try:
            median += colVals[int((len(colVals)-startIndex)/2) + 1]
        except TypeError:
            median = string2Val(colVals[int((len(colVals)-startIndex)/2) + 1])
        median /= 2
    return median

def calMode(matrix, colIndex):
    colVals = [matrix[i][colIndex] for i in range(0,len(matrix))]
    map = {"":0}
    maxVal = ""
    for i in range(0,len(colVals)):
        if(map.get(colVals[i],-1) == -1):
            map[colVals[i]] = 1
        else:
            map[colVals[i]] += 1
        if(map[colVals[i]] > map[maxVal]):
            maxVal = colVals[i]
    return maxVal


def write_csv(path, data,delimeter=",", headers=[]):
    lines = []
    for i in range(0,len(data)):
        line = f'{data[i][0]}'
        for j in range(1,len(data[i])):
            line = delimeter.join((line,str(data[i][j])))
        lines.append(line.strip("\n"))
    rows = "\n".join(lines)
    with open(path, "w") as file:
        if(len(headers) != 0):
            file.write(delimeter.join(headers))
            file.write("\n")
        file.write(rows)


def calStd(matrix, colIndex, mean):
    std = 0
    size = 0
    for i in range(0,len(matrix)):
        try:
            if matrix[i][colIndex] is None:
                continue
            std += (matrix[i][colIndex] - mean) ** 2
        except TypeError:
            std += (string2Val(matrix[i][colIndex]) - mean) ** 2
        size += 1
    std /= size
    std = math.sqrt(std)
    return std


def findMinMax(matrix, colIndex):
    min = 0
    max = 0
    flag = 0
    for i in range(1,len(matrix)):
        cmpVal = matrix[i][colIndex]
        minVal = matrix[min][colIndex]
        maxVal = matrix[max][colIndex]
        if(type(cmpVal) == str):
            cmpVal = string2Val(cmpVal)
            minVal = string2Val(minVal)
            maxVal = string2Val(maxVal)
            flag = 1
        if(cmpVal < minVal):
            min = i
        if(cmpVal > maxVal):
            max = i
    if flag == 1:
        min = string2Val(matrix[min][colIndex])
        max = string2Val(matrix[max][colIndex])
    else:
        min = matrix[min][colIndex]
        max = matrix[max][colIndex]
    return min,max

def standardization(val, mean, std):
    if type(val) == str:
        val = string2Val(val)
    return (val - mean) * 1.0/ std
    

def min_maxScale(val, min, max):
    if type(val) == str:
        val = string2Val(val)
    return (val - min)/ (max - min)

def normalization( matrix, colIndex,method,args1, args2):
    for i in range(0,len(matrix)):
        if matrix[i][colIndex] is None:
            continue
        matrix[i][colIndex] = method(matrix[i][colIndex],args1,args2)


def addition(a, b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    if b == 0:
        return None
    return a / b


def columnWise(matrix, colIndexA, colIndexB, f):
    output = []
    for i in range(0,len(matrix)):
        a = matrix[i][colIndexA]
        b = matrix[i][colIndexB]
        if matrix[i][colIndexA] is None or matrix[i][colIndexB] is None:
            continue
        if type(matrix[i][colIndexA]) == str:
            a = string2Val(matrix[i][colIndexA])
        if type(matrix[i][colIndexB]) == str:
            b = string2Val(matrix[i][colIndexB])
        output.append([f(a,b)]) # Boi vi write_csv can ma tran 2D nen phai them 1 lop dummy vao
    return output
