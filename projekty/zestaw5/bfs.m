function [ds, ps] = bfs(flownet, s)
%BFS
%     BFS(G,s)
%     1. for każdy wierzchołek v należący do grafu G
%     2. do ds(v) = ∞ // Wszystkie wierzchołki są nieodwiedzone.
%     3. ps(v) = Nil
%     4. ds(s) = 0
%     5. Utwórz pustą kolejkę Q
%     6. Dodaj s do kolejki Q
%     7. while Q 6= Ø // Dopóki kolejka nie jest pusta
%     8. do Ściągnij wierzchołek z początku kolejki i przypisz go do v
%     9. for każdy wierzchołek u ∈ G będący sąsiadem v
%     10. do if ds(u) == ∞
%     11. then ds(u) = ds(v) + 1
%     12. ps(u) = v
%     13. Dodaj u do kolejki Q
    n = length(flownet.Nodes);
    ds = inf.*ones(1,n);
    ps = zeros(1,n);
    ds(s) = 0;
    Q = [s];
    A = flownet.getAdjacencyMatrix();
    while ~isempty(Q)
        v = Q(1);
        Q = Q(2:end);
        u = 1:n;
        u = u(A(v,:)~=0);
        for i=u
            if ds(i) == inf
                ds(i) = ds(v) + 1;
                ps(i) = v;
                Q = [Q, i];
            end
        end
    end
end

