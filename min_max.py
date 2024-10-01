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
