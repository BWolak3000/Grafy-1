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
            %   Detailed explanation goes here
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
            n = obj.Nodes;
            e = obj.Edges;
            esize = size(e);
            nsize = size(n);
            A = zeros(nsize(2));
            if esize(1)<3
                e = [e;ones(1,esize(2))];
            end
            for i=1:esize(2)
                A(e(1,i), e(2,i)) = e(3,i);
            end
        end
        
        function In = getIncidencyMatrix(obj)
            %GETINCIDENCYMATRIX Converter to incidency matrix representation
            n = obj.Nodes;
            e = obj.Edges;
            esize = size(e);
            nsize = size(n);
            In = zeros(nsize(2), esize(2));
            for i=1:esize(2)
                In(e(1,i), i) = -1;
                In(e(2,i), i) = 1;
            end
        end
        
        function handle = plot(obj)
            e = obj.Edges;
            esize = size(e);
            if esize(1) > 2
                d = digraph(e(1,:), e(2,:), e(3, :));
                LWidths = 5*d.Edges.Weight/max(d.Edges.Weight);
                handle = plot(d,'EdgeLabel',d.Edges.Weight,'LineWidth',LWidths);
            else
                d = digraph(e(1,:), e(2,:));
                handle = plot(d);
            end
            
        end
        
        function transposed = transpose(obj)
            transposed = obj;
            s=transposed.Edges(1,:);
            t=transposed.Edges(2,:);
            w=transposed.Edges(3:end,:);
            transposed.Edges = [t;s;w];
        end
    end
end

