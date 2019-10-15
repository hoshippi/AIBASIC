"""
# aruithmetics Operator

print(2+3)
print(2-1.0)

# 掛け算においては、文字を指定回数分返す。文字型はString
print( 3 * "3")

# 割り算においては、文字型は常にFloat型になる
print( 3 / 3 )

print(3**3)

# 割り算をした後に、四捨五入された値を返す。
print(10//3)


# ---comparison operator

# #"==, !="など
# １）異なるデータ型では比較はできない
# ２）

# "==="（3つ）はデータ型と数値が一緒なのかどうかを比較する。

x = [1,2,3,4,5]
print( 4 in x )
print(4 not in x)


# --- logical operators
# and or not


name = input( "what is your name? :")
age = input("how old are you? :")

print( "Hi {}  .you are alredy {} ?".format(name, age))

# ↓はPython３から使えるようになったformat関数
print( f"Hi {name} . you are already {age} ?")

# """"""で囲むとその間をすべてコメントアウトできる



# String文字列に対して、index指定をして、特定の文字だけを取り出すことが可能
word = "lorem Ipsum Dolor"
print( word[:5])

# Stringはindexを指定して修正することは不可能
# word[0] = "G" ←　ダメ

print( word.split(" "))



word2 = ["I am", "Taka", "Cebu."]
print(" ".join(word2)) 


word3 = "Lorem Ipsum Dolor"
new_word3 = word3.replace("o","a")
print(new_word3)



# activity using input and if 

age = int(input( "Can I ask your age? :"))

if age < 18 and age >0:
    print("You are underage!")
elif age >= 18 and age <60 :
    print("You are in Legal age")

elif age >= 60 and age < 120 :
    print( "You are in Senior age")
else :
    print( "What you input as age is invalid")




mylist = [1,2,3,4,5,6,7]
count = 20 

for i in range(1,count):
    if i%2 != 0:
        print(f"odd number{i}")
    else :
        print(f"equal number{i}")

students = ["taka", "hiro" , "ayaka"]

for student in students :
    print( student )

for i,student in enumerate(students) :
    print( f"[{i+1}]{student}")


count = 10
while True :
    
    answer = input("input x to break or c to continue ")
    if answer == "c":
        for i in range( 1, count+1)
        continue
    else : 
        print("Stopped")
        break





numbers = [i*2 for i in range(1,10) if i % 2 == 0]
print(numbers)
"""







