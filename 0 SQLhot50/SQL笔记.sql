limit 5 --可以只选择展示5个数据
offset 10 -- 不展示前10个数据 展示11开始往后的

order by 字段名 --将字段名进行整合
order by 字段名1， 字段名2 --现将字段名1进行分类 再进行字段名2的分类。优先的分类放在前面
order by 字段名 desc --降序呈现
order by 字段名 asc  --升序呈现

where 字段名 like '张_' --会回传含有张+一个字的名字
where 字段名 like '张%' --会回传含有张+很多东西的名字
where 字段名 between xx and xx

where score between 80 and 90 and (class='1' or class='2')
where score between 80 and 90 and (class in ('1','2'))

select avg(score), sum(score), max(score), min(score), count(score) --count求数量
from students

select round(avg(score),2) as average -- 两位小数
select rounc(avg(score))   as average -- 整数

select round(avg(score),2) as average
from students
group by class
order by average desc; -- 按照班级分类求平均分 并且按照平均分降序呈现
-- select 选取
-- from 来源
-- where 分组前过滤
-- group by 分组
-- having 分组后过滤
-- order by 最后结果排序
-- limit 笔数限制

select round(avg(score),2) as average
from students
group by class
having average>=80
order by average desc; -- 按照班级分类求平均分 并且按照平均分降序呈现

————————————
select count(*) -- line numbers
from students;

select count(class) --line numbers except null
from students

select count(distinct class) --different line numbers 
from students

select distinct class -- different line with null

select distinct class --different class without null
from students
where class is not null
order by class

-------------

create table clubs(  --create table
clubnumber int primary key,
clubname varchar(15),
)

droup table clubs --delete club

insert into clubs(xx,xx)
values (101,'x')

update clubs
set clubname='dance'
where clubnumber='104'

delete
from clubs
where clubnumber=''

-------------------
 join w2 ON w1.recordDate = w2.recordDate - INTERVAL '1 day'
 -- w1的日期和w2的前一天日期匹配 interval是在pgsql里面表示时间间隔的数据类型 
 select date'2025-08-17'-interval'1 day'
 -- return 2025-08-16

-------------------
--1661
select start.machine_id, round(avg(end.timestamp-start.timestamp),3) processing_time
from
(select  *
from Activity
where activity_type ='start') as start
join
(select   *
from Activity
where activity_type ='end') as end
on
start.machine_id=end.machine_id and start.process_id=end.process_id
group by start.machine_id


