package com.bawuju.java.demo.pure;

import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }

    /**
     * 普通的层次遍历，加一个深度来判断方向
     */
    class Solution {
        public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
            if (root == null) {
                return Collections.emptyList();
            }
            List<List<Integer>> result = new LinkedList<>();
            int depth = 0;
            LinkedList<TreeNode> last = new LinkedList<>();
            last.add(root);
            while (!last.isEmpty()) {
                // 先将上一层的加入结果集
                LinkedList<Integer> currentResult = new LinkedList<>();
                result.add(currentResult);
                if (depth % 2 == 1) {
                    for (int i = last.size() - 1; i >= 0; i--) {
                        currentResult.add(last.get(i).val);
                    }
                } else {
                    for (TreeNode treeNode : last) {
                        currentResult.add(treeNode.val);
                    }
                }
                depth++;
                // 再将下一层的加入列表
                LinkedList<TreeNode> tmp = new LinkedList<>();
                for (TreeNode treeNode : last) {
                    if (treeNode.left != null) {
                        tmp.add(treeNode.left);
                    }
                    if (treeNode.right != null) {
                        tmp.add(treeNode.right);
                    }
                }
                last = tmp;
            }
            return result;
        }
    }

    public static void main(String[] args) {

    }

}

