#if cart items >5 then 10% discount
#10 % d1scount if total value is b/w 20k and 50 k and 15% if total >50k
#calculate sum where price>25000

def cal_total1(cart):
    total=sum(cart.values())
    if(len(cart)>5):
        total*=0.9
    return total
def cal_total2(cart):
    total=sum(cart.values())
    if(total>20000 and total<50000):
        total*=0.9
    elif(total>50000):
        total*=0.85
    return total

def cal_total3(cart):
    total=0
    for v in cart.values():
        if v>25000:
            total+=int(v)
    return total

cart={'laptop':50000,'Headphones':2000,'Mouse':35000,'Keyboard':55000,'Monitor':8000,'YDB Crive':1000}
print("case 1 :",cal_total1(cart))
print("case 2:",cal_total2(cart))
print("case 3:",cal_total3(cart))