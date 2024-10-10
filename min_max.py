def min_max(lst):
    a=b=lst[0]
    for c in lst:
        if a>=c:
            a=c
        if b<=c:
            b=c
    return [a,b]

def str_count(strng, letter):
    a=0
    for c in strng:
        if c==letter:
            a=a+1
    return a    

def human_years_cat_years_dog_years(human_years):
    
    if human_years>2:
        cat=15+9+4*(human_years-2)
        dog=15+9+5*(human_years-2)
    elif human_years==2:
        cat=15+9
        dog=15+9
    else:
        cat=15
        dog=15

    return [human_years,cat,dog]


def check_for_factor(base, factor):
    if base%factor==0:
        return True
    else:
        return False
    
    
def square(n):
    return n*n  

def nb_dig(n, d):
    b=0
    for i in range (0,n+1):
        a=i*i
        for c in str(a):
            if c==str(d):
                b=b+1
    
    return b

# def format_duration(seconds):
#     y=0
#     d=0
#     h=0
#     m=0
#     s=0
#     rep=""
#     while seconds>=31536000:
#         seconds=seconds-31536000
#         y=y+1
#     if y!=0:
#         if y>1:
#             years=" years "
#         else:
#             years=" year "    
#         rep=rep+ (str(y) + years)    
#     while seconds>=86400:
#         seconds=seconds-86400
#         d=d+1
#     if d!=0:
#         if d>1:
#             days=" days "
#         else:
#             days=" day "    
#         rep=rep+ (str(d) + days)      
#     while seconds>=3600:
#         seconds=seconds-3600
#         h=h+1
#     if h!=0:
#         if h>1:
#             hours=" hours "
#         else:
#             hours=" hour "    
#         rep=rep+ (str(h) + hours)         
#     while seconds>=60:
#         seconds=seconds-60
#         m=m+1
#     if m!=0:
#         if m>1:
#             minutes=" minutes"
#         else:
#             minutes=" minute"    
#         rep=rep+ (str(m) + minutes)        
#     s=seconds
#     if s!=0:
#         if s>1:
#             scd=" seconds"
#         else:
#             scd=" second"
#         if m>0:
#             rep=rep+" and "        
#         rep=rep+ (str(s) + scd)  
#     if rep=="":
#         return "now"
#     else:
#         return(rep)



def find_smallest_int(arr):
    a=arr[0]
    for c in arr:
        if c<a:
            a=c
    return a

def update_light(current):
    if current=="Red":
        return "Green"
    elif current=="Green":
        return"Orange"
    elif current=="Orange":
        return"Red"
    # Your code here.
    
    
def expression_matter(a, b, c):
    prem=a*(b+c)
    deuz=a*b*c
    treuz=a+b*c
    qtr=(a+b)*c
    cnq=a+b+c
    return max(prem,deuz,treuz,qtr,cnq)

def array_diff(a, b):        
    return [c for c in a if c not in b]