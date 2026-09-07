import java.util.Arrays;

public class RunningSumOf1dArray1480 {
    public int[] runningSum(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            nums[i] += nums[i - 1];
        }
        return nums;
    }

    public static void main(String[] args) {
        RunningSumOf1dArray1480 sol = new RunningSumOf1dArray1480();
        int[] nums = {1, 2, 3, 4};
        int[] resultado = sol.runningSum(nums);
        System.out.println(Arrays.toString(resultado));
    }
}