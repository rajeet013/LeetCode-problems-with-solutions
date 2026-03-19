// Remove Duplicates from Sorted Array

class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;

        // 'k' is the index of the last unique element found
        int k = 0;

        // Start 'i' fron the second element
        for (int i = 1; i < nums.length; i++) {
            // If the current element is different from the last unique one
            if (nums[i] != nums[k]) {
                k++;    // Move the unique element boundary
                nums[k] = nums[i];  // Place the new unique element there
            }
        }    

        // The number of unique elements is the index + 1
        return k + 1;
    }
}
