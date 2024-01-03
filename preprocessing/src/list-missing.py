import argparse
import utilities


def main():
    parser = argparse.ArgumentParser(description='Extract columns with missing value')
    parser.add_argument('path', metavar='path', type=str, nargs='?',default="",help='path to processing file') 
    parser.add_argument('--out', metavar='outputFile', type=str, nargs='?',default="list_missing.csv",help='output file name (default: list_missing.csv)')
    # xem page sau để hiểu rõ hơn https://realpython.com/python-main-function/
    args = parser.parse_args()
    if(args.path == ""):
        print("name of the file is mandatory")
        return;
    db, features = utilities.read_csv(args.path,isHeader=True,getFeatures=True)
    retainIndex = []
    for i in range(0,len(db[0])):
        flag = 0;
        for j in range(0,len(db)):
            if utilities.isMissing(db[j][i]) == True:
                flag += 1
                break
        if flag == 1:
            retainIndex.append(i)
    counter = 0
    for i in range(0,len(db[0])):
        if(i not in retainIndex):
            utilities.deleteColumn(db,i - counter) # Mỗi lần xóa thì giảm 1 cột nên phải trừ vào
            del features[i - counter]
            counter += 1
    utilities.write_csv(args.out,db,headers=features)
    
        
    
     

if __name__ == "__main__":
    main()

