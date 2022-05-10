function [nr, comp] = componentsr(nr, v, gt, comp)
%COMPONENTSR 
%     Components_R(nr, v, GT, comp)
%     1. for każdy wierzchołek u ∈ GT będący sąsiadem v
%     2. do if comp[u] == −1
%     3. then comp[u] = nr
%     4. Components_R(nr,u, GT, comp)
    A = gt.getAdjacencyMatrix();
    u = 1:length(gt.Nodes(1,:));
    u = u(A(v,:)==1);
    for i=1:length(u)
        if comp(u(i)) == -1
            comp(u(i)) = nr;
            [nr, comp] = componentsr(nr, u(i), gt, comp);
        end
    end
end

