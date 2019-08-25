clear;

%[x,y,I,e] = load_slice_xyie('./NCCF_elastic_folded.xyie');
[x,y,I,e] = load_slice_xyie('./newData/1K0Slice_Integratedpm0p1.xyie');




[X,Y] = meshgrid(x,y);


M = zeros(size(X,1)*size(X,2),3);
n = 1;
for ii = 1:size(X,1)
    for jj = 1:size(X,2)
        M(n,1) = X(ii,jj);
        M(n,2) = Y(ii,jj);
        M(n,3) = I(ii,jj);
        n = n+1;
    end
end




csvwrite('Data_From_1K0Slice_Integratedpm0p1.csv',M);

figure;
h = surf(x,y,I)
set(h,'EdgeColor','none');
