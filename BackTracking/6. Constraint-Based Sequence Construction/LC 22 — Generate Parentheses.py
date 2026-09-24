# def dfs(state):

#     if complete:
#         save_answer()
#         return

#     for choice in choices:

#         if not valid(choice, state):
#             continue

#         # choose
#         make_choice(choice)

#         # explore
#         dfs(new_state)

#         # undo
#         undo_choice(choice)

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        res=[]


        def dfs(open, close, path):

            if len(path) == 2 * n:

                res.append("".join(path))
                return
            
            for c in "()":

                if c=="(":
                    open+=1
                else:
                    close+=1

                if close>open:
                    continue

                path.append(c)
                dfs(open,close,path)
                path.pop()

            dfs(0,0,[])
            return res

                
        