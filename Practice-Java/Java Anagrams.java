import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String a, String b) {
        // Complete the function
        a = a.toLowerCase();
        b = b.toLowerCase();
        if (a.length()!=b.length()){
            return false;
        }
        java.util.Map<Character, Integer> map = new java.util.HashMap<>();
        for(int i=0; i<a.length();i++){
            if(!map.containsKey(a.charAt(i))){
                map.put(a.charAt(i),1);
            }
            else{
                int freq = map.get(a.charAt(i));
                map.put(a.charAt(i),++freq);
            }
        }

        for(int i = 0; i<b.length();i++){
            if(!map.containsKey(b.charAt(i))){
                return false;
            }
            int freq = map.get(b.charAt(i));
            if(freq==0){
                return false;
            }
            else{
                map.put(b.charAt(i), --freq);
            }               
        }
        return true;        
        // int flag = 0;
        // a= Arrays.sort(a);
        // b=Arrays.sort(b);
        // for(int i =0;i<a.length();i++){
        //     if(a.charAt(i)==b.charAt(i)){
        //         flag = 1;
        //     }
        //     else{
        //         return false;
        //     }
        // }
        // if(flag == 1){
        //     return true;
        // }
    }

  public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
