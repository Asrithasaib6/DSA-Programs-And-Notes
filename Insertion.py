class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None 
    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    #preorder is [ root,left , right]
    def preorderIterative(self,root):
        if not root:
            return []
        stack=[root]
        ans=[]
        while stack:
            curr=stack.pop()
            ans.append(curr.data)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return ans  
    #inorder is [left,root,right]
    def InorderIterative(self,root):  
        if not root:
            return []
        stack=[root]
        curr=root
        ans=[]
        while stack:
            if curr.left is None:
                temp=stack.pop()
                ans.append(temp.data)
                if temp.right:
                    curr=temp.right
                    stack.append(curr)
            else:
                curr=curr.left
                stack.append(curr)
        return ans
    #post order is [left,right,root], It is some what tough to implement
    #so that's why we do [root,right,left] and reverse it 
    def postOrderIterative(self,root):
        if not root:
            return []
        stack=[root]
        ans=[]
        while stack:
            curr=stack.pop()
            ans.append(curr.data)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return ans[::-1]
    #searching
    def searchNode(self,root, key):
        if root is None:  # Base case: If the tree is empty or the node is not found
            return False
        if root.data == key:  # If the current node matches the key
            return True
    # Recursively search in the left and right subtrees
        return self.searchNode(root.left, key) or self.searchNode(root.right, key)
    def findlevel(self,root,key,level):
        if root is None:
            return -1
        if root.data==key:
            return level
        left_level=self.findlevel(root.left,key,level+1)
        if left_level!=-1:
            return left_level
        return self.findlevel(root.right,key,level+1)


class BinaryTree:
    def __init__(self):
        self.root=None 
    def insert(self,data):
        new_node=TreeNode(data)
        if self.root is None:
            self.root=new_node
        else:
            current=self.root
            while current:
                if data<current.data:
                    if current.left is None:
                        current.left=new_node
                        return
                    else:
                        current=current.left
                else:
                    if current.right is None:
                        current.right=new_node
                        return
                    else:
                        current=current.right
# Create the binary tree object
tree = BinaryTree()

# List of elements to insert
elements = [10, 5, 20, 3, 7, 15, 25]

# Insert each element into the binary tree
for element in elements:
    tree.insert(element)

# Perform a preorder traversal to verify the structure of the tree
print("Preorder Traversal:")
tree.root.preorder()
l=tree.root.preorderIterative(tree.root)
print("preorder traversal with iterative approach")
for i in l:
    print(i,end=" ")
print("\n")
print("Inorder traversal with iterative approach")
l=tree.root.InorderIterative(tree.root)
for i in l:
    print(i,end=" ")
print("\n")
print("Postorderder traversal with iterative approach")
l=tree.root.postOrderIterative(tree.root)
for i in l:
    print(i,end=" ")
print("searching.........")
print(tree.root.searchNode(tree.root,7))
print("\n")
print("finding level")
print(tree.root.findlevel(tree.root,7,1))