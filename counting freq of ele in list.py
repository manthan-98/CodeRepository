PyList=["Big Data", "Hadoop", "Spark", "IoT", "Hadoop"]
print(PyList.count("Hadoop"))
dic = {}
for i in PyList:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(dic)
for key, value in dic.items():
    print(f'{key} = {value}')