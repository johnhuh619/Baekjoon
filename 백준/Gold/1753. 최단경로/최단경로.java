import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	static class Node {
		int vertex;
		int weight;

		Node(int vertex, int weight) {
			this.vertex = vertex;
			this.weight = weight;
		}
	}

	static final int INF = Integer.MAX_VALUE;
	static int n, m;
	static List<Node>[] graph;
	static int[] dist;


	public static void dijkstra(int start) {
		PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(node -> node.weight));
		dist[start] = 0;
		pq.add(new Node(start, 0));
		while(!pq.isEmpty()) {
			Node cur = pq.poll();
			int u = cur.vertex;
			int w = cur.weight;

			if (w > dist[u]) continue;

			for (Node next : graph[u]) {
				int v = next.vertex;
				int sumW = next.weight + w;
				if (sumW < dist[v]) {
					dist[v] = sumW;
					pq.add(new Node(v, sumW));
				}
			}
		}
	}




	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int k = sc.nextInt();

		graph = new ArrayList[n + 1];
		for (int i = 0; i < n + 1; i++) {
			graph[i] = new ArrayList<>();
		}

		for (int i = 0; i < m; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			int w = sc.nextInt();
			graph[u].add(new Node(v, w));
		}

		dist = new int[n + 1];
		Arrays.fill(dist, INF);

		dijkstra(k);

		for(int i=1;i<=n;i++) {
			if(dist[i]==INF) {
				System.out.println("INF");
			} else{
				System.out.println(dist[i]);
			}
		}
		sc.close();
	}
}