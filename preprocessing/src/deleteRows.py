import argparse
import utilities


def main():
    parser = argparse.ArgumentParser(description='delete missing row if exceed a certain threshold')
    parser.add_argument('path', metavar='path', type=str, nargs='?',default="",help='path to processing file') 
    parser.add_argument('--threshold', metavar='threshold', type=float, nargs='?',default=0.5,help='threshold to delete a given row (default 0.5)') 
    parser.add_argument('--out', metavar='outputFile', type=str, nargs='?',default="deleteRows.csv",help='output file name (default: deleteRows.csv)')
    # xem page sau để hiểu rõ hơn https://realpython.com/python-main-function/
    args = parser.parse_args()
    if(args.path == ""):
        print("file name is mandatory")
        return;
    db,features = utilities.read_csv(args.path,isHeader=True,getFeatures=True);
    i = 0
    while i < len(db):
        counterMissing = 0
        for j in range(0,len(db[i])):
            if utilities.isMissing(db[i][j]) == True:
                counterMissing += 1
            if (counterMissing / len(db[i])) >= args.threshold:
                utilities.deleteRow(db,i)
                i -= 1
                break
        i += 1
    utilities.write_csv(args.out,db,headers=features)
    
        
    
     

if __name__ == "__main__":
    main()

