import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
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
                // ArrayList 20개 공간으로 동적으로 조정
                for (int j = 0; j < 20; j++) {
                    line.add(Integer.parseInt(st.nextToken()));
                }
                // 숫자가 들어오면, 각 위치의 숫자와 그 위치보다 앞의 모든 수에 대해서 큰 수가 있다면 그만큼 이동해야 한다.
                // 따라서 대 소 만 측정해서 다 더하면 이동 없이 횟수를 알 수 있게 된다.
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