-- HiveQL code to find the order for the
-- tablet (product ID 1274348) from the 
-- contest winner (customer ID 1139477)
SELECT o.order_id, fname, lname, o.order_date 
FROM customers c 
JOIN orders o 
   ON (c.cust_id = o.cust_id) 
JOIN order_details d 
   ON (o.order_id = d.order_id) 
WHERE d.prod_id=1274348
  AND c.cust_id=1139477;
