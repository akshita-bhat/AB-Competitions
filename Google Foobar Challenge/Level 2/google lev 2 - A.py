l1 = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
l2 = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
import numpy

def normalise(x):
    a = []
    if len(x.split('.'))== 3:
        a.append(int(x.split('.')[0]))
        a.append(int(x.split('.')[1]))
        a.append(int(x.split('.')[2]))
    elif len(x.split('.')) == 2:
        a.append(int(x.split('.')[0]))
        a.append(int(x.split('.')[1]))
        a.append(-1)
    elif len(x.split('.')) == 1:
        a.append(int(x.split('.')[0]))
        a.append(-1)
        a.append(-1)
    return a

x = []
for i in l2:
    x.append(normalise(i))
y=numpy.array([numpy.array(xi) for xi in x])    
z = y[numpy.lexsort((y[:,2], y[:,1], y[:,0]))]

def unnormalise(element):
    tem = str(element[0])
    if element[1] != -1 and element[2] != -1:
        tem+= '.' + str(element[1]) + '.' + str(element[2])
    if element[1] != -1 and element[2] == -1:
        tem+='.'+ str(element[1])
    else:
        tem+=''
    return tem
    

for i in z:
    print(unnormalise(list(i)))    
        

