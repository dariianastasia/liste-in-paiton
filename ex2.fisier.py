x=[-5,5,-4,4,-3,3,-2,2,-1,1]
print(x) #lista initiala
x=sorted(x)
print(x) # lista sortata crescator
x.sort(reverse=True)
print(x) #lista sortata descrescator
print(len(x)) #nr. de elemente in lista
print(max(x)) #valoarea maximala
print(min(x))  # valoarea minimala
x.exted(111) 
print(x) # inserasea nr. la coada listei
x.inset (2,-222) # inserarea nr. pe locul al 2 din lista
print(x)
with open('output.txt','w') as f:
    f.write[(str(x))]