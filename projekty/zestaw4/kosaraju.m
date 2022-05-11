function [comp] = kosaraju(d)
%KOSARAJU Kosaraju algorithm
%     1. for każdy wierzchołek v należący do G
%     2. do d[v] = −1 // d[v] - czas odwiedzenia wierzchołka v. d[v] == −1 oznacza nieodwiedzony.
%     3. f[v] = −1 // f[v] – czas przetworzenia wierzchołka v.
%     4. t = 0
%     5. for każdy wierzchołek v należący do G
%     6. do if d[v] == −1
%     7. then DFS_visit(v, G, d, f, t)
%     8. Utwórz graf GT, będący transpozycją grafu G // W GT zwroty krawędzi są odwrócone.
%     9. nr = 0 // nr – numer spójnej składowej.
%     10. for każdy wierzchołek v należący do grafu GT
%     11. do comp[v] = −1 // Wszystkie wierzchołki są nieodwiedzone.
%     12. for każdy wierzchołek v należący do grafu GT w kolejności malejących czasów f[v]
%     13. do if comp[v] == −1
%     14. then nr = nr + 1
%     15. comp[v] = nr
%     16. Components_R(nr, v, GT, comp)
%     17. return comp
    noV = length(d.Nodes);
    md = -ones(1, noV);
    f = -ones(1, noV);
    t = 0;
    for i=1:noV
        if md(i) == -1
           [md, f, t] =  dfsvisit(i, d, md, f, t);
        end
    end
    dt = d.transpose();
    nr = 0;
    noVt = length(dt.Nodes);
    comp = -ones(1, noVt);
    [~, orderu] = sort(f, 'descend');
    for i=1:noVt
        u = dt.Nodes(orderu(i));
        if comp(u) == -1
            nr = nr + 1;
            comp(u) = nr;
            [nr, comp] = componentsr(nr, u, dt, comp);
        end
    end
end

