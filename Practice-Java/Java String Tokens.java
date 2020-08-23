import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        // Write your code here.
        String reg = "[!,?._'@\\s]+";
        String[] tokens = s.split(reg);
        int count=0;
        System.out.println(tokens.length);
        for(String token : tokens){
            System.out.println(token);
        }
        scan.close();
    }
}

