import pickle

f=open("writedata.txt","rb")

file=pickle.load(f)
print(file)