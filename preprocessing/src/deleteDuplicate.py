import argparse
import utilities


def main():
    parser = argparse.ArgumentParser(description='delete duplicate row')
    parser.add_argument('path', metavar='path', type=str, nargs='?',default="",help='path to processing file') 
    parser.add_argument('--out', metavar='outputFile', type=str, nargs='?',default="deleteDuplicate.csv",help='output file name (default: deleteDuplicate.csv)')
    map = {}
    # xem page sau để hiểu rõ hơn https://realpython.com/python-main-function/
    args = parser.parse_args()
    if(args.path == ""):
        print("file name is mandatory")
        return;
    db,features = utilities.read_csv(args.path,isHeader=True,getFeatures=True);
    i = 0
    while i < len(db):
        if(map.get(tuple(db[i]),-1) != -1):
            utilities.deleteRow(db,i)
            i -= 1
        else:
            map[tuple(db[i])] = 0
        i += 1
    utilities.write_csv(args.out,db,headers=features)
    
        
    
     

if __name__ == "__main__":
    main()

