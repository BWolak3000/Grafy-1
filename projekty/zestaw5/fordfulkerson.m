function [f, residualnet] = fordfulkerson(flownet, s, t)
%FORDFULKERSON
%     Ford_Fulkerson(G, s, t)
%     1. for każda krawędź (u, v) należąca do grafu G
%     2. do f(u, v) = 0 // Zerowanie przepływów dla wszystkich krawędzi
%     3. while istnieje ścieżka rozszerzająca p z s do t w sieci rezydualnej Gf
%     4. do cf (p) = min{cf (u, v) dla wszystkich krawędzi (u, v) ∈ p}
%     5. for każda krawędź (u, v) ∈ p
%     6. do if krawędź (u, v) należy do grafu G
%     7. then f(u, v) = f(u, v) + cf (p) // Zwiększamy przepływ przez krawędź (u, v)
%     8. else f(v, u) = f(v, u) − cf (p)
    residualnet = flownet.getResidual();
    e = length(flownet.Edges);
    f = zeros(1, e);
    [ds, ps] = bfs(residualnet, s);
    while ps(t) ~= 0
        p = zeros(1, ds(t));
        ebegin = ps(t);
        eend = t;
        for i=ds(t):-1:1
            edgefilter = residualnet.Edges(1,:)==ebegin;
            edgefilter = edgefilter&(residualnet.Edges(2,:)==eend);
            edgepos = vec2ind(edgefilter');
            p(i) = edgepos;
            eend = ebegin;
            ebegin = ps(eend);
        end
        cfp = min(residualnet.Edges(3, p));
        for i=p
            if i<=e
                f(i) = f(i) + cfp;
                residualnet.Edges(3, i) = residualnet.Edges(3, i) - cfp;
                residualnet.Edges(3, i+e) = residualnet.Edges(3, i+e) + cfp;
            else
                f(i-e) = f(i-e) - cfp;
                residualnet.Edges(3, i) = residualnet.Edges(3, i) - cfp;
                residualnet.Edges(3, i-e) = residualnet.Edges(3, i-e) + cfp;
            end
        end
        [ds, ps] = bfs(residualnet, s);
    end
end

