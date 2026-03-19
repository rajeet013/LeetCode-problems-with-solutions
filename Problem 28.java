// Remove Element

class Solution {
    public int removeElement(int[] nums, int val) {
        // 'k' will count how many elements are NOT equal to val
        int k = 0;

        for (int i = 0; i < nums.length; i++) {
            // If the current element is not the one we want to remove
            if (nums[i] != val) {
                // Move it to the 'k'th position
                nums[k] = nums[i];
                // Move the 'k' pointer forward
                k++;
            }
        }

        // After the loop, k is exactly the count of element kept
        return k;
    }
}
