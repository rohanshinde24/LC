select p.firstName as firstName, p.lastname as lastName, a.city as city, a.state as state 
from Person p 
left join Address a
on p.personId = a.personId;