select p.product_name as product_name,s.year as year, s.price
from sales s 
left join product p 
on s.product_id = p.product_id