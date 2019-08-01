"""
(1) Write a function to check that a binary tree is a valid binary search tree. 
    
    
(2). Write a function to merge our lists of orders into one sorted list.

    For example:

    my_list     = [3, 4, 6, 10, 11, 15]
    alices_list = [1, 5, 8, 12, 14, 19]
    
    answer     = [1,3,4,5,8,6,10,11,12,14,15,19]


insertLeft(node1) 
insertRight(node)

"""

class node:
    def __init__(self, data):
        self.data = data 
        self.leftChild = None 
        self.rightChild = None 
        
    def insertLeft(self, node_obj):
        self.leftChild = node_obj 
        
    def insertRight(self, node_obj):
        self.rightChild = node_obj
        
class BST:
    def __init__(self, root):
        self.root = None
        


# def isBinarySearchTree(root):
#     if root.leftChild:
#         checkQuery1 = _isBinarySearchTree(root, root.data, root.leftChild.data, "left")
   
#     if root.rightChild:
#         checkQuery2 = _isBinarySearchTree(root, root.data, root.rightChild.data, "right")
        
#     if checkQuery1 < root.data and checkQuery2 > root.data:
#         return True 
#     elif checkQuery1 < root.data:
#         return True
#     elif checkQuery2 > root.data:
#         return True
#     else:
#         return False
        
    
# def _isBinarySearchTree(cur_node, data, check, wing):
#     if cur_node.leftChild:
#         if cur_node.leftChild.data < data:
#             _isBinarySearchTree(cur_node.leftChild, cur_node.leftChild.data, check, wing)
#             if wing == "left":
#                 if cur_node.data > check:
#                     check = data
                    
#             else:
#                 if cur_node.data < check:
#                     check = data
            
#         return check

#     if cur_node.rightChild:
#         if cur_node.rightChild.data > data:
#             _isBinarySearchTree(cur_node.rightChild, cur_node.rightChild.data, check, wing)
#             if wing == "left":
#                 if cur_node.data > check:
#                     check = data
                    
#             else:
#                 if cur_node.data < check:
#                     check = data

#         return check
#   10 
 
def _isBinarySearchTree(root): 
    if root is None: 
        return (True,None)   
        
    left_condition,left_max_value   = _isBinarySearchTree(root.leftChild)  # True,None   
    right_condition,right_max_value = _isBinarySearchTree(root.rightChild) # True,None
    
    #:: compare them 
    if left_condition and right_condition:         
        #::
        if (left_max_value is not None and right_max_value is not None ) and root.data > left_max_value and root.data <= right_max_value: 
            #::
            max_value = max([left_max_value,right_max_value,root.data])            
        elif (left_max_value is None and right_max_value is not None) and root.data <= right_max_value:             
            max_value = right_max_value            
        elif (left_max_value is not None and right_max_value is None) and root.data > left_max_value:                    
            max_value = root.data   
        elif (left_max_value is None and right_max_value is None): 
            max_value = root.data 
        else:
            return (False,None) 
        
        return (True,max_value)
    else:
        return (False,None) 

def isBinarySearchTree(root):
    
    result,max_value = _isBinarySearchTree(root) 
    return result


def gen_test_input(arr,root_value): 
    def get_node(value,node_dict):
        if value is None: 
            return None 
        
        if value in node_dict: 
            node_ref = node_dict[value] 
        else:
            node_ref = node(value) 
            node_dict[value] = node_ref             
        return node_ref 
        
    ref_dict = {}
    for item in arr:
        cur_node   = get_node(item[0],ref_dict)
        left_node  = get_node(item[1],ref_dict)
        right_node = get_node(item[2],ref_dict)
        cur_node.insertLeft(left_node)
        cur_node.insertRight(right_node)
        
    root = get_node(root_value,ref_dict)
    return root 



def printTree(root): 
    if root is not None: 
        print(root.data) 
        printTree(root.leftChild)
        printTree(root.rightChild) 
       
def printOut(res,correct,root,testname):
    print("=====================")
    print("Result for {} ".format(testname))    
    print("Your output   : ", res)
    print("Correct output: ",correct)
    print("Tree: =====")
    # print("printing tree")
    printTree(root) 
    print("=====================")
            


def test1():
    arr = [(4,1,5)]
    root = gen_test_input(arr,4)
    #:: add your code here    
    res = isBinarySearchTree(root)
    printOut(res,True,root,"test 1")

    
def test2():
    """
                10
             4      3

    """       
    arr = [(10,4,3)]
    root = gen_test_input(arr,10)     
    res = isBinarySearchTree(root)
    printOut(res,False,root,"test 2")
    
def test3():
    
    """
                10
             4      
           3
    """       
    arr = [(10,4,None),(4,3,None)]
    root = gen_test_input(arr,10) 
    res  = isBinarySearchTree(root)
    printOut(res,True,root,"test 3")
    
def test4():
    """
                10
            5        13 
         4    11    4   15

    """       
    arr = [(10,5,13),(5,4,11),(13,4,15)]
    root = gen_test_input(arr,10)     
    res = isBinarySearchTree(root)
    printOut(res,False,root,"test 4")
    
    
def test5():
    """
                10
            5         13 
         11   6    11   15

    """       
    arr = [(10,5,13),(5,11,6),(13,11,15)]
    root = gen_test_input(arr,10)     
    res = isBinarySearchTree(root)
    printOut(res,False,root,"test 5")    
#insert 

    
test1()
test2() 
test3()
test4()
test5()
