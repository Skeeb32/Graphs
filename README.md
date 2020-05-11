# Graphs!

## Objectives

* [Graph Intro](objectives/graph-intro)
* [Graph Representations](objectives/graph-representations)
* [Breadth First Search](objectives/breadth-first-search)
* [Depth First Search](objectives/depth-first-search)
* [Randomness](objectives/randomness)
* [Connected Components](objectives/connected-components)

## Projects

### Day 1
* [Graph Traversal and Search](projects/graph)
What are graphs?
    Graphs are collections of related data represented by nodes and connections between nodes. 
    Trees can be a type of graph, except connections can be made from any node to any other node, even forming loops. 
    By this definition, all trees are grpahs, but not all grpahs are trees. 
    We call the nodes in a graph vertexes (or vertices or verts). and we call the connections between the verts edges. An edge denotes a relationship or linkage between to the verts.
        Nodes or vertices - represent objects in a data (cities, animals, web pages)
        Edges - connections between vertices; can be bidirectional
        Weight - cost to travel across edges
    Cyclic graph - edges allow you to revist at least one vert 
    Acyclic graph - vertices or nodes can only be visited once

Directed and Undirected graphs
    If the relationship of the graph is one way, it is directed. For example, owing money (debt) to someone. Directed graphs can also be bidirectional. Road maps are directed since all roads are one-way, howevever most streets consists of roads in both directions. 
    If the relationship is mutual, meaning going back and forth, or have an exchange relationship it is undirected.

Weighted Graphs
    Have values associated with the edges. The weigths represent different data in different graphs. Given a certian situation in a certain curcumstance weights may represent a higher or lower value assocaited with the graphs output. Weights can be modified. 

Directed Acyclic Graphs (DAGs)
A directed acyclic graph is a directed graph with no cylces. We can order the graph;s vertices lineraly where every edge is directed from earlier to later in a give sequence. 

What is the difference between a traversal and a search?
    In a traverse you visit all the vertex, in search once you find what you're looking for you stop.
    Traversal goes through all and search stops when you find its target. 

What type of graph does GIT use to store things?
    Directed asylic.
When would you want to use an adjacency matrix instead of an adjacency list?
    When dense - weight
Why are we using a set to keep track of our edges?
    Cant contain duplicates. We're only going to have one connection of each edge. 0(1).
What's the difference between a traversal and a search?
    In a search you visit till you find a traverse you visit all the vertexs.


### Day 2
* [Earliest Ancestor](projects/ancestor)

### Day 3
* [Random Social Network](projects/social)

### Day 4
* [Adventure Map Traversal](projects/adventure)
