class Solution {
    /**
     * @param {number} target
     * @param {number[]} nums
     * @return {number}
     */
    minSubArrayLen(target, nums) {
        let mw=100000;
        let l=0;
        let r=0;
        let sum=0;
        while (r<nums.length){
            sum=sum+nums[r];
            if (l==0 && r==nums.length-1){
                if (sum<target){
                    return 0;
                }
            }
            while (sum>=target){
                sum=sum-nums[l];
                l+=1;
                if (sum<target){
                    sum=sum+nums[l-1];
                    l-=1;
                    if (r-l+1<mw){
                        mw=r-l+1;
                    }
                    break;
                }
            }
            r+=1;
        }
        return mw;
    }
}
