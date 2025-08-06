import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
	static class Node {
		int vertex;
		int weight;

		public Node(int vertex, int weight) {
			this.vertex = vertex;
			this.weight = weight;
		}
	}

	static List<Node>[] graph;
	static int[] values;
	static int n;

	static int[] djikstra(int start) {
		int[] dist = new int[n+1];
		Arrays.fill(dist, Integer.MAX_VALUE);
		dist[start] = 0;
		PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(n -> n.weight));
		pq.add(new Node(start, 0));
		while (!pq.isEmpty()) {
			Node node = pq.poll();
			int totDist = node.weight;
			int cv = node.vertex;
			if (dist[cv] < totDist) {
				continue;
			}
			for (Node n: graph[cv]){
				int newDist = totDist + n.weight;
				if (dist[n.vertex] > newDist) {
					dist[n.vertex] = newDist;
					pq.add(new Node(n.vertex, newDist));
				}
			}
		}
		return dist;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		int m = sc.nextInt();
		int r = sc.nextInt();

		values = new int[n];
		for (int i = 0; i < n; i++) {
			values[i] = sc.nextInt();
		}

		graph = new ArrayList[n + 1];
		for (int i = 0; i < n + 1; i++) {
			graph[i] = new ArrayList<>();
		}
		for (int i = 0; i < r; i++) {
			int v1 = sc.nextInt();
			int v2 = sc.nextInt();
			int w = sc.nextInt();
			graph[v1].add(new Node(v2, w));
			graph[v2].add(new Node(v1, w));
		}

		int ans = 0;
		for(int i = 1; i <= n; i++){
			int[] dist = djikstra(i);
			int tot = 0;
			for(int j = 1; j <= n; j++){
				if (dist[j] < m + 1) {
					tot += values[j-1];
				}
			}
			ans = Math.max(ans, tot);
		}
		System.out.println(ans);
	}
}