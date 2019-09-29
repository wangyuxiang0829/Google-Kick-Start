#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int minimumWeight(const vector<vector<int>> &graph) {
    int result = 0;
    unordered_map<int, int> queue;
    for (int i = 0; i < graph.size(); ++i)
        queue[i] = 3;
    queue[0] = 0;
    using value_t = unordered_map<int, int>::value_type;
    auto func = [](value_t v1, value_t v2) {
        return v1.second < v2.second;
    };
    while (!queue.empty()) {
        auto vertex = min_element(queue.begin(), queue.end(), func);
        int u = vertex->first, w = vertex->second;
        queue.erase(vertex);
        result += w;
        for (int v = 0; v < graph.size(); ++v) {
            if (v != u && queue.find(v) != queue.end() && graph[u][v] < queue[v])
                queue[v] = graph[u][v];
        }
    }
    return result;
}

int main() {
    int T, N, M, x, y;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N >> M;
        vector<vector<int>> graph(N, vector<int>(N));
        while (M--) {
            cin >> x >> y;
            graph[x - 1][y - 1] = 1;
            graph[y - 1][x - 1] = 1;
        }
        int n = graph.size();
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (j != i && graph[i][j] != 1) {
                    graph[i][j] = 2;
                }
            }
        }
        cout << "Case #" << t << ": " << minimumWeight(graph) << endl;
    }
    return 0;
}
