function [d, p] = dijkstra(g, w, s)
%DIJKSTRA 
%     Dijkstra(G, w, s)
%     1. Init(G, s)
%     2. S = ∅ // S - zbiór “gotowych” wierzchołków; na początku jest pusty
%     3. while S 6= zbiór wszystkich wierzchołków G
%     4. do u = wierzchołek o najmniejszym ds(u) spośród niegotowych wierzchołków: u /∈ S
%     5. S = S ∪ u
%     6. for każdy wierzchołek v /∈ S będący sąsiadem u
%     7. do Relax(u, v, w)
    nodes = g.Nodes(1, :);
    n = length(nodes);
% INIT(G, s):
% 1. for każdy wierzchołek v należący do grafu G
% 2. do ds(v) = ∞
% 3. ps(v) = Nil
% 4. ds(s) = 0
    p = zeros(1, n);
    d = inf*ones(1, n);
    d(s) = 0;
    S=[];
    isEqual = false;
    while ~isEqual
        if sum(size(S) == size(nodes)) == 2
            if sum(sort(S) == nodes) == n
                isEqual = true;
                break;
            end
        end
        Si = true(1, n);
        for i=S
            Si(i)=false;
        end
        infarr = inf.*ones(1, n);
        infarr(Si) = 0;
        tempd = d + infarr;
        [~, u] = min(tempd);
        S = [S, u];
        A = g.getAdjacencyMatrix();
        v = 1:n;
        % fprintf(1, "v: %d\t", v);
        filter = A(u,:)~=0;
        filter = logical(filter.*Si);
        v = v(filter);
        for i=v
            % Relax(u, v, w) // u, v - wierzchołki połączone krawędzią (u, v) poddaną relaksacji; w - wagi
            % 1. if ds(v) > ds(u) + w(u, v)
            % 2. then ds(v) = ds(u) + w(u, v)
            % 3. ps(v) = u
            edgefilter = g.Edges(1,:)==u;
            edgefilter = edgefilter.*(g.Edges(2,:)==i);
            edgepos = vec2ind(edgefilter');
            if d(i) > d(u) + w(edgepos)
                d(i) = d(u) + w(edgepos);
                p(i) = u;
            end
        end
    end
    
end

