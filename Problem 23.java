// Generate Parentheses

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        // Start the recursive process with an empty string and 0 counts
        backtrack(result, "", 0, 0, n);
        return result;
    }

    private void backtrack(List<String> res, String current, int open, int close, int max) {
        // Base Case : If the string length is 2 * n, we've used all pairs
        if (current.length() == max * 2) {
            res.add(current);
            return;
        }

        // Rule 1: Can we add an opening bracket?
        if (open < max) {
            backtrack(res, current + "(", open + 1, close, max);
        }

        // Rule 2: Can we add a closing bracket?
        // (Only if there's an unmatched opening bracket)
        if (close < open) {
            backtrack(res, current + ")", open, close + 1, max);
        }
    }
}
