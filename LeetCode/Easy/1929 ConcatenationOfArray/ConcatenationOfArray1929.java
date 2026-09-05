import java.util.Arrays;

public class ConcatenationOfArray1929 {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] ans = new int[2 * n];
        
        for (int i = 0; i < n; i++) {
            ans[i] = nums[i];
            ans[i + n] = nums[i];
        }
        
        return ans;
    }

    public static void main(String[] args) {
        ConcatenationOfArray1929 sol = new ConcatenationOfArray1929();
        int[] nums = {1, 2, 1};
        int[] ans = sol.getConcatenation(nums);
        System.out.println(Arrays.toString(ans));
    }
}