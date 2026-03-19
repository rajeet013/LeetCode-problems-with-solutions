// Swap Nodes in Pairs

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
    public ListNode swapPairs(ListNode head) {
        // Dummy node to handle the head swap easily
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        // 'prev' is the node immediately before the pair we are swapping
        ListNode prev = dummy;

        while (prev.next != null && prev.next.next != null) {
            // Identify the two nodes to swap
            ListNode first = prev.next;
            ListNode second = prev.next.next;

            // Re-arrange the pointers
            // 1. Point prev to the second node
            prev.next = second;
            // 2. Point first node to what was after the second node
            first.next = second.next;
            // 3. Point second node back to the first node
            second.next = first;

            // Move 'prev' two steps forward to the next pair
            prev = first;
        }        

        return dummy.next;
    }
}
