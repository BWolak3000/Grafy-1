function [result, d, p] = bellmanford(g, s)
%BELLMANFORD 
%     Bellman_Ford(G, w, s) // n – liczba wierzchołków
%     1. Init(G, s)
%     2. for i = 1 to n − 1
%     3. do for każda krawędź (u, v) należąca do grafu G
%     4. do Relax(u, v, w)
%     5. for każda krawędź (u, v) należąca do grafu G
%     6. do if ds(v) > ds(u) + w(u, v)
%     7. then return False // W grafie jest cykl o ujemnej wadze osiągalny ze źródła s
%     8. return True
    nodes = g.Nodes(1, :);
% INIT(G, s):
% 1. for każdy wierzchołek v należący do grafu G
% 2. do ds(v) = ∞
% 3. ps(v) = Nil
% 4. ds(s) = 0
    p = zeros(1, length(nodes));
    d = inf*ones(1, length(nodes));
    d(s) = 0;
    edges = g.Edges;
    for i=1:length(nodes)-1
        for j=1:length(edges(1,:))
            u = edges(1, j);
            v = edges(2,j);
            w_uv = edges(3,j);
            % Relax(u, v, w) // u, v - wierzchołki połączone krawędzią (u, v) poddaną relaksacji; w - wagi
            % 1. if ds(v) > ds(u) + w(u, v)
            % 2. then ds(v) = ds(u) + w(u, v)
            % 3. ps(v) = u
            if d(v) > d(u) + w_uv
                d(v) = d(u) + w_uv;
                p(v) = u;

            end
        end
    end
    for j=1:length(edges(1,:))
        u = edges(1, j);
        v = edges(2,j);
        w_uv = edges(3,j);
        if d(v) > d(u) + w_uv
            result = false;
            return; 
        end
    end
    result = true;
end



