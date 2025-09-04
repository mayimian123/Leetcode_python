-- Write your PostgreSQL query statement below
select p.product_id, 
COALESCE(ROUND(sum(u.units*p.price)::numeric/nullif(sum(u.units),0),2),0) as average_price
from Prices p
left join unitsSold u
on p.product_id=u.product_id
and u.purchase_date between p.start_date and p.end_date
group by p.product_id

-- 需要重新写一遍！
-- 核心是line3 
    -- COALESCE 就是拿第一个有效值，如果全是空就用备用值。
        -- 在这里的case中 如果 coalesce(null,0) 则返回0
    -- ::numeric  可以把数值升级成可以带小数的精确数字，保证除法或计算不丢精度。
        -- 这里的需要转换的原因是 ROUND函数要求里面的内容格式为：ROUND(numeric, integer) 
    -- Round 结果保留两位小数 
--