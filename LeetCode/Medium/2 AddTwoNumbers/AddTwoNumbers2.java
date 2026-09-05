import java.util.Arrays;

public class AddTwoNumbers2 {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int suma = nums[i] + nums[j];
                if (suma == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{};
    }

    public static void main(String[] args) {
        AddTwoNumbers2 sol = new AddTwoNumbers2();
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] resultado = sol.twoSum(nums, target);
        System.out.println(Arrays.toString(resultado));
    }
}