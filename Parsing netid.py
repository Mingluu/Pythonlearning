** Create a function that grabs the NETID  from a email in the form **

    netid@utdallas.edu
    
**So for example, passing "hsd10566@utdallas.edu" would return: abc100000**

def domainGet(x):
    return x[:-13]
    
def domain(email):
return email.split('@')[0]

domainGet('abc100000@utdallas.edu')

domain('abc100000@utdallas.edu')
