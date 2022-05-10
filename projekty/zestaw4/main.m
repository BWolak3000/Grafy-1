close all; clear; clc;

n = 10;
p = 0.3;
digraph1 = genRandDigraph(n, p);
digraph1t = digraph1.transpose();
subplot(1, 2, 1);
plot(digraph1);
subplot(1, 2, 2);
plot(digraph1t);
comp = kosaraju(digraph1)
if max(comp)==1
    noEdges = length(digraph1.Edges(1,:));
    weights = randi(10,[1, noEdges]);
    noEdgesMinus= round(sqrt(n));
    for i=1:noEdgesMinus
        weights(randi(noEdges)) = -randi(5);
    end
    digraph1.Edges = [digraph1.Edges; weights];
    plot(digraph1.getDigraph(),'EdgeLabel',weights);
    [D, P] = johnson(digraph1)
else
    error("Digraf nie jest silnie spójny! Proszę spróbować inny")
end