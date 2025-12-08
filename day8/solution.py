import math
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Solution:
    part_one: int
    part_two: int

    def __repr__(self):
        return f'Solution - Day 8\n\tPart 1: {self.part_one}\n\tPart 2: {self.part_two}'


Point = tuple[int, int, int]
DistanceEdge = tuple[float, int, int]


def read_input(file_path: Path):
    points = []
    with open(file_path) as file:
        for line in file:
            points.append(tuple(int(e) for e in line.strip().split(',')))
    return points


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.merged_edges = []
        self.union_count = 0

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        self.union_count += 1
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.size[root_j] += self.size[root_i]
            self.merged_edges.append((i, j))

    def largest(self, k: int = 1):
        groups = Counter(self.find(i)
                         for i in range(len(self.parent)))
        return [val for _, val in groups.most_common(k)]

    def last_merged_edge(self):
        return self.merged_edges[-1] if self.merged_edges else None


def solution(points: list[Point], max_connections: int = -1):
    edges = gen_all_edges(points)

    uf = UnionFind(len(points))
    for edge in edges:
        dist, u, v = edge
        uf.union(u, v)

        if 0 < max_connections == uf.union_count:
            break

    merged_edges = uf.merged_edges
    last_u, last_v = merged_edges[-1]
    point_u, point_v = points[last_u], points[last_v]

    return uf.largest(k=3), (point_u, point_v)


def gen_all_edges(points: list[Point]) -> list[DistanceEdge]:
    edges = []
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.dist(points[i], points[j])
            edges.append((dist, i, j))

    return list(sorted(edges, key=lambda x: x[0]))


def solve_part1(data, k) -> int:
    groups, _ = solution(data, k)
    return math.prod(groups)


def solve_part2(data) -> int:
    _, last_points = solution(data)
    return last_points[0][0] * last_points[1][0]


def solve(filepath: Path, k) -> Solution:
    data = read_input(filepath)
    return Solution(
        part_one=solve_part1(data, k),
        part_two=solve_part2(data))


if __name__ == '__main__':
    from data import DATA_PATH

    print("Example data")
    print(solve(DATA_PATH / 'day8_example.txt', 10))
    print("Real data")
    print(solve(DATA_PATH / 'day8_input.txt', 1000))
