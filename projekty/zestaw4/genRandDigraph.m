function d = genRandDigraph(n, p)
%GENRANDDIGRAPH Generate random digraph
%   Generate random digraph with n nodes and probability p that two nodes
%   are connected
    if p<0 || p>1
        error("Propability out of range [0, 1]");
    end
    if n<=0
        error("Number of vertices to small! Must be >= 1");
    end
    A = rand(n);
    A = A<=p;
    A = A&(~eye(n));
    d = Digraph(A);
end

