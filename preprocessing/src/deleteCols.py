import argparse
import utilities


def main():
    parser = argparse.ArgumentParser(description='delete missing column if exceed a certain threshold')
    parser.add_argument('path', metavar='path', type=str, nargs='?',default="",help='path to processing file') 
    parser.add_argument('--threshold', metavar='threshold', type=float, nargs='?',default=0.5,help='threshold to delete a given column (default 0.5)') 
    parser.add_argument('--out', metavar='outputFile', type=str, nargs='?',default="deleteCol.csv",help='output file name (default: deleteCol.csv)')
    # xem page sau để hiểu rõ hơn https://realpython.com/python-main-function/
    args = parser.parse_args()
    if(args.path == ""):
        print("file name is mandatory")
        return;
    db,features = utilities.read_csv(args.path,isHeader=True,getFeatures=True);
    deleteCol = 0
    for i in range(0,len(db[0])):
        counterMissing = 0
        for j in range(0,len(db)):
            if utilities.isMissing(db[j][i - deleteCol]) == True:
                counterMissing += 1
            if (counterMissing / len(db)) >= args.threshold:
                utilities.deleteColumn(db,i - deleteCol)
                del features[i - deleteCol]
                deleteCol += 1
                break
    utilities.write_csv(args.out,db,headers=features)
    
    
        
    
     

if __name__ == "__main__":
    main()

