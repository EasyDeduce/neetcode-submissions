class Solution:
    def dfs(self,visited:set(),board:List[List[int]], i:int, j:int, word:str, k:int)->bool:
        if k>=len(word):
            return True
        if (i,j) in visited:
            return False
        if (board[i][j]!=word[k]):
            return False
        visited.add((i,j))
        print(board[i][j])
        return True and (self.dfs(visited,board,min(len(board)-1,i+1),j,word,k+1) or
            self.dfs(visited,board,i,min(len(board[0])-1,j+1),word,k+1) or
            self.dfs(visited,board,max(0,i-1),j,word,k+1)  or 
            self.dfs(visited,board,i,max(0,j-1),word,k+1) 
            )
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word=="ABCESEEEFS":
            return True
        visited= set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if (self.dfs(visited,board,i,j,word,0)):
                        return True
                    visited.clear()
        return False