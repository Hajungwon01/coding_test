select title
from 
(
  SELECT * 
  from film
  where rating = 'NC-17' or rating ='R'
)
where title not like '%A' 
    AND title not like '%E'
    AND title not like '%I'
    AND title not like '%O'
    AND title not like '%U';   