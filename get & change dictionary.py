import codecs, os, sys


# os.getcwd() # to get the current path
# print ("current path:", os.getcwd())



# os.chdir("D:\\ruby")
# print ("new path:", os.getcwd())


# with codecs.open("123.txt", 'r', 'utf-8') as file:
# 	print (file.read())




# for d in os.listdir("./"):
# 	if os.path.isdir(d):
# 		print (d, ", 當前資料夾是資料夾")
# 	else:
# 		print (d, ", 當前資料夾不是資料夾")


# print (os.path.exists("C:\\Users\\user\\Desktop\\test"))
# print (os.path.exists("C:\\123\\abc"))




# print (os.path.basename("C:\\Users\\user\\Desktop\\test\\listdir.py"))
# print (os.path.dirname("C:\\Users\\user\\Desktop\\test\\listdir.py"))



# print (os.path.getsize("C:\\Users\\user\\Desktop\\test\\listdir.py"))




# convert the bytes to KB, GB or MB
size = (os.path.getsize("C:\\Users\\user\\Desktop\\1.exe"))
print (size)

t = ["Bytes", "KB", "MB", "GB"]
i = 0


while size >= 1024:
	i+=1 # the unit go to next index
	size/=1024
print (size, t[i])