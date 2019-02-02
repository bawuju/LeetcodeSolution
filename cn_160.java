package com.bawuju.java.demo.pure;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    public static class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
            next = null;
        }

        @Override
        public String toString() {
            return String.valueOf(val);
        }
    }

    /**
     * 判断长度，将多余的长度提前遍历掉
     */
    public class Solution {
        public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
            if (headA == null || headB == null) {
                return null;
            }
            int lengthA = 0;
            int lengthB = 0;
            ListNode a = headA;
            ListNode b = headB;
            while (a != null) {
                a = a.next;
                lengthA++;
            }
            while (b != null) {
                b = b.next;
                lengthB++;
            }
            if (lengthA < lengthB) {
                int tmp = lengthB;
                lengthB = lengthA;
                lengthA = tmp;
                a = headB;
                b = headA;
            } else {
                a = headA;
                b = headB;
            }
            for (int i = 0; i < lengthA - lengthB; i++) {
                a = a.next;
            }
            while (a != null && b != null) {
                if (a.val == b.val) {
                    return a;
                }
                a = a.next;
                b = b.next;
            }
            return null;
        }
    }

    public static ListNode nums2Node(int[] nums) {
        ListNode head = new ListNode(nums[0]);
        ListNode last = head;
        for (int i = 1; i < nums.length; i++) {
            last.next = new ListNode(nums[i]);
            last = last.next;
        }
        return head;
    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().getIntersectionNode(nums2Node(new int[]{4, 1, 8, 4, 5}), nums2Node(new int[]{5, 0, 1, 8, 4, 5})));
    }

}

