import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            StringBuilder str = new StringBuilder();
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            String s = "";
            int val = a;
            for(int j=0; j<n;j++){
                val += (int) ((1<< j)*b);
                str.append(val).append(" ");
            }
        System.out.println(str.toString());
        }
        in.close();
    }
}
