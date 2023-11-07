/*
Using the Pagila database:

Find all the cities which begin with “al”
Find all the actors whose first name doesn't end in “EN”
Find all the actors whose first name doesn't end in “EN” and have an ID greater than 100
Find all the actors whose first name doesn't end in “EN”, have an ID greater than 100, and have a last name that ends in “D”. Order the results by the last name in descending order.
Return only the address of addresses in either the Alberta or QLD district
Find actors who's first name begins with “MI” or last name ends with “ING”
What's the difference in results if you use an AND instead of an OR?
Return film titles and descriptions of films whose lengths are between 80 and 100 minutes,
Return film titles and descriptions of films whose lengths are between 80 and 100 minutes. 
Further filter these results by films which have a rental period between 5 and 7 days 
or have a replacement cost between $17 and $22

*/



SELECT title, description FROM film
WHERE length BETWEEN 80 AND 100 
      AND rental_duration BETWEEN 5 AND 7
      OR replacement_cost BETWEEN 17 AND 22;
