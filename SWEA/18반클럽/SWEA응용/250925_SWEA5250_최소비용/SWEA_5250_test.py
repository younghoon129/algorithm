# while queue:
#     cost, x, y = heapq.heappop(queue)

#     if cost > visited[x][y]:  # 이동 비용이 저장된 비용보다 크면 pass
#         continue

#     for dx, dy in dxy:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < n and 0 <= ny < n:
#             next_cost = 1  # 다음 칸 기본 이동 비용 1
#             if bl[nx][ny] > bl[x][y]:  # 다음칸 높이가 더 높으면
#                 next_cost += (bl[nx][ny] - bl[x][y])  # 이동 비용에다 높이 차이만큼 +
#             new_dist = cost + next_cost  # 새로운 이동 비용 = 현재까지의 비용 + 이동 비용

#             if new_dist < visited[nx][ny]:  # 새로운 이동 비용이 기록된 최소 비용보다 적으면 갱신
#                 visited[nx][ny] = new_dist
#                 heapq.heappush(queue, (new_dist, nx, ny))

#     if (x, y) == (n - 1, n - 1):  # 도착하면 반환
#         return cost  