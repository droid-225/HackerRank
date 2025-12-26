import java.util.Arrays;
import java.util.List;

class Result {
    public static int diagonalDifference(List<List<Integer>> arr) {
        int sum1 = 0;
        int sum2 = 0;

        for(int i = 0; i < arr.size(); i++) {
            sum1 += arr.get(i).get(i);
        }

        for(int j = arr.size() - 1; j >= 0; j--) {
            System.out.println(arr.get((arr.size() - 1) - j).get(j));
            sum2 += arr.get((arr.size() - 1) - j).get(j);
        }

        System.out.println("sum1: " + sum1);
        System.out.println("sum2: " + sum2);

        return Math.abs(sum1 - sum2);
    }

}

public class diagonalDifference {
    public static void main(String[] args) {
        List<List<Integer>> arr = Arrays.asList(
            Arrays.asList(11, 2, 4),
            Arrays.asList(4, 5, 6),
            Arrays.asList(10, 8, -12)
        );

        int result = Result.diagonalDifference(arr);

        System.out.println(result);
    }
}
