import argparse
import utilities


def main():
    parser = argparse.ArgumentParser(description='feature scaling')
    method = {'z-score' : utilities.standardization, 'min-max': utilities.min_maxScale}
    parser.add_argument('path', metavar='path', type=str, nargs='?',default="",help='path to processing file') 
    # xem page sau để hiểu rõ hơn https://realpython.com/python-main-function/
    parser.add_argument('--method', metavar='method', type=str, nargs='?',default="z-score",help='way to normalization a feature (default: using z-score)')
    parser.add_argument('--columns', metavar='columnNames', type=str, nargs='*',default='all',help='choose the column that you want to perform on (default: peform on all columns )')
    parser.add_argument('--out', metavar='outputFile', type=str, nargs='?',default="scaling.csv",help='output file name (default: scaling.csv)')
    args = parser.parse_args()
    if(args.path == ""):
        print("file name is mandatory")
        return
    db, features = utilities.read_csv(args.path,isHeader=True,getFeatures=True)
    retainFeatures = args.columns
    if type(retainFeatures) != str:
        i= 0
        while i < len(features):
            if features[i] not in retainFeatures:
                utilities.deleteColumn(db,i)
                del features[i]
                continue
            i += 1
    for i in range(0, len(features)):
        arguments = [0,0]
        if args.method == 'z-score':
            arguments[0] = utilities.calMean(db,i)
            arguments[1] = utilities.calStd(db,i,arguments[0])
            if(arguments[1] == 0):
                continue
        elif args.method == 'min-max':
            arguments[0], arguments[1] = utilities.findMinMax(db,i) # tra lan luot min max
            if(arguments == [0,0]):
                continue
        utilities.normalization(db,i,method[args.method],arguments[0],arguments[1])
    
    utilities.write_csv(args.out,db,headers=features)
            
        
    
     

if __name__ == "__main__":
    main()

