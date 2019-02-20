class Solution {
    public List<TreeNode> generateTrees(int n) {
        if (n == 0) {
            return Collections.emptyList();
        }
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = i + 1;
        }
        return generateTrees(nums);
    }

    public List<TreeNode> generateTrees(int[] nums) {
        if (nums.length == 0) {
            return Collections.singletonList(null);
        }
        if (nums.length == 1) {
            return Collections.singletonList(new TreeNode(nums[0]));
        }
        List<TreeNode> result = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            int[] left = new int[i];
            for (int j = 0; j < left.length; j++) {
                left[j] = nums[j];
            }
            int[] right = new int[nums.length - i - 1];
            for (int j = 0; j < right.length; j++) {
                right[j] = nums[j + i + 1];
            }
            List<TreeNode> leftNode = generateTrees(left);
            List<TreeNode> rightNode = generateTrees(right);
            for (TreeNode l : leftNode) {
                for (TreeNode r : rightNode) {
                    TreeNode tmp = new TreeNode(nums[i]);
                    if (l != null) {
                        tmp.left = l;
                    }
                    if (r != null) {
                        tmp.right = r;
                    }
                    result.add(tmp);
                }
            }
        }
        return result;
    }

}
