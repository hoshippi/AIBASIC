# import math as mt
# #mathはpythonにデフォルトで入っているモジュール
# import statistics as st

# x = mt.pow(2,3)
# print(x)

# y = [1,2,2,2,3,3,3,3,5,5,5,6,6,6,6,9,9,]

# print(st.median(y))
# print(st.mean(y))

# from model import model

# print(model.module1())


# import csv

# header = []
# body = []

# with open("data/book.csv","r") as rf:
#     reader = csv.reader(rf)
#     #reading the file(csv)
#     header = next(reader)
#     #最初のカラム名＝header（第1行を飛ばしている）を飛ばす作業

#     for row in reader :
#         body.append(row)

# # CSVを開く際、headerはすでに「CSVファイルの1行目」として定義されている。
# print(body)

# name = input("Enter the book Name :")
# author = input("enter the author :")
# isbn = input("enter isbn :")

# body.append([len(body)+1,name,author,isbn])

# with open("data/book.csv","w",newline="") as wf:
#     writer = csv.writer(wf)
#     writer.writerow(header)
#     writer.writerows(body)

# #csvファイルの書き込みでは、元のファイルにすべて上書きしてしまうため、元のデータを保持しない。


from model.model import readData,writeData

path = input("Can you just put the directry of where the file is located")

data = readData(path)
print(data)
data.append([len(data)+1,"Taka's book", "Taka", "123456789"])

writeData(path,data)