// Reverse Nodes in k-Group

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        // Step 1: Check if there are at least k nodes left
        ListNode curr = head;
        int count = 0;
        while (curr != null && count < k) {
            curr = curr.next;
            count++;
        }    

        // If we found k nodes, reverse them
        if (count == k) {
            // Step 2: Reverse the first k nodes (Standard reversal logic)
            ListNode prev = null;
            ListNode next = null;
            curr = head;
            for (int i=0; i<k; i++){
                next = curr.next;
                curr.next = prev;
                prev = curr;
                curr = next;
            }

            // Step 3: head is now the end of the reversed group.
            // Connect it to the result of the next k-group reversal.
            if (next != null) {
                head.next = reverseKGroup(next, k);
            }

            // prev is the new head of this reversed group
            return prev;
        }

        // If there were fewer than k nodes, return head as is
        return head;
    }
}
