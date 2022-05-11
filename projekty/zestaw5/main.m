clear; close all; clc;
net = Flownet(2);
plot(net);
[ds, ps] = bfs(net, 1);
[f, resnet] = fordfulkerson(net, 1, length(net.Nodes));
plot(resnet);