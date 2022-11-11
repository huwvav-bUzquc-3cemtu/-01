import PyPDF2
import random
count = 0
def getRandom(randomlength=16):
  """
  生成一个指定长度的随机字符串
  """
  digits = '0123456789'
  ascii_letters='abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  str_list =[random.choice(digits +ascii_letters) for i in range(randomlength)]
  random_str =''.join(str_list)
  return random_str
def text_create(name, msg):
    desktop_path = "/Users/wangzhiyi/Desktop/pywork/加解密/加密/加密文件/"  # 新创建的txt文件的存放路径
    full_path = desktop_path + name + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    file.write(msg)   #msg也就是下面的Hello world!
    # file.close()
 

f1 = input("filepath: ")
print(f1)
f2 = input("name: ")
print(f2)
reader1=PyPDF2.PdfReader(f'{f1}')
#<PyPDF2._reader.PdfReader object at 0x0000018715058FD0>
#2、创建一个空白的PDF写方法
my_key = getRandom(1024)
print(my_key)
text_create(f'{f2}', f'{my_key}')
#记录密码

writer1=PyPDF2.PdfWriter()
#3、获取原来文件的总页数
pages=reader1.getNumPages()
for i in range(pages):#循环遍历每一页
    writer1.addPage(reader1.pages[i])#将每一页添加到空白pdf中
writer1.encrypt(f'{my_key}')#加密
f=open("/Users/wangzhiyi/Desktop/pywork/加解密/加密/加密文件/"+f'{f2}'+'.pdf','wb') #
writer1.write(f)
f.close()

