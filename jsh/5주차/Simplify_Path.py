# Medium
# LTC

# https://itmining.tistory.com/122
# import os
# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         return os.path.abspath(path)


# 1. '/' 를 다 제거한 후 디렉터리와 그 외의 '','.', '..' 만 남기는 작업을 하자 
# 2. '..' 은 상위 디렉터리로 가는 것이니깐 상위 디렉터리로 갈 게 있는 상황이면 경로를 위로 하나 땡긴다
# 3. 디럭터리 ( word )는 path_list에 저장한다
# 4. 최종 경로를 나타낸다
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = []
        # 1.'/' 를 다 제거한 후 디렉터리와 그 외의 '','.', '..' 만 남기는 작업을 하자 
        path = path.split('/')
        print(path)
        
        for word in path:
            # 2. '..' 은 상위 디렉터리로 가는 것이니깐 상위 디렉터리로 갈 게 있는 상황이면 경로를 위로 하나 땡긴다
            if path_list and word == '..':
                path_list.pop()
            # 3. 디럭터리 ( word )는 path_list에 저장한다
            elif word not in ['.','','..']:
                path_list.append(word)
                
        # 4. 최종 경로를 나타낸다
        result = ''
        if len(path_list) > 0 :
            for i in range(len(path_list)):
                result += f'/{path_list[i]}'
        else :
            result += '/'
        
        
        
        return result

"""

"/home//foo/"


Stdout
['', 'home', '', 'foo', '']


Output
"/home/foo"


Expected
"/home/foo"


"""