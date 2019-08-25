function [x,y,z,e] = load_slice_xyie(filename, bg)
% [x,y,z,e] = load_slice_xyie(filename, bg)
fid = fopen(filename, 'rt');
y = 0;
test = 0;
count = 1;
x = 0;
storez = 0;
storee = 0;
s =0;
countx = 1;
county = 1;
countz = 1;
counte = 1;
next = 0;
while feof(fid) == 0
   tline = fgetl(fid);
   if (count == 1)
       num_steps = str2num(tline);
       z= zeros(num_steps(2),num_steps(1));
       e= zeros(num_steps(2),num_steps(1));       
   end
  
  
   % reading in the x values
   if ((count >2) && (count<=num_steps(1)+2))
       x(countx) = str2num(tline);
       countx = countx+1;
   end
  
   % reading in the y values
   if ((count > num_steps(1)+3) && (count<= num_steps(2)+num_steps(1)+3))
       y(county) = str2num(tline);
       county = county+1;
   end
   
   % reading in the intensities
   if ((count > num_steps(2)+num_steps(1)+4) && (next == 0))
       s = s+size(str2num(tline),2);
       if (s==0)
           next = 1;
           continue;
       end
       storez = [storez,str2num(tline)];
       if((mod(s, num_steps(1)) == 0))
           z(countz,:) = storez(2:end);
           countz = countz+1;
           s = 0;
           storez = 0;
       end
   end

   % reading in the errors
   if (next==1)
       s = s+size(str2num(tline),2);
       if (s==0)
           continue;
       end

       storee = [storee,str2num(tline)];
       if((mod(s, num_steps(1)) == 0))
           e(counte,:) = storee(2:end);
           counte = counte+1;
           s = 0;
           storee = 0;
       end
   end
       
   
   count = count+1;

end
fclose(fid);

% try setting the large negative numbers to nans:
for i=1:size(z,1)
    for j = 1:size(z,2)
        if (z(i,j) < -1e3)
%             z(i,j) = nan;
            z(i,j) = 0;

        end
    end
end


end