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

def format_duration(seconds):
    y=0
    d=0
    h=0
    m=0
    s=0
    rep=""
    while seconds>=31536000:
        seconds=seconds-31536000
        y=y+1
    if y!=0:
        if y>1:
            years=" years "
        else:
            years=" year "    
        rep=rep+ (str(y) + years)    
    while seconds>=86400:
        seconds=seconds-86400
        d=d+1
    if d!=0:
        if d>1:
            days=" days "
        else:
            days=" day "    
        rep=rep+ (str(d) + days)      
    while seconds>=3600:
        seconds=seconds-3600
        h=h+1
    if h!=0:
        if h>1:
            hours=" hours "
        else:
            hours=" hour "    
        rep=rep+ (str(h) + hours)         
    while seconds>=60:
        seconds=seconds-60
        m=m+1
    if m!=0:
        if m>1:
            minutes=" minutes"
        else:
            minutes=" minute"    
        rep=rep+ (str(m) + minutes)        
    s=seconds
    if s!=0:
        if s>1:
            scd=" seconds"
        else:
            scd=" second"
        if m>0:
            rep=rep+" and "        
        rep=rep+ (str(s) + scd)  
    if rep=="":
        return "now"
    else:
        return(rep)

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
    
def expression_matter(a, b, c):
    prem=a*(b+c)
    deuz=a*b*c
    treuz=a+b*c
    qtr=(a+b)*c
    cnq=a+b+c
    return max(prem,deuz,treuz,qtr,cnq)

def array_diff(a, b):        
    return [c for c in a if c not in b]

def switch_it_up(number):
    match number:
        case 1:return "One"
        case 2:return "Two"
        case 3:return "Three"
        case 4:return "Four"
        case 5:return "Five"
        case 6:return "Six"
        case 7:return "Seven"
        case 8:return "Eight"
        case 9:return "Nine"
        case 0:return "Zero"

def capitals(word):
    i=0
    a=[]
    for c in word:
        if c.isupper()==True:
            a.append(i)
        i=i+1
    return a

def binary_array_to_number(arr):
    a=""
    for c in arr:
        a=a+str(c)
    return int(a,2)

def add_length(str_):
    a=str_.split(" ")
    b=[]
    for c in a:
        b.append(c+" "+str(len(c)))   
    return b

def factorial(n):
    fact=1
    if n>=0 and n<=12:
        for i in range(1,n+1):
            fact*=i
    else:
        raise ValueError
    return fact

def repeat_str(repeat, string):
    a=(print(repeat*string))
    a=str(a)
    return a

def reverse_seq(n):
    a=[]
    for i in range(1,n+1):
        a.append(i)
    return a[::-1]

def validate_pin(pin):
    if len(pin)==4 or len(pin)==6:
        return pin.isdigit()
    else:
        return False

def row_sum_odd_numbers(n):
        return n**3

def calcul():
    def zero(truc=None): return 0 if not truc else truc(0)
    def one(truc=None): return 1 if not truc else truc(1)
    def two(truc=None): return 2 if not truc else truc(2)
    def three(truc=None): return 3 if not truc else truc(3)
    def four(truc=None): return 4 if not truc else truc(4)
    def five(truc=None): return 5 if not truc else truc(5)
    def six(truc=None): return 6 if not truc else truc(6)
    def seven(truc=None): return 7 if not truc else truc(7)
    def eight(truc=None): return 8 if not truc else truc(8)
    def nine(truc=None): return 9 if not truc else truc(9)
    def plus(n): return  lambda i:i+n
    def minus(n): return lambda i:i-n
    def times(n): return lambda i:i*n
    def divided_by(n): return lambda i:i//n

def chromosome_check(chromosome):
    a=0
    for c in chromosome:
        if c=="Y":
            a=a+1
    if a==0:
        return "Congratulations! You\'re going to have a daughter."
    else:
        return "Congratulations! You\'re going to have a son."

def maps(a):
    b=[]
    for c in a:
        c=c*2
        b.append(c)
    return b

def count_smileys(arr):
    w=0
    for b in arr:
        for dex,c in enumerate(b):
            a=dex
            if c==")"or c=="D":
                i=b[a-1]
                if i=="-"or i=="~":
                    i=b[a-2]
                    if i==";"or i==":":
                        w=w+1 
                elif i==";"or i==":":
                    w=w+1
    return w

def reverse(st):
    a=st.split(" ")
    a.reverse()
    return " ".join(a)