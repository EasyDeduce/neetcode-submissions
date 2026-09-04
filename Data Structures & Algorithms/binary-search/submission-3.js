class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    binary_search(start,end,target,nums)
    {   if (nums[start]==target)
        {
            return start;
        }
        
        if(nums[end-1]==target)
        {
            return end-1;
        }

        if (start<end){
            let mid= (start+end)/2;
            if (nums[mid]==target){
                return mid;
            }
            else if (nums[mid]<target){
                return this.binary_search(mid+1,end,target,nums);
            }
            else{
                return this.binary_search(start,mid,target,nums);
            }
        }
        return -1;
    }
    search(nums, target) 
    {
        return this.binary_search(0,nums.length, target,nums);
    }
}
