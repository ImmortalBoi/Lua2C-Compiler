table_1={1,2,3,4,5}
max=table_1[1]
min=table_1[1]
for i=1 ,5, 1 do 
    if(table_1[i]>max) then
        max= table_1[i]
        elseif(table_1[i]<min) then
            min=table_1[i]
    end
end
    print("maximum number =",max)
    print("miimum number =",min)