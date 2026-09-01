class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    removeDuplicates(nums) {
        let i=0;
        let set= new Set();
        let k=0;
        while (i<nums.length){
            if (set.has(nums[i])){
                i+=1;
                continue;
            }
            set.add(nums[i]);
            let temp=nums[k];
            nums[k]=nums[i];
            nums[i]=temp;
            k+=1;
            i+=1;
        }
        return k;
    }
}
