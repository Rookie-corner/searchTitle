import re

f = open("./demo.txt",mode="r", encoding="utf-8")
content = f.read()
f.close()


start = content.find(')')     #开始截取位置
print('start',start)

content = re.sub('浙ICP备05019169号',"",content)

pattern = re.compile(r'\d+')
lastNum = pattern.findall(content).pop(-1)
print('lastNum',lastNum)
end = content.rindex(lastNum)
print('end',end)
content = content[start:end]   #末尾截取位置

# print(content)
content = re.sub(r'[^\u4e00-\u9fa5\u9fa6-\u9fef]+', "",content)
content = re.sub(r'\u672a\u5206\u7c7b',"",content)
print('',content)
# content = re.sub(r'\n', "",content)
# content = content.split(',')
em = ''
i=''
# for a in content:
#     a='"'+a+'"'+':'+'"",\n'
#     print(a)
#     em+=a
# print(content.encode("unicode_escape"))
for a in content:
    i = str(a.encode("unicode_escape"))
    i=i.replace("b'\\"," ")
    em+=i
# print(em)
content = re.sub(r"[' ]", "",em)
fo = open("./hah.txt", "w")
# fo.write(content.encode('utf-8'))
fo.write(content)
fo.close()




