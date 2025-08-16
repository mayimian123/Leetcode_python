-- Write your PostgreSQL query statement below
select id,movie,description, rating
from cinema
where description !='boring'
and id%2=1
order by rating desc;

-- order by ** desc 降序 asc 升序
-- descending
-- ascending