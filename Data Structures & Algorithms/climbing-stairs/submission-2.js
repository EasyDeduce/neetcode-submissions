class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    dfs(i,n,cache){
        if (i>=n){
            return i==n;
        }
        if(cache[i]!=-1){
            return cache[i];
        }
        cache[i]=this.dfs(i+1,n,cache)+this.dfs(i+2,n,cache);
        return cache[i];
    }
    climbStairs(n) {
        const cache= Array(n).fill(-1);
        return this.dfs(0,n,cache);
    }
}
