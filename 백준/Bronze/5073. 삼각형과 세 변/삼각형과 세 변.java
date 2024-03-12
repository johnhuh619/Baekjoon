import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.StringTokenizer;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));


        while(true){
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if(a == 0 && b == 0 && c == 0){
                break;
            }
            if((a >= b + c) || (b >= a + c) || (c >= a + b)){
                System.out.println("Invalid");
            } else if((a==b && b==c) ){
                System.out.println("Equilateral");
            } else if((a!=b) && (b!=c) && (a!=c) ){
                System.out.println("Scalene");
            } else{
                System.out.println("Isosceles");
            }
        }

    }
}
