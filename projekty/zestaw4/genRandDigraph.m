function d = genRandDigraph(n, p)
%GENRANDDIGRAPH Generate random digraph
%   Generate random digraph with n nodes and probability p that two nodes
%   are connected
    A = zeros(n);
    for i=1:n
        for j=1:n
            if i==j
                continue;
            end
            if rand() <= p
                A(i,j) = 1;
            end
        end
    end
    d = Digraph(A);
end

