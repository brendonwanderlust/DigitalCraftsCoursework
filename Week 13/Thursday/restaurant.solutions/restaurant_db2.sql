-- restaurants by distance
select
	*
from
	restaurant
order by
	distance;

-- restaurants by top 2 - closest 2
  select
  	*
  from
  	restaurant
  order by
  	distance
  limit 2;

-- top 2 restaurants by stars
  select
  	*
  from
  	restaurant
  order by
  	stars desc
  limit 2
  ;


-- top 2 restaurants by stars and less than 2 miles away
  select
  	*
  from
  	restaurant
  where
  	distance <= 2
  order by
  	stars desc
  limit 2
  ;

-- number of restaurants
  select count(*) from restaurant;

-- number of restaurants
  select category, count(*) from restaurant group by category;

-- avg star by category
  select category, avg(stars) from restaurant group by category;

-- max star by category
  select category, max(stars) from restaurant group by category;
