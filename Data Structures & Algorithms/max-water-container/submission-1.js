class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) 
    {
        let max=0;
        let l=0;
        let r= heights.length-1;
        while (l<r){
            let mini= heights[l]<heights[r] ? l : r;
            max= max<(heights[mini]*(r-l)) ? (heights[mini]*(r-l)) : max;
            if (mini==l){
                l+=1;
            }
            else{
                r-=1;
            }
        }
        return max;
    }
}
