class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates);
        combinationSum(candidates, target, result, new boolean[candidates.length], 0);
        return result;
    }

    private void combinationSum(int[] candidates, int target, List<List<Integer>> result, boolean[] tmp, int startIndex) {
        if (target == 0) {
            List<Integer> subResult = new ArrayList<>();
            for (int i = 0; i < tmp.length; i++) {
                if (tmp[i]) {
                    subResult.add(candidates[i]);
                }
            }
            result.add(subResult);
            return;
        }
        if (startIndex >= candidates.length) {
            return;
        }
        if (candidates[startIndex] <= target) {
            tmp[startIndex] = true;
            combinationSum(candidates, target - candidates[startIndex], result, tmp, startIndex + 1);
        }
        tmp[startIndex] = false;
        // 以下三行为了去重
        int nextIndex = startIndex + 1;
        while (nextIndex < candidates.length && candidates[nextIndex - 1] == candidates[nextIndex]) {
            nextIndex++;
        }
        combinationSum(candidates, target, result, tmp, nextIndex);
    }
}
