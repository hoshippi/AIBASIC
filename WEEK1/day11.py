
# print("Hello World")

# name = input("What is your name :")

# print ("Hi " + name + ". How are you?" )



# num1 = int(input( "please input the number 1 : "))
# num2 = int(input( "please input the number 2 : "))

# print( num1 + num2)

# list
# tuple
# dictionaly


my_list = [1,2,3,4,5]
print(my_list [:-3])
print()

#末尾に追加したいとき
my_list.append(7)
print(my_list)
print()

#配列内の所定の場所に追加したいとき
my_list.insert(1,8)
print(my_list)
print()

#配列内の任意のモノを" index "を指定して消したいとき
my_list.pop(2)
print(my_list)
print()

#配列内の任意のものを" value "を指定して消したいとき

my_list.remove(5)
print(my_list)
print()

#配列を完全消去する
my_list.clear()
print(my_list)
print()

print("tuple")
print()
print()

my_tuple = ( 1,2,3,4,5 )

print(my_tuple[2])

#探してboolean値を返す
print(4 in my_tuple)



print("dictionaly")
print()
print()

my_dictionaly = {"name":"Jan", "age":25, "address": "Cebu"}

print(my_dictionaly["name"])


list_dictionary = [
    {"name":"Jan", "age":25, "address": "Cebu"},
    {"name":"Taka", "age":23, "address": "Kanagawa"},
    {"name":"Hiro", "age":22, "address": "Tokyo"} 
]

print(list_dictionary)
print(list_dictionary[1]["name"])
