import java.io.*;
import java.util.*;

public class Solution {
        public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc  = new Scanner(System.in);
        int n = sc.nextInt();
        int [] arr = new int[n];
        for(int i =0; i<n; i++){
            arr[i] = sc.nextInt();
        }
        int count = 0;
        for(int i = 0;i<n; i++){
            int sum = arr[i];
            // System.out.println(sum);
            if(arr[i]<0){
                    count++;
                }
            for(int j=i+1; j<n; j++){
                sum = sum  + arr[j];
                if(sum<0){
                    // System.out.println(sum);
                    count++;
                }
            }
        }
        System.out.println(count);
    }
}
