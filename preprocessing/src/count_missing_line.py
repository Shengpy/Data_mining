import argparse
import utilities


def main():
    parser = argparse.ArgumentParser(description='Count missing data row')
    parser.add_argument('path', metavar='path', type=str, nargs='?',default="",help='path to processing file') 
    # xem page sau để hiểu rõ hơn https://realpython.com/python-main-function/
    args = parser.parse_args()
    if(args.path == ""):
        print("file name is mandatory")
        return;
    db = utilities.read_csv(args.path,isHeader=True);
    counter = 0;
    for i in range(0, len(db)):
        for j in range(0, len(db[i])):
            if utilities.isMissing(db[i][j]) == True:
                counter += 1;
                break;
    print(counter);
    
        
    
     

if __name__ == "__main__":
    main()

