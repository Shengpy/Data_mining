import argparse
import utilities


def main():
    parser = argparse.ArgumentParser(description='feature scaling')
    method = {'addition' : utilities.addition,'subtraction':utilities.subtraction,'multiplication':utilities.multiplication,'division':utilities.division}
    parser.add_argument('path', metavar='path', type=str, nargs='?',default="",help='path to processing file') 
    parser.add_argument('columnA', metavar='columnA', type=str, nargs='?',default="",help='first operator column') 
    parser.add_argument('columnB', metavar='columnB', type=str, nargs='?',default="",help='second operator column') 
    # xem page sau để hiểu rõ hơn https://realpython.com/python-main-function/
    parser.add_argument('--operation', metavar='operation', type=str, nargs='?',default="addition",help='operation will be perform on a given column (default: using addition else subtraction, division , multiplication)')
    parser.add_argument('--out', metavar='outputFile', type=str, nargs='?',default="columnWise.csv",help='output file name (default: columnWise.csv)')
    args = parser.parse_args()
    if(args.path == ""):
        print("path of the file is mandatory ")
        return
    db, features = utilities.read_csv(args.path,isHeader=True,getFeatures=True)
    retainFeatures = [args.columnA, args.columnB]
    for i in range(0, len(retainFeatures)):
        if(retainFeatures[i] == ''):
            print("name of column A and B is mandatory ")
            return
    index= 0
    while index < len(features):
        if features[index] not in retainFeatures:
            utilities.deleteColumn(db,index)
            del features[index]
            continue
        index += 1
    for i in range(0, len(features)):
        if(utilities.isNumeric(db,i) == False):
            print("column A and B must have numeric value ")
            return
    result = utilities.columnWise(db,0,1,method[args.operation])
    utilities.write_csv(args.out,result,headers=[f'{args.operation} of {args.columnA} and {args.columnB} '])
            
        
    
     

if __name__ == "__main__":
    main()

