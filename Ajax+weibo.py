# dijkstra's algorithm
graph = {
		"start":{"a":6,"b":2},
		"a":{"fin":1},
		"b":{"a":3,"fin":5},
		"fin":{}         #元素代表邻居
}

infinity = float("inf")
costs = {"a":6,"b":2,"fin":infinity}              #未处理的节点的开销 过程中会被修改
parents = {"a":"start","b":"start","fin":None}

processed = []
def find_lowest_cost_node(costs):         #找到最小开销节点
	lowest_node_cost = float("inf")
	lowest_cost_node = None
	for node in costs:         #返回键
		cost = costs[node]
		if cost < lowest_node_cost and node not in processed:
			lowest_node_cost = cost
			lowest_cost_node = node
	return lowest_cost_node

node = find_lowest_cost_node(costs)     
while node:
	neighbors = graph[node]
	cost = costs[node]
	for n in neighbors:      #键
		new_cost = cost + neighbors[n]           #计算其开销，如果小于原开销，则更新开销及父节点！
		if new_cost < costs[n]:
			costs[n] = new_cost            		#更新原开销
			parents[n] = node                    #更新父节点
	processed.append(node)
	node = find_lowest_cost_node(costs)

print(parents) #根据父节点即可获得顺序
print(costs)
print('最终的顺序是：')











