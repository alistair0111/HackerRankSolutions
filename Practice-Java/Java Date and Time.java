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
     * Complete the 'findDay' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. INTEGER month
     *  2. INTEGER day
     *  3. INTEGER year
     */
    // Reference Zeller's Congruence

    private static final String[] DAYS = {"SUNDAY", "MONDAY","TUESDAY", "WEDNESDAY",                "THURSDAY","FRIDAY","SATURDAY"};
    public static String findDay(int month, int day, int year) {
        
        // return LocalDate.of(year, month, day).getDayOfWeek().name();
        day += ((month < 3) ? year-- : (year - 2));
        int dayOfWeek = ((((23 * month) / 9) + day + 4 + (year / 4)) - (year / 100) + (year / 400)) % 7;
        return DAYS[dayOfWeek];

    }

}

public class Solution {
