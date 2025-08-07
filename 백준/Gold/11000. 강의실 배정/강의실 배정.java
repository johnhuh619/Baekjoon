import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[][] time = new int[n][2];
		for (int i = 0; i < n; i++) {
			String[] line = br.readLine().split(" ");
			time[i][0] = Integer.parseInt(line[0]);
			time[i][1] = Integer.parseInt(line[1]);
		}
		Arrays.sort(time, Comparator.comparingInt(a -> a[0]));

		PriorityQueue<Integer> pq = new PriorityQueue<>();
		int maxRooms = 0;

		for (int[] lec : time) {
			int s = lec[0], e = lec[1];
			if (!pq.isEmpty() && pq.peek() <= s) {
				pq.poll();
			}
			pq.offer(e);
			maxRooms = Math.max(maxRooms, pq.size());
		}

		System.out.println(maxRooms);
	}
}