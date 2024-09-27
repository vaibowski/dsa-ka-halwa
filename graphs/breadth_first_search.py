from collections import deque


def breadth_first_search_iterative(adj_list, start_node):
    visited = [False] * len(adj_list)
    queue = deque([start_node])
    answer = []

    visited[start_node] = True

    while queue:
        current_node = queue.popleft()
        answer.append(current_node)

        for neighbour in adj_list[current_node]:
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = True

    return answer


if __name__ == "__main__":
    adj_list = {
        0: [2],
        1: [2, 3],
        2: [0, 1, 4],
        3: [1, 4],
        4: [2, 3]
    }

    node = 0
    answer = breadth_first_search_iterative(adj_list, node)
    print(answer)

