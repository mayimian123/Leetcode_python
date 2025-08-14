select e.name
from employee e
where e.id in(
    select managerId
    from employee
    where managerId is not null
    group by managerId
    having count(*)>=5
);

-- 用外层查询+内层查询