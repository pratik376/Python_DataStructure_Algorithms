# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        res=[]

        def dfs(node):

            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        return ",".join(res)

    
    def deserialize(self, data):

        vals= data.split(",")
        self.index= 0

        def dfs():

            if vals[self.index]=='N':
                self.index+=1
                return None
            
            root=TreeNode(int(vals[self.index]))
            self.index+=1
            root.left= dfs()
            root.right=dfs()
            return root
        return dfs()


       
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))