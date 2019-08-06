"""

Given a string b and an array of smaller strings T, write a method to search b for each small string in T. 

e.g 
    T = "mejameloganjimaksjsk"
    strings = ["me","jamie","jamielogan","sjsk","vv"]
    
    result = {"me":[0,4],"jamie":[2],"jemielogan":[2],
              "sjks":[17]}
"""

def search(strings, T):
    result = {} 
    for item in strings:
        for i in range(len(T)):
            if T[i] == item[0] and check_Match(T, i, item) == True:
                if item not in result:
                    result[item] = [i]
                else:
                    result[item].append(i)
                    
    return result

# def check_Match(T,i,item):
#     #::check that you have enough to compare 
#     if len(T) - i + 1 >= len(item):
#         n = len(item) 
#         substring = T[i:n+i]
#         return substring == item 
#     return False 

def check_Match(T, i, item):
    n = len(item)
    
    extract, status = extractable(T, i , n)
    # while status == True:
    for k in range(len(extract)):
        if extract[k] != item[k]:
            return False                    
    return status

def extractable(T, i, n):
    extract = ""
    if len(T[i:]) < n:
        return [], False 
    
    for k in range(i, n+i):
        extract += T[k]
    return extract, True
        
        
                
          
        
#     match = True
    
#     while match == True and j < n: 
#         for k in range(i, n):
#             if T[k] == item[j]:
#                 j +=1
#             else:
#                 match = False
#     return match


          
        
def test():
    T = "mejameloganjimaksjsk"
    strings = ["me","jame","jamielogan","sjsk","vv"]
    print(search(strings, T))
    
test()
    
