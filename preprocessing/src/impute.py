import argparse
import utilities


def main():
    parser = argparse.ArgumentParser(description='fill in missing value')
    method = {'mean' : utilities.calMean, 'median': utilities.calMedian,'mode':utilities.calMode}
    parser.add_argument('path', metavar='path', type=str, nargs='?',default="",help='path to processing file') 
    # xem page sau để hiểu rõ hơn https://realpython.com/python-main-function/
    parser.add_argument('--method', metavar='method', type=str, nargs='?',default="mean",help='find the alternative for missing values (default: using mean)')
    parser.add_argument('--columns', metavar='columnNames', type=str, nargs='*',default='all',help='choose the column that you want to perform on (default: peform on all columns )')
    parser.add_argument('--out', metavar='outputFile', type=str, nargs='?',default="impute.csv",help='output file name (default: impute.csv)')
    args = parser.parse_args()
    if(args.path == ""):
        print("name of the file is mandatory")
        return;
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
        f = method[args.method]
        fillInVal = f(db,i)
        for j in range(0,len(db[i])):
            if(utilities.isMissing(db[i][j])):
                db[i][j] = fillInVal
    utilities.write_csv(args.out,db,headers=features)
            
        
    
     

if __name__ == "__main__":
    main()

