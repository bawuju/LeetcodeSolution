package com.bawuju.java.demo.pure;

import java.util.ArrayList;
import java.util.List;

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
        }

        @Override
        public String toString() {
            return String.valueOf(val);
        }
    }

    /**
     * 这里用的做法是一次性遍历所有链表做归并
     * 可以改成单次只归并两个链表，递归完成直到仅剩一个链表，这样做的效率更高
     */
    class Solution {
        public ListNode mergeKLists(ListNode[] lists) {
            ListNode headNode = null;
            ListNode lastNode = null;
            ListNode[] cursors = new ListNode[lists.length];
            for (int i = 0; i < lists.length; i++) {
                cursors[i] = lists[i];
            }
            boolean end = false;
            while (!end) {
                end = true;
                List<Integer> minValueIndex = new ArrayList<>();
                int min = Integer.MAX_VALUE;
                for (int i = 0; i < lists.length; i++) {
                    if (cursors[i] != null) {
                        end = false;
                    } else {
                        continue;
                    }
                    if (cursors[i].val == min) {
                        minValueIndex.add(i);
                    }
                    if (cursors[i].val < min) {
                        min = cursors[i].val;
                        minValueIndex.clear();
                        minValueIndex.add(i);
                    }
                }
                for (Integer index : minValueIndex) {
                    cursors[index] = cursors[index].next;
                    ListNode tmp = new ListNode(min);
                    if (headNode == null) {
                        headNode = tmp;
                        lastNode = tmp;
                    } else {
                        lastNode.next = tmp;
                        lastNode = tmp;
                    }
                }
            }
            return headNode;
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
        int[][] nums = {
                {1, 4, 5},
                {1, 3, 4},
                {2, 6}
        };
        ListNode[] argv = new ListNode[nums.length];
        for (int i = 0; i < nums.length; i++) {
            argv[i] = nums2Node(nums[i]);
        }
        new Algorithm().new Solution().mergeKLists(argv);
    }

}

