import os


# print (os.listdir("../"))

# print ("-------------------------")
# for d in os.listdir("./"):
# 	print (d)



d = "/" # indicates top folder
while True:
	f = os.listdir(d)
	for p in range(1, len(f)): # count the all files in the folder from 0
		print (p, f[p])
	r = input("\n請問你要觀看的資料夾:") # str format
	d+=f[int(r)]+"/" # new path, the end of path must be "/"