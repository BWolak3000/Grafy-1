function [D, P] = johnson(g)
%JOHNSON
%     Johnson(G, w) // n – liczba wierzchołków grafu G
%     1. G0 =Add_s(G)
%     2. if Bellman_Ford(G0
%     , w, s)==False
%     3. then ERROR // G zawiera cykl o ujemnej wadze
%     4. else for każdy wierzchołek v należący do G0
%     5. do h(v) = ds(v) // ds(v) - długość najkrótszej ścieżki s → v obliczona w 2. kroku
%     6. for każda krawędź (u, v) należąca do grafu G0
%     7. do wb(u, v) = w(u, v) + h(u) − h(v)
%     8. Utwórz macierz D rozmiaru n × n, gdzie Du,v to długość najkrótszej ścieżki u → v w G
%     9. for każdy wierzchołek u należący do G
%     10. do Dijkstra(G, w, u b ) // aby obliczyć dbu(v) dla każdego v należącego do G
%     11. for każdy wierzchołek v należący do G
%     12. do Du,v = dbu(v) − h(u) + h(v)
%     13. return D

    n = length(g.Nodes);
    s = n+1;
% Add_s(G) // n – liczba wierzchołków grafu G
% 1. Utwórz G0 = G ∪ s
% 2. for każdy wierzchołek v należący do G
% 3. do Dodaj krawędź (s, v) do G0
% 4. w(s, v) = 0
% 5. return G0
    gp = g;
    gp.Nodes = [g.Nodes, s];
    newEdges = zeros(3, n);
    for i=1:n
        newEdges(1:2,i)=[s;i];
    end
    gp.Edges = [gp.Edges, newEdges];
% -----------------------------------------
    [isValid, h, ~] = bellmanford(gp, s);
    wb = gp.Edges(3, :);
    if isValid
        for i=1:length(wb)
            wb(i) = wb(i) + h(gp.Edges(1, i)) - h(gp.Edges(2, i));
        end
        D = zeros(n);
        P = zeros(n);
        for i=1:n
            [dp, pp] = dijkstra(g, wb, i);
            for j=1:n
                D(i,j) = dp(j) - h(i) + h(j);
            end
            P(i,:) = pp; 
        end
    else
        error("Digraf zawiera ujemny cykl");
    end
end

