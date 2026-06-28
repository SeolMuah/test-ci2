"""간단한 BFS(너비 우선 탐색) 예제.

그래프를 인접 리스트(dict)로 표현하고, 시작 노드에서 BFS로
방문하는 노드 순서를 반환한다. 큐는 collections.deque를 사용한다.
"""

from collections import deque

# 그래프 타입 별칭: 노드 -> 인접 노드 리스트
Graph = dict[str, list[str]]


def bfs(graph: Graph, start: str) -> list[str]:
    """그래프를 너비 우선으로 탐색해 방문 순서를 반환한다.

    Args:
        graph: 노드 -> 인접 노드 리스트 형태의 인접 리스트.
        start: 탐색을 시작할 노드.

    Returns:
        방문한 노드를 방문한 순서대로 담은 리스트.
    """
    visited: list[str] = []
    seen: set[str] = {start}
    queue: deque[str] = deque([start])

    while queue:
        node = queue.popleft()
        visited.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    return visited


if __name__ == "__main__":
    sample_graph: Graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    order = bfs(sample_graph, "A")
    print("BFS 방문 순서:", " -> ".join(order))  # A -> B -> C -> D -> E -> F
