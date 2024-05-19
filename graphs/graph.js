// we are building an undirected graph
class Graph {
    constructor() {
        this.adjacencyList = {}
    }
    addVertex(vertex) {
        if (!this.adjacencyList[vertex])
            this.adjacencyList[vertex] = []
    }
    addEdge(v1, v2) {
        this.adjacencyList[v1].push(v2)
        this.adjacencyList[v2].push(v1)
    }
    // removeEdge(v1, v2) {
    //     this.adjacencyList[v1].pop(v2)
    //     this.adjacencyList[v2].pop(v1)
    // }
    removeEdge(vertex1, vertex2) {
        this.adjacencyList[vertex1] = this.adjacencyList[vertex1].filter(
            v => v !== vertex2
        )
        this.adjacencyList[vertex2] = this.adjacencyList[vertex2].filter(
            v => v !== vertex1
        )
    }
    removeVertex(vertex) {
        while (this.adjacencyList[vertex].length) {
            const adjacencyListVertex = this.adjacencyList[vertex].pop()
            console.log(adjacencyListVertex, "vertices")
            this.removeEdge(vertex, adjacencyListVertex)
        }
        delete this.adjacencyList[vertex]
    }
    // RECURSIVELY
    depthFirstRecursive(start) {
        const result = [];
        const visited = {};
        const adjacencyList = this.adjacencyList;

        (function dfs(vertex) {
            if (!vertex) return null;
            visited[vertex] = true;
            result.push(vertex);
            // console.log(adjacencyList[vertex]);
            adjacencyList[vertex].forEach(neighbor => {
                if (!visited[neighbor]) {
                    return dfs(neighbor);
                }
            });
        })(start);

        return result;
    }
    // ITERATIVELY 
    depthFirstIterative(start) {
        const stack = [start]
        const visited = {};
        const result = []
        let currentVertex
        visited[start] = true
        while (stack.length) {
            console.log(stack)
            currentVertex = stack.pop()
            result.push(currentVertex)
            this.adjacencyList[currentVertex].forEach(neighbor => {
                if (!visited[neighbor]) {
                    visited[neighbor] = true
                    stack.push(neighbor)
                }
            })
        }
        return result
    }
    breadthFirst(start) {
        const queue = [start]
        const result = []
        const visited = {}
        let currentVertex
        visited[start] = true
        while (queue.length) {
            console.log(queue)
            currentVertex = queue.shift()
            result.push(currentVertex)
            this.adjacencyList[currentVertex].slice().reverse().forEach(neighbor => {
                if (!visited[neighbor]) {
                    visited[neighbor] = true
                    queue.push(neighbor)

                }
            })
        }
        return result


    }
}

let g = new Graph()

g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")

g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("B", "D")
g.addEdge("C", "E")
g.addEdge("D", "E")
g.addEdge("D", "F")
g.addEdge("E", "F")
g.depthFirstRecursive("A")