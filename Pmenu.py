#menu
#9\11\22
veg=["Rice",'cheese','butter','daal','roti','curd']
nveg=['egg','biriyani','chicken']
snack=['burger','pizza','sandwich']
soft=['cola','pepsi','mojito']
vp=[100,100,65,120,10,12]
np=[50,150,100]
snp=[25,80,60]
sp=[20,20,80]
for x in range(len(veg)):
    veg[x]=veg[x].upper()
for x in range(len(nveg)):
    nveg[x]=nveg[x].upper()
for x in range(len(snack)):
    snack[x]=snack[x].upper()
for x in range(len(soft)):
    soft[x]=soft[x].upper()
print(veg)
print(nveg)
print(snack)
print(soft)
n1=int(input("Enter the number of veg items= "))
if len(veg)>n1:
    print("Total veg items are : ",len(veg))
    n1=int(input("Enter no. of veg items = "))
n2=int(input("Enter the number of non veg items= "))
if len(veg)>n2:
    print("Total non veg items are : ",len(nveg))
    n2=int(input("Enter no. of non veg items = "))
n3=int(input("Enter the number of snack items= "))
if len(veg)>n3:
    print("Total snack items are : ",len(snack))
    n3=int(input("Enter no. of snack items = "))
n4=int(input("Enter the number of soft drink items= "))
if len(veg)>n4:
    print("Total soft drink items are : ",len(soft))
    n1=int(input("Enter no. of soft drink items = "))
ordered_items={}
for x in range(n1):
    i=str(input("Enter veg item = "))
    i=i.upper()
    Q=int(input("Enter quantity : "))
    for y in range(len(veg)):
        if i==veg[y]:
            ordered_items.update({i:vp[y]*Q})
for x in range(n2):
    i=str(input("Enter non veg item = "))
    i=i.upper()
    Q=int(input("Enter quantity : "))
    for y in range(len(veg)):
        if i==veg[y]:
            ordered_items.update({i:vp[y]*Q})
for x in range(n3):
    i=str(input("Enter snack item = "))
    i=i.upper()
    Q=int(input("Enter quantity : "))
    for y in range(len(veg)):
        if i==veg[y]:
            ordered_items.update({i:vp[y]*Q})
for x in range(n4):
    i=str(input("Enter soft drink item = "))
    i=i.upper()
    Q=int(input("Enter quantity : "))
    for y in range(len(veg)):
        if i==veg[y]:
            ordered_items.update({i:vp[y]*Q})
print(ordered_items)
gst=0.18
bill=0 
for x in ordered_items:
    bill=bill+ordered_items[x]
total_bill=bill+(bill*gst)
print("Bill Slip")
print("Dish name",":","price")
for x in ordered_items:
    print(x,":",ordered_items[x])
print("Total Bill",":",total_bill)


