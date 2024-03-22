def count(a, b, c):
    result = 0
    for x in range(0,101):
        for y in range(0,101):
            if x*a + y*b <= c:
                result = max(result,(x + y))
                   
    return result
    
if __name__ == "__main__":
    print(count(3, 4, 11)) # 3
    print(count(5, 1, 100)) # 100
    print(count(2, 3, 1)) # 0
    print(count(2, 3, 9)) # 4