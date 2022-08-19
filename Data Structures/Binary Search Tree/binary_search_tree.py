class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        

class BST:
    def __init__(self):
        self.root = None
        self.queue = list()
        self.left = 0
        self.right = 0
        
    def insert_node(self,root,value):
        if root is None:
            return Node(value)
        else:
            if value < root.value:
                root.left = self.insert_node(root.left,value)
            else:
                root.right = self.insert_node(root.right,value)
            return root
            
    def search_in_tree(self,root_node,value):
        if root_node is None:
            return False
        else:
            if root_node.value == value:
                return True
            elif root_node.value > value:
                return self.search_in_tree(root_node.left,value)
            else:
                return self.search_in_tree(root_node.right,value)
    
    def inorder_traversal(self,root):
        if root is not None:
            self.inorder_traversal(root.left)
            print(root.value)
            self.inorder_traversal(root.right)
        
        
    def preorder_traversal(self,root):
        if root is not None:
            print(root.value)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
            
    def postorder_traversal(self,root):
        if root is not None:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.value)
            
    def level_order_traversal(self,queue):
        if len(queue) > 0:
            node = queue.pop(0)
            print(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            self.level_order_traversal(queue)
            
    def height_of_tree(self,root):
        if root is None:
            return 0
        left = self.height_of_tree(root.left)
        right = self.height_of_tree(root.right)
        return max(left,right)


tree = BST()
root = tree.root
sorted_array = [3,4,5,6,7,8,9]
root = tree.insert_node(root,5)
root = tree.insert_node(root,4)
root = tree.insert_node(root,6)
root = tree.insert_node(root,3)
root = tree.insert_node(root,8)
root = tree.insert_node(root,7)
root = tree.insert_node(root,9)
print("The InOrder Traveral of the tree")
tree.inorder_traversal(root)
print("The PreOrder Traversal of the tree")
tree.preorder_traversal(root)
print("The PostOrder Traversal of the tree")
tree.postorder_traversal(root)
print("The LevelOrder Traversal of the tree")
tree.queue.append(root)
tree.level_order_traversal(tree.queue)
print("The height of the tree: " + str(tree.height_of_tree(root)))
print("The number 6 exists in tree: " if tree.search_in_tree(root,6) else "The number 6 doesn't exist in tree")

# Following is the implementation of construction of BST from given InOrder Traversal

def construct_tree_with_in_order_traversal(sorted_array,root,tree):
    if len(sorted_array) > 1:
        mid = int(0 + (len(sorted_array) - 0) / 2)
        root = tree.insert_node(root,sorted_array[mid])
        left_array = sorted_array[0:mid]
        right_array = sorted_array[mid:len(sorted_array)]
        root = construct_tree_with_in_order_traversal(left_array,root,tree)
        root = construct_tree_with_in_order_traversal(right_array,root,tree)
    return root
    
# calling     
root = construct_tree_with_in_order_traversal(sorted_array,root,tree)
tree.inorder_traversal(root)
