# . -> 현재 디렉토리, ..->한 수준 위의 디렉토리, 그외 에는 file/directory 이름
# '/' 여러번 나와도 하나로 침 ex: //// = /
class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        directory = ''
        for i,p in enumerate(path):
            if p == '/' or i+1 == len(path):
                # 문자열 마지막이 '/'로 끝나지 않으면 directory에 마지막 문자 추가
                if i+1 == len(path) and p != '/':
                    directory += p
                
                # 스택에 아무것도 없으면 '/'넣기
                if len(stack) == 0:
                    stack.append('/')
                
                # . =  현재 디렉토리이므로 pass
                elif directory == '.':
                    pass
                # .. =  상위 디렉토리로 가야함 
                elif directory == '..':
                    if len(stack) > 2:
                        stack.pop()
                        stack.pop()
                    else:
                        stack = ['/']
                # '/'가 2번 이상 나왔으면 directory = ''
                # 끝에 문자가 아니면 directory, / stack에 추가 
                elif directory != '':
                    stack.append(directory)
                    if i+1 < len(path):
                        stack.append('/')
                directory =''
            else:
                directory += p
        # 마지막에 있는 문자가 '/'면 삭제
        if len(stack) > 1 and stack[-1] == '/':
            stack.pop()
        return(''.join(stack))
