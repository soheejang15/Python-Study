f = open("newfile.txt",'r')

# 한 줄 읽기

# line = f.readline()



# 모든 줄 읽기

# readline()
'''while True :
    line = f.readline()
    if not line : break
    print(line)'''

# readlines()
'''lines = f.readlines()
for i in lines :
    print(i)'''

# read()
lines = f.read()
print(lines)

print(line)
f.close()
