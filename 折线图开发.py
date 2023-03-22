import json

f_us=open("./zhexiantu_data/美国.txt","r",encoding="UTF-8")
us_data=f_us.read()
# 去掉不符合JSON规范的开头
us_data=us_data.replace("jsonp_1629344292311_69436(","")
# 去掉不符合JSON规范的结尾
us_data=us_data[:-2]

us_dict=json.loads(us_data)
print(type(us_dict))
print(us_dict)