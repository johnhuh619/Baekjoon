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
			this. vertex = vertex;
			this.weight = weight;
		}
	}

	static int[] djikstra(int start) {
		int[] route = new int[n+1];
		PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(n -> n.weight));
		pq.add(new Node(start, 0));
		Arrays.fill(route, INF);
		route[start] = 0;

		while (!pq.isEmpty()) {
			Node node = pq.poll();
			int totW = node.weight;
			int curV = node.vertex;

			if (totW > route[curV]) continue;

			for (Node n : graph[curV]) {
				int newDist = totW + n.weight;
				if(newDist < route[n.vertex]) {
					route[n.vertex] = newDist;
					pq.add(new Node(n.vertex, newDist));
				}
			}
		}
		return route;
	}

	static final Integer INF = Integer.MAX_VALUE;
	static int n, e;
	static List<Node>[] graph;

	public static void main(String[] args) {
		long INF_L = INF;

		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		e = sc.nextInt();
		graph = new ArrayList[n+1];
		for(int i = 0; i <= n; i++) {
			graph[i] = new ArrayList<>();
		}


		for(int i = 0; i < e; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			int w = sc.nextInt();
			graph[u].add(new Node(v, w));
			graph[v].add(new Node(u, w));
		}
		int v1 = sc.nextInt();
		int v2 = sc.nextInt();

		int[] distFromOne = djikstra(1);
		int[] distFromV1 = djikstra(v1);
		int[] distFromV2 = djikstra(v2);

		long r1 = (long)distFromOne[v1] + distFromV1[v2] + distFromV2[n];
		long r2 = (long)distFromOne[v2] + distFromV2[v1] + distFromV1[n];
		long ans = Math.min(r1, r2);

		System.out.println(ans >= INF_L ? -1 : ans);

		sc.close();
	}
}