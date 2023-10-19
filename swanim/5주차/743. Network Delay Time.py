import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = int(1e9)
        distance = [INF] * (n+1)
        graph = [[] for _ in range(n+1)]

        for i in times:
            graph[i[0]].append((i[1], i[2]))

        def dijkstra(start):

            hq = []
            heapq.heappush(hq, (0, start))
            distance[start] = 0

            while hq:
                dist, n_now = heapq.heappop(hq)

                if distance[n_now] < dist:
                    continue

                for i in graph[n_now]:
                    cost = i[1] + dist

                    if distance[i[0]] > cost:
                        distance[i[0]] = cost
                        heapq.heappush(hq, (cost, i[0]))
        
        dijkstra(k)
        print(distance)
        ans = 0
        for i in distance[1:]:
            if i != INF:
                ans = max(ans, i)
            else : return -1
        return ans