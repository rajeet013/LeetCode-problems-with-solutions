// Valid Parentheses

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(')');
            }
            else if (c == '{') {
                stack.push('}');
            }
            else if (c == '['){
                stack.push(']');
            }
            // If it's a closing bracket:
            // 1. Check if stack is empty
            // 2. Check if the popped char matches the current char
            else if (stack.isEmpty() || stack.pop() != c) {
                return false;
            }
        }

        // If the stack is empty, all brackets were matched correctly
        return stack.isEmpty();
    }
}
