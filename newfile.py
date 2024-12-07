#filehandling in python
f=open('demoAarjan.txt','r')
#print(f.read())
#print(f.readline())
#print(f.readline())
#print(f.readline())
#using a for loop to read a File
for x in f:
    print(x)
f.close()
#opening file using append mode
f=open('demoAarjan.txt','a')
f.write('today is saturday the 7th')
f=open('demoAarjan.txt','w')
f.write('the data has been erased')
f.write('the file has new content')
f.close()
f=open('demoAarjan.txt','w')
f.write('today is the 7th of december')
print(f.readline())