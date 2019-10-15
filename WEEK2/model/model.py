import csv

def readData(path) :
    
    body=[]
    
    with open(path,"r") as rf:
        reader = csv.reader(rf)
        header = next(reader)

        for row in reader :
            body.append(row)

    return body

def writeData(path,data) :
    
    readData(path)
    header=["id","bookname","author","isbn"]
    with open("data/book.csv","w",newline="") as wf:
        writer = csv.writer(wf)
        writer.writerow(header)
        writer.writerows(data)
