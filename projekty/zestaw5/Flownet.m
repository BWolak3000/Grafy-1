classdef Flownet < Digraph
    %FLOWNET Custom digraph representing flow network
    %   Extension of the Dirgaph class
    
    properties
        NumberOfLayers
        Layers
    end
    
    methods
        function obj = Flownet(N)
            %FLOWNET Construct flow network of N layers
            obj@Digraph([]);
            obj.NumberOfLayers = N;
            obj.Layers = cell(1,N);
            obj.Nodes = [1];
            lastid = 1;
            for i=1:N
                amount = randi([2, N]);
                obj.Nodes = [obj.Nodes, lastid+1:lastid+amount];
                obj.Layers{i} = lastid+1:lastid+amount;
                lastid = lastid+amount;
            end
            obj.Nodes = [obj.Nodes, lastid+1];
            n = length(obj.Nodes);
            npl = length(obj.Layers{1});
            obj.Edges = [ones(1, npl);obj.Layers{1}; randi(10, [1, npl])];
            for i=1:N-1
                li = length(obj.Layers{i});
                li1 = length(obj.Layers{i+1});
                [k, side]= min([li, li1]);
                newEdges = [...
                   obj.Layers{i}(randperm(li, k));...
                   obj.Layers{i+1}(randperm(li1, k));...
                   randi(10, [1, k])
                ];
                obj.Edges = [obj.Edges,newEdges];
                cside = mod(side, 2) + 1;
                leftVer = setdiff(obj.Layers{i+cside-1}, newEdges(cside, :));
                mini = min(obj.Layers{i+side-1});
                maxi = max(obj.Layers{i+side-1});
                randVer = randi([mini, maxi], 1, length(leftVer));
                newEdges = [...
                   leftVer;...
                   randVer;...
                   randi(10, [1, length(leftVer)])
                ];
                newEdges = newEdges([cside, side, 3], :);
                obj.Edges = [obj.Edges,newEdges];
            end
            npl = length(obj.Layers{N});
            obj.Edges = [obj.Edges,[obj.Layers{N};n*ones(1, npl); randi(10, [1, npl])]];
            A = obj.getAdjacencyMatrix();
            count = 0;
            while count < 2*N
                u = randi([1, n-1]);
                v = randi([2, n]);
                if u==v
                    continue;
                elseif A(u,v) ~= 0
                    continue;
                else
                    A(u, v) = randi(10);
                    count = count + 1;
                end
            end
            temp = Digraph(A);
            obj.Edges = temp.Edges;
        end
        
        function handle = plot(obj)
            esize = size(obj.Edges);
            n = length(obj.Nodes);
            x = zeros(1, n);
            y = zeros(1, n);
            middle = length(obj.Layers{1})/2;
            y(1) = middle;
            y(n) = middle;
            x(n) = obj.NumberOfLayers+1;
            lastid = 2;
            for i=1:obj.NumberOfLayers
                npl = length(obj.Layers{i});
                offset = middle-npl/2+rand()-0.5;
                x(lastid:lastid+npl-1) = i;
                for j=1:npl
                    y(lastid) = offset + (j-1);
                    lastid = lastid + 1;
                end
            end
            d = digraph(obj.Edges(1,:), obj.Edges(2,:), obj.Edges(3, :));
            LWidths = 5*d.Edges.Weight/max(d.Edges.Weight);
            handle = plot(d,'NodeColor','m','EdgeLabel',d.Edges.Weight,'LineWidth',LWidths, 'XData', x, 'YData', y);
        end
    end
end

