dict_test={
    "张三":{
        "语文":99,
        "数学":88,
        "英语":77
    },
    "李四":{
        "语文":99,
        "数学":88,
        "英语":77
    },
    "王五":{
        "语文":98,
        "数学":88,
        "英语":77
    }
}
score=dict_test["张三"]["语文"]

print(f"张三的语文分数为：{score}")

dict_test["小明"]={"语文":69,
        "数学":88,
        "英语":77
                   }
score=dict_test["小明"]["语文"]

print(f"小明的语文分数为：{score}")

# keys
keys=dict_test.keys()

# 方式1：通过获取到全部的key来完成遍历
# for key in keys:
#     print(f"字典的key是{key}")
#     print(f"字典的value是{dict_test[key]}")

# 方式2： 直接对字典进行for循环，每一次循环都是直接得到key
for i in dict_test:
    print(f"字典的key是{i}")
    print(f"字典的value是{dict_test[i]}")