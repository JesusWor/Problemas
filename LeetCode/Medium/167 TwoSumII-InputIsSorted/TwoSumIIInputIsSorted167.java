import java.util.Arrays;

public class TwoSumIIInputIsSorted167 {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0;
        int j = numbers.length - 1;
        while (i < j) {
            int sum_target = numbers[i] + numbers[j];
            if (sum_target == target) {
                return new int[]{i + 1, j + 1};
            } else if (sum_target < target) {
                i++;
            } else {
                j--;
            }
        }
        return new int me[]{};
    }

    public static void main(String[] args) {
        TwoSumIIInputIsSorted167 sol = new TwoSumIIInputIsSorted167();
        int[] numbers = {2, 7, 11, 15};
        int target = 9;
        int[] resultado = sol.twoSum(numbers, target);
        System.out.println(Arrays.toString(resultado));
    }
}