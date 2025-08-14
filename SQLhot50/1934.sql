-- Write your PostgreSQL query statement below
select s.user_id,
coalesce(
    round(
        cast(sum(case when c.action='confirmed' then 1 else 0 end) as numeric)
        /
        nullif(count(c.action),0)
    ,2)
,0.00) as confirmation_rate


from signups s
left join confirmations c
    on s.user_id=c.user_id
group by s.user_id
order by s.user_id

-- coalesce(a,b) 如果a为null 则b为0.00
-- round(a,2) (保留两位小数)
-- cast(... as numeric) 将里面的内容转化为浮点数
-- sum(case when xx then a else b end) 求和满足条件的数量
-- nullif(xx,0)如果xx为null则变为0
