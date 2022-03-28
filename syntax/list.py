print('==== test list ====')

testList = ['aa', 'bb', 'cc']
testList2 = [11, 22, 33]

# 判斷串列是否為空
if len(testList) != 0:
    print('此串列不為空值')
testList.append("dd")

for element in testList:
    if element.startwith('a'):
        print(f'{element} 此元素開頭是a')
if "cc" in testList:
    # 若搜尋值不存在串列中 會出錯
    testList.index("cc")
    testList.count("cc")
    testList.remove("cc")
testList.insert(2, 'ff')
# 將元素貼在後面
testList.extend(testList2)

# str轉字串串列
teststr = "D:/python/test"
splitList = teststr.split("/")

# 字串串列組成一個字
testPath = ["D:", "tset", 'path']
print("/".join(testPath))
print('==== test list ====')
