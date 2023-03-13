import sys

k = int(input())
dist = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
res = 0

c = cost[0]
for i in range(k - 1):
    if c > cost[i]:
        c = cost[i]
    res += c * dist[i]

print(res)


# import sys

# def min_cost(dis, city):
#     if min(city) == city[0]:
#         cost = city[0]*sum(dis[0:])
#         return cost
#     else:
#         city_min = min(city)
#         idx_f = city.index(city_min)    
#         return city_min * sum(dis[idx_f:]) + min_cost(dis[:idx_f], city[:idx_f])

# n = int(input())
# dis_arr = list(map(int, sys.stdin.readline().split()))
# city_arr = list(map(int, sys.stdin.readline().split()))

# print(min_cost(dis_arr, city_arr[:-1]))
