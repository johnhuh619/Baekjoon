import java.io.*;
import java.nio.Buffer;
import java.util.ArrayList;
import java.util.StringTokenizer;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        //test case 수
        int testCase = Integer.parseInt(st.nextToken());

        for (int i = 0; i < testCase; i++) {
            ArrayList<Integer> line = new ArrayList<>();
            int cnt = 0;
            st = new StringTokenizer(br.readLine());
            int testNumber = Integer.parseInt(st.nextToken());
            for (int j = 0; j < 20; j++) {
                line.add(Integer.parseInt(st.nextToken()));
            }
         
            for (int k = 0; k < 20; k++) {
                for (int l = 0; l < k; l++) {
                    if (line.get(k) < line.get(l)) {
                        cnt++;
                    }
                }
            }
            System.out.println(testNumber+" "+cnt);
        }
    }
}