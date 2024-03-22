def count_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1 
    return result
def karkit_1_1(a,b,c):
    result = 0
    for x in range(0,101):
        for y in range(0,101):
            if x*a + y*b <= c:
                result = max(result,(x + y))
                   
    return result
def inversions_1_2(t):
    inversions = []
    for i, value1 in enumerate(t):
        #print(i,value1)
        for j, value2 in enumerate(t):
            if i < j and value1 > value2:
                inversions.append((value1, value2))
    return len(inversions)
                 


        

    

