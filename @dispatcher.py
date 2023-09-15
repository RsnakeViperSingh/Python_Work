from multipledispatch import dispatch 
@dispatch(int,int)
def product (first,second) :
    result = first*second
    print(result);
    
    