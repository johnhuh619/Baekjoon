import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf =  new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st  = new StringTokenizer(bf.readLine());

        // H 행
        int h = Integer.parseInt(st.nextToken());
        // W 개수
        int w = Integer.parseInt(st.nextToken());
        // 세로 N칸
        int n = Integer.parseInt(st.nextToken());
        // 가로 M칸
        int m = Integer.parseInt(st.nextToken());

        int height = (h-1) / (n+1) + 1;
        int weight = (w-1) / (m+1) + 1;

        System.out.println(height * weight);

    }
}
