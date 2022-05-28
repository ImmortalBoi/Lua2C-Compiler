function search(num)
    -- table_1={1,8,9,6,2,3,8,4,2,9,5}
    for i=1 , 20 ,1 do            
    if(table_1[i]==num) then 
        print("Element found at index:",i)
        break
    end
    end
end

table_1={1,8,9,6,2,3,8,4,2,9,5}    --start element 1
number=search(9)

--io.write("Enter number:")
--num=io.read()