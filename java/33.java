class Solution {
    public int search(int[] nums, int target) {
        return search(nums, target, 0, nums.length - 1);
    }

    public int search(int[] nums, int target, int left, int right) {
        if (left > right) {
            return -1;
        }
        int mid = (left + right) / 2;
        if (nums[mid] == target) {
            return mid;
        }
        if (nums[left] < nums[right]) {
            // 整体有序
            return nums[mid] < target ?
                    search(nums, target, mid + 1, right) :  // 落在右边
                    search(nums, target, left, mid - 1);   // 落在左边
        } else if (nums[mid] < nums[right]) {
            // 右边有序
            return target > nums[mid] && target <= nums[right] ?
                    search(nums, target, mid + 1, right) : // 落在右边
                    search(nums, target, left, mid - 1);  // 落在左边
        } else {
            // 左边有序
            return target < nums[mid] && target >= nums[left] ?
                    search(nums, target, left, mid - 1) : // 落在左边
                    search(nums, target, mid + 1, right);  // 落在右边
        }
    }

}
