import json

# 准备列表，列表内每一个元素都是字典，将其转换为JSON
data = [{"name": "张三", "age": 11}, {"name": "李四", "age": 11}, {"name": "王五", "age": 11}]

json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)

# 准备字典，将字典转换为JSON
data1 = {"name": "张三", "age": 11}
json_d = json.dumps(data1, ensure_ascii=False)
print(type(json_d))
print(json_d)

# 将JSON字符串转换为Python数据类型
s = '[{"name": "张三", "age": 11}, {"name": "李四", "age": 11}, {"name": "王五", "age": 11}]'
l = json.loads(s)
print(type(l))
print(l)
