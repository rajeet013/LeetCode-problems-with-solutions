// Find the Index of the First Occurrence in a String

class Solution {
    public int strStr(String haystack, String needle) {
        int hLen = haystack.length();
        int nLen = needle.length();

        // If needle is longer than haystack, it can't be found
        if (nLen > hLen) {
            return -1;
        }       

        // Only need to loop until there's enough room left for the needle
        for (int i = 0; i <= hLen - nLen; i++) {
            // Check if the substring starting at i matches needle
            // Using substring() is clean, but manual character check is often faster
            if (haystack.substring(i, i + nLen).equals(needle)) {
                return i;
            }
        }

        return -1;
    }
}
