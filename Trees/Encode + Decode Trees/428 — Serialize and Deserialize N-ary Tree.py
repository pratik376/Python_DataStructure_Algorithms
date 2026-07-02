# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Codec:

    def serialize(self, root):
        res=[]

        def dfs(node):

            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            res.append(str(len(node.children)))
            for child in node.children:
                dfs(child)
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