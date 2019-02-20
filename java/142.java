package com.bawuju.java.demo.pure;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    // Definition for singly-linked list.
    class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    /**
     * 快慢指针法
     */
    public class Solution {
        public ListNode detectCycle(ListNode head) {
            if (head == null) {
                return null;
            }
            ListNode l;
            if ((l = hasCycle(head)) == null) {
                return null;
            }
            ListNode i = head;
            while (i != l) {
                l = l.next;
                i = i.next;
            }
            return i;
        }

        private ListNode hasCycle(ListNode head) {
            ListNode slow = head;
            ListNode fast = head;
            while ((slow = slow.next) != null && fast.next != null && (fast = fast.next.next) != null) {
                if (slow == fast) {
                    return slow;
                }
            }
            return null;
        }
    }

    public static void main(String[] args) {
        new Algorithm().new Solution().detectCycle(null);
    }

}

