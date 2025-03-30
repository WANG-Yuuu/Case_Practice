# 阶乘的计算
def fact(n):
    s=1
    for i in range (1,n+1):
        s *= i
    return s
print(fact(3))

# map函数
'''
map 函数：这是一个高阶函数，基本语法为map(function, iterable, ...) 
function：要应用的函数，可以是内置函数或自定义函数
iterable：一个或多个可迭代对象，如列表、元组等
它的作用是将指定的函数function依次应用到iterable的每个元素上
并返回一个新的迭代器（一般用list()函数转换为列表来查看结果）
'''
nums=[1,2,3,4,5,6,7,8,9]
square = map(lambda x: x**2,nums)
print(list(square))



# filter函数 筛选
'''
filter 函数：可理解为数据筛选器，语法是filter(function, iterable) 
function是筛选规则函数，该函数应返回布尔值
iterable是待筛选的可迭代对象
它会从iterable中筛选出使function返回True的元素，并返回一个新的迭代器（同样常用list()转换查看）
'''
nums=[1,2,3,4,5,6,7,8,9]
evens = filter(lambda x: x % 2==0,nums)
print(list(evens))

# sorted函数
'''
sorted 函数：用于对可迭代对象进行排序，基本语法为sorted(iterable, key=..., reverse=...) 
iterable是需要排序的可迭代对象
key是一个函数，用于指定排序的规则
reverse是一个布尔值，True表示降序，False表示升序（默认值为False）。
'''
words=["apple","banana","cherry","date"]
sorted_words = sorted(words,key = lambda x:len(x),reverse=0)
print(sorted_words)

# 练习：计算并保存股票收益率
import csv
def calculate(open_price,close_price):
    return (float(close_prise)-float(open_price))/float(open_price)
data_list=[]
with open("stock_prices.csv","r",encoding="utf-8")as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        date = row[0]
        open_price = row[1]
        close_prise = row[2]
        change_rate = calculate(open_price,close_prise)
        data_list.append([date,change_rate])
with open ("stock_change","w",encoding="utf-8")as file:
    writer = csv.writer(file)
    writer.writerow(["日期","收益率"])
    for item in data_list:
        writer.writerow(item)