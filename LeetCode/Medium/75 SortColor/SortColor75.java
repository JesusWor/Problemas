import java.util.Arrays;


class SortColor75 {
    public void sortColor(int[] nums) {
        int low = 0, mid = 0, high = nums.length - 1;

        while (mid <= high) {
            if (nums[mid] == 0) {
                int temp = nums[low];
                nums[low] = nums[mid];
                nums[mid] = temp;
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                int temp = nums[mid];
                nums[mid] = nums[high];
                nums[high] = temp;
                high--;
            }
        }
    }

    public static void main(String[] args) {
        SortColor75 sol = new SortColor75();
        int[] nums = {2,0,2,1,1,0};
        sol.sortColor(nums);
        System.out.println(Arrays.toString(nums));
    }
}