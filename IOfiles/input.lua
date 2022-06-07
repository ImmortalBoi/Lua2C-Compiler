table_1={1,2,3,4,5}
even=0
odd=0
for i=1 ,5, 1 do 
    if(table_1[i]%2==0) then
        even=even+1
        else
            odd=odd+1
    end
end
    print("Even number =",even)
    print("Odd number =",odd)

