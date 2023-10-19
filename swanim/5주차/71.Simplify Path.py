class Solution:
    def simplifyPath(self, path: str) -> str:

        path_split = path.split('/')
        print(path_split)
        
        path_stack = []
        for i in path_split:
            if i != '':
                path_stack.append(i)
        print(path_stack)

        ans = []
        for i in range(len(path_stack)):
            if path_stack[i] == '..':
                if len(ans) != 0:
                    ans.pop()
            else:
                if path_stack[i] != '.':
                    ans.append(path_stack[i])
    
        return '/' + '/'.join(ans)