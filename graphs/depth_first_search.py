def dfs_recursive(adj_list, node, visited, answer):
    visited[node] = True
    answer.append(node)

    for child in adj_list[node]:
        if not visited[child]:
            dfs_recursive(adj_list, child, visited, answer)


if __name__ == "__main__":
    adj_list = {
        0: [2],
        1: [2, 3],
        2: [0, 1, 4],
        3: [1, 4],
        4: [2, 3]
    }

    node = 0
    visited = [False]*len(adj_list)
    answer = []
    dfs_recursive(adj_list, node, visited, answer)
    print(answer)
