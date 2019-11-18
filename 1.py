import csv
def loadcsv(filename):
    lines=csv.reader(open(filename,"rt"))
    dataset=list(lines)
    return dataset
attributes=['sky','temp','humidity','wind','water','forecast']
print('attributes=',attributes)
num_attributes=len(attributes)
print(num_attributes)
filename="finds.csv"
dataset=loadcsv(filename)
print(dataset)
hypothesis=['0']*num_attributes
print("initial hypothesis")
print(hypothesis)
print("the hypothesis are")
for i in range(len(dataset)):
    target=dataset[i][-1]
    if(target=='yes'):
        for j in range(num_attributes):
            if(hypothesis[j]=='0'):
                hypothesis[j]=dataset[i][j]
            if(hypothesis[j]!=dataset[i][j]):
                    hypothesis[j]='?'
    print(i+1,'=',hypothesis)
print("final hypothesis")
print(hypothesis)
