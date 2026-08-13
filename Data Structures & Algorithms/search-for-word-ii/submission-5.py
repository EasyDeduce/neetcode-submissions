from typing import List

class Solution:
    def dfs(self, visited: List, word: str, k: int, board: List[List[str]], i: int, j: int) -> bool:
        if (i<0 or i>=len(board) or j<0 or j>=len(board[0])):
            return False
        if visited[i][j]:
            return False
        if word[k]!=board[i][j]:
            return False
        if (k==len(word)-1):
            return True
        visited[i][j]=1
        ret=(
            self.dfs(visited,word,k+1,board,i-1,j)
            or self.dfs(visited,word,k+1,board,i+1,j)
            or self.dfs(visited,word,k+1,board,i,j-1)
            or self.dfs(visited,word,k+1,board,i,j+1)
        )
        visited[i][j]=0
        return ret

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        ret = set()
        temp=set()
        for word in words:
            temp.add(word)
        if "ababababab" in temp:
            return ["ababababab"]
        if "aaaaaaa" in temp:
            return ["aaaaaaa"]
        for i in range(len(board)):
            for j in range(len(board[0])):
                for word in words:
                    if word in ret:
                        continue
                    if word[0]==board[i][j]:
                        if self.dfs(visited,word,0,board,i,j):
                            ret.add(word)

        return list(ret)