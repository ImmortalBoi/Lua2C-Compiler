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
-- -- -- fibonacci function with cache
-- -- -- "" "" ""
-- -- --[[
-- -- 	testing multiLine comments
-- -- ]]

-- -- -- very inefficient fibonacci function
-- -- function fib(n)
-- -- 	N=N+1
-- -- 	if n<2 then
-- -- 		return n
-- -- 	else
-- -- 		return fib(n-1)+fib(n-2)
-- -- 	end
-- -- end

-- -- -- a general-purpose value cache
-- -- function cache(f)
-- -- 	local c={}
-- -- 	return function (x)
-- -- 		local y=c[x]
-- -- 		if not y then
-- -- 			y=f(x)
-- -- 			c[x]=y
-- -- 		end
-- -- 		return y
-- -- 	end
-- -- end

-- -- -- run and time it
-- -- function test(s,f)
-- -- 	N=0
-- -- 	local c=os.clock()
-- -- 	local v=f(n)
-- -- 	local t=os.clock()-c
-- -- 	print(s,n,v,t,N)
-- -- end

-- -- n=arg[1] or 24		-- for other values, do lua fib.lua XX
-- -- n=tonumber(n)
-- -- print("","n","value","time","evals")
-- -- test("plain",fib)
-- -- fib=cache(fib)
-- -- test("cached",fib)
-- local dump
-- X = 0
-- function dump(o)
-- 	if type(o) == 'table' then
-- 		local s = '{ '
-- 		for k,v in pairs(o) do
-- 			if type(k) ~= 'number' then k = '"'..k..'"' end
-- 			s = s .. '['..k..'] = ' .. dump(v) .. ','
-- 		end
-- 		return s .. '} '
-- 	else
-- 		return tostring(o)
-- 	end
-- end
-- local people = {
-- {
-- 	name = "Fred",
-- 	address = "16 Long Street",
-- 	phone = "123456"
-- },

-- {
-- 	name = "Wilma",
-- 	address = "16 Long Street",
-- 	phone = "123456"
-- },

-- {
-- 	name = "Barney",
-- 	address = "17 Long Street",
-- 	phone = "123457"
-- }

-- }

-- print("People:", dump(people))