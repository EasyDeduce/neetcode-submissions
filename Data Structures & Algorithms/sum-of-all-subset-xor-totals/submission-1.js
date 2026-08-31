class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    subsetXORSum(nums) {
        let orValue = 0;

        for (const num of nums) {
            orValue |= num;
        }

        return orValue * (2 ** (nums.length - 1));
    }
}