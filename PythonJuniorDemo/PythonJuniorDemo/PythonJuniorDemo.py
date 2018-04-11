print("hello python")
print('hello python')
print("i said ,\"hello,'python'\"")#单引号双引号可以嵌套使用，转义符同样生效
print('i said "hello python"')
print(""" i said,
hello 
python""")
print("i\nsaid\nhello\npython")
print("""i\nsaid\nhello\npython""")#即使是用三个引号的方式，转移符 依然在字符串中生效
print("i said,%s" % ("hello python"))
#print("i said,%s"("hello")) #这句会报错 % 不可以掉
print(10 / 5)
print(type(10 / 5))
print(10.2 % 3)
print(10 % 3)
testStr = "this is a %s" % "testStr"
print(testStr)
tupleVar = ("12",234,"23")#元组测试
print(tupleVar)
print("%s%s%s" % tupleVar)
print("len is %d,the last one is %s" % (len(tupleVar),tupleVar[len(tupleVar) - 1]))
single_element_tuple = ("the sole element",)#空元组在创建的时候，需要多加一个逗号，不然会和被当成一个字符串
try:
    tupleVar[0] = "change"
except Exception as err:
    print("发生了异常：%s" % err)#元组是不能更改的
listVar = ["i","am" ,1,"man"]#列表其他语法差不多，但是列表可以修改
print(listVar[0])
listVar[0] = "you"
print(listVar[0])
try:
    listVar[len(listVar)] = "asd"
except Exception as err :
    print(err)
listVar.append("!")
print(listVar)
listVar.extend(listVar)
print(listVar)
dictVar = {}#字典:键值对
dictVar["1th"] = "1"
dictVar["2nd"] = "2"
dictVar["3rd"] = "3"
print(dictVar)
print(dictVar.keys())
print(dictVar.values())
print(list(dictVar.keys()))
print(list(dictVar.values()))
try:
    print(dictVar[0:2])
except Exception as er :
    print(er)#元组和列表、字符串是序列，能够分片（slice），而字典不能
strVar = "123456"
try:
    strVar[0]="0"    
except Exception as er:
    print(er)#字符串是不能更改的
print(strVar[3:5]) #结果45，[a:b] 从小标a开始截到下表为b之前
print(strVar[3:3]) #如果a>=b 不会报错，返回空字符串
print(strVar[-5:3])#结果23，相当于[1:3]
print(strVar[-5:-2])#结果234，相当于[1:4]
print(strVar[-2:3])#结果空字符串，相当于[4:3]
listVar = ["a","a","b","b","c"]
print(listVar.pop())#列表有下标，不传时，默认为-1，及返回并删除最后一个元素
set_var = set(listVar)
print(listVar)
print(set_var)#集合，和字典一样的key一样，{}标志，且不可重复，可以用来快速去重
set_var.add('adf')
print(set_var)
print(set_var.pop())#集合自己没有下标的概念,不能传下标，执行时返回并删除第一个元素
print((list(set_var))[1])

