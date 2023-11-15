select 
p.product_name as product_name, 
sum(o.unit) as unit
from Products p 
left join Orders o 
on p.product_id = o.product_id
where year(o.order_date) = '2020' and month(o.order_date) = '02'
group by product_name
having sum(o.unit)>=100
