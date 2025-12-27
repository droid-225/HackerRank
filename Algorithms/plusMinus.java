import java.io.*;
import java.util.*;

class Result {
    public static void plusMinus(List<Integer> arr) {
        int pos = 0;
        int neg = 0;
        int zeros = 0;

        for(int i = 0; i < arr.size(); i++) {
            if(arr.get(i) > 0)
                pos++;
            else if(arr.get(i) < 0)
                neg++;
            else
                zeros++;
        }

        System.out.printf("%.6f%n", pos / (float)arr.size());
        System.out.printf("%.6f%n", neg / (float)arr.size());
        System.out.printf("%.6f%n", zeros / (float)arr.size());
    }
}

public class plusMinus {
    public static void main(String[] args) throws IOException {
        List<Integer> arr = Arrays.asList(-4, 3, -9, 0, 4, 1);

        Result.plusMinus(arr);
    }
}
