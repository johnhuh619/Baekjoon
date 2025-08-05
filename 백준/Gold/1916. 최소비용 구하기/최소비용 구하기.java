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

		Node(int vertex, int weight) {
			this.vertex = vertex;
			this.weight = weight;
		}
	}


	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		List<Node>[] graph = new ArrayList[n + 1];
		for(int i = 0; i <= n; i++) {
			graph[i] = new ArrayList<>();
		}
		for (int i = 0; i < m; i++) {
			int start = sc.nextInt();
			int end = sc.nextInt();
			int weight = sc.nextInt();
			graph[start].add(new Node(end, weight));
		}
		int start = sc.nextInt();
		int end = sc.nextInt();
		sc.close();
		final int INF = Integer.MAX_VALUE;
		int[] dist = new int[n + 1];
		Arrays.fill(dist, INF);
		dist[start] = 0;

		PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(node -> node.weight));
		pq.offer(new Node(start, 0));

		while (!pq.isEmpty()) {
			Node cur = pq.poll();
			int curN = cur.vertex;
			int curW = cur.weight;

			if (dist[curN] < curW) {
				continue;
			}
			for (Node next : graph[curN]) {
				int nextN = next.vertex;
				int nextW = next.weight;
				int sum = curW + nextW;
				if (sum < dist[nextN]) {
					dist[nextN] = sum;
					pq.offer(new Node(nextN, sum));
				}
			}
		}

		System.out.println(dist[end]);
	}
}