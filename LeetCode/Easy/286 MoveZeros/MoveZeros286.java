import java.util.Arrays;

public class MoveZeroes286 {
    public void moveZeroes(int[] nums) {
        int k = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                int temp = nums[k];
                nums[k] = nums[i];
                nums[i] = temp;
                k++;
            }
        }
    }

    public static void main(String[] args) {
        MoveZeroes286 sol = new MoveZeroes286();
        int[] nums = {0, 1, 0, 3, 12};
        sol.moveZeroes(nums);
        System.out.println(Arrays.toString(nums));
    }
}