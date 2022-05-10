function [d, f, t] = dfsvisit(v, G, d, f, t)
%DFSVISIT 
%   DFS_visit(v, G, d, f, t)
%   1. t = t + 1
%   2. d[v] = t
%   3. for każdy wierzchołek u ∈ G będący sąsiadem v // Przejście po krawędzi (v, u)
%   4. do if d[u] == −1
%   5. then DFS_visit(u, G, d, f, t)
%   6. t = t+ 1 // Zwiększona wartość t musi być zapamiętana – można np. przekazywać t przez referencję.
%   7. f[v] = t
    t = t + 1;
    d(v) = t;
    A = G.getAdjacencyMatrix();
    u = 1:length(G.Nodes(1,:));
    % fprintf(1, "v: %d\t", v);
    u = u(A(v,:)==1);
    for i=1:length(u)
        if d(u(i)) == -1
            [d, f, t] = dfsvisit(u(i), G, d, f, t);
        end
    end
    t = t + 1;
    f(v) = t;
end

