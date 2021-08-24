from math import *
a=[[0,0,0]]
vectorA=input("Enter vector A:\n")
a.append(vectorA.split())
vectorB=input("Enter vector B:\n")
a.append(vectorB.split())
#VectorAddition
val_1=int(a[1][0])
val_2=int(a[1][1])
val_3=int(a[1][2])
val_4=int(a[2][0])
val_5=int(a[2][1])
val_6=int(a[2][2])
AddOutput1=val_1+val_4
AddOutput2=val_2+val_5
AddOutput3=val_3+val_6
OutputAddString="A+B = ["+str(AddOutput1)+", "+str(AddOutput2)+", "+str(AddOutput3)+"]"
print(OutputAddString)
MultiVec=(val_1*val_4)+(val_2*val_5)+(val_3*val_6)
OutputMultiString="A.B = "+str(MultiVec)
print(OutputMultiString)
NormA=round(sqrt(pow(val_1,2)+pow(val_2,2)+pow(val_3,2)),2)
NormB=round(sqrt(pow(val_4,2)+pow(val_5,2)+pow(val_6,2)),2)
OutputNormA="|A| = "+str(NormA)
print(OutputNormA)
OutputNormB="|B| = "+str(NormB)
print(OutputNormB)