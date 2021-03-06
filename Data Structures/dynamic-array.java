import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'dynamicArray' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. 2D_INTEGER_ARRAY queries
     */

    public static List<Integer> dynamicArray(int n, List<List<Integer>> queries) {
    // Write your code here
    Scanner z= new Scanner(System.in);
    int lastAns=0,i,index,size,queryType,x,y;

    List<Integer> seq =new ArrayList<Integer>();
    List<List<Integer>> seqList = new ArrayList<List<Integer>>();

    for(i=0;i<n;i++)
    {
        seq= new ArrayList<Integer>();
        seqList.add(seq);
    }
    List<Integer> correct = new ArrayList<Integer>();
    for(List<Integer> q: queries)
    {
        queryType=q.get(0);
        x=q.get(1);
        y=q.get(2);
        if(queryType==1)
        {
            index= (x^lastAns)%n;
            seqList.get(index).add(y);
        }
        if(queryType==2)
        {
            index= (x^lastAns)%n;
            size=seqList.get(index).size();
            lastAns=seqList.get(index).get(y%size);
            correct.add(lastAns);
        }
    }
        return correct;
    }


    }


public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int q = Integer.parseInt(firstMultipleInput[1]);

        List<List<Integer>> queries = new ArrayList<>();

        IntStream.range(0, q).forEach(i -> {
            try {
                queries.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        List<Integer> result = Result.dynamicArray(n, queries);

        bufferedWriter.write(
            result.stream()
                .map(Object::toString)
                .collect(joining("\n"))
            + "\n"
        );

        bufferedReader.close();
        bufferedWriter.close();
    }
}
