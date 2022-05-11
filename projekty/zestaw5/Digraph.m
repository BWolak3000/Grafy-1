classdef Digraph
    %DIGRAPH Class representing directed graphs
    %   Class representing directed graphs with support to
    %   all 2 common representation methods:
    %   adjacency matrix
    %   incidency matrix
    
    properties
        Edges; % [s;t;weight];
        Nodes; % [indexes];
    end
    
    methods(Access=private)
        function obj = fromLogicalAdjacencyMatrix(obj, matrix)
            msize = size(matrix);
            e=1;
            for i=1:msize(1)
                for j=1:msize(2)
                    if(matrix(i,j))
                        obj.Edges(:, e) = [i; j];
                        e=e+1;
                    end
                end
            end
        end
        function obj = fromIncidencyMatrix(obj, matrix)
            msize = size(matrix);
            for j=1:msize(2)
                s = vec2ind(matrix(:, j)==-1);
                f = vec2ind(matrix(:, j)==1);
                obj.Edges(:,j) = [s;f];
            end
        end
        function obj = fromAdjacencyMatrix(obj, matrix)
            msize = size(matrix);
            e=1;
            for i=1:msize(1)
                for j=1:msize(2)
                    if(matrix(i,j))
                        obj.Edges(:, e) = [i; j; matrix(i,j)];
                        e=e+1;
                    end
                end
            end
        end
    end
    
    methods
        function obj = Digraph(matrix)
            %DIGRAPH Construct an instance of this class
            %   Basic constructor capable of using adjacency matrix
            %   and incidency matrix
            msize = size(matrix);
            z = matrix==0;
            o = matrix==1;
            mo = matrix==-1;
            if sum(z+o, 'all') == msize(1)*msize(2)
                matrix = logical(matrix);
                obj.Nodes = 1:msize(1);
                if msize(1) == msize(2)
                    obj.Edges = zeros(2, sum(matrix, 'all'));
                    obj = fromLogicalAdjacencyMatrix(obj, matrix);
                else
                    error('Adjacency matrix is not square');
                end
            elseif sum(z+o+mo, 'all') == msize(1)*msize(2)
                obj.Nodes = 1:msize(1);
                obj.Edges = zeros(2, msize(2));
                obj = fromIncidencyMatrix(obj, matrix);
                
            else    
                if msize(1) == msize(2)
                    obj.Edges = zeros(3, sum(matrix~=0, 'all'));
                    obj = fromAdjacencyMatrix(obj, matrix);
                else
                    error('Adjacency matrix is not square');
                end
            end
            
        end
        
        function d = getDigraph(obj)
            %GETDIGRAPH Converter to matlab digraph representation
            e = obj.Edges;
            esize = size(e);
            if esize(1) > 2
                d = digraph(e(1,:), e(2,:), e(3, :));
            else
                d = digraph(e(1,:), e(2,:));
            end
        end
        
        function A = getAdjacencyMatrix(obj)
            %GETADJACENCYMATRIX Converter to adjacency matrix representation
            esize = size(obj.Edges);
            nsize = size(obj.Nodes);
            A = zeros(nsize(2));
            if esize(1)<3
                obj.Edges = [obj.Edges;ones(1,esize(2))];
            end
            for i=1:esize(2)
                A(obj.Edges(1,i), obj.Edges(2,i)) = obj.Edges(3,i);
            end
        end
        
        function In = getIncidencyMatrix(obj)
            %GETINCIDENCYMATRIX Converter to incidency matrix representation
            esize = size(obj.Edges);
            nsize = size(obj.Nodes);
            In = zeros(nsize(2), esize(2));
            for i=1:esize(2)
                In(obj.Edges(1,i), i) = -1;
                In(obj.Edges(2,i), i) = 1;
            end
        end
        
        function handle = plot(obj)
            esize = size(obj.Edges);
            if esize(1) > 2
                d = digraph(obj.Edges(1,:), obj.Edges(2,:), obj.Edges(3, :));
                LWidths = 5*d.Edges.Weight/max(d.Edges.Weight);
                handle = plot(d,'EdgeLabel',d.Edges.Weight,'LineWidth',LWidths);
            else
                d = digraph(obj.Edges(1,:), obj.Edges(2,:));
                handle = plot(d);
            end
        end
        
        function transposed = transpose(obj)
            transposed = obj;
            transposed.Edges = transposed.Edges([2,1,3:end], :);
        end
    end
end

