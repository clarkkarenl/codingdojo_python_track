-- Assignment:  Lead Gen Business
-- Karen Clark
-- 2018-06-23

-- Queries
-- 1. What query would you run to get the total revenue for March of 2012?
SELECT sum(amount) 
FROM billing 
WHERE 
charged_datetime BETWEEN '2012-03-01' AND '2012-03-31';

-- 2. What query would you run to get total revenue collected from the client with an id of 2?
SELECT sum(amount) 
FROM billing
WHERE 
client_id = 2;

-- 3. What query would you run to get all the sites that client=10 owns?
SELECT * 
FROM sites 
WHERE 
client_id = 10;

-- 4. What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client=20?
SELECT DATE_FORMAT(created_datetime, '%Y') AS 'year'
, DATE_FORMAT(created_datetime, '%m') AS 'month'
, count(distinct(site_id)) AS 'total' 
FROM sites
GROUP BY DATE_FORMAT(created_datetime, '%Y%m');

-- 5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?
SELECT count(leads_id) 
FROM leads
WHERE 
registered_datetime BETWEEN '2011-01-01' AND '2011-02-15';

-- 6. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?
SELECT CONCAT_WS(' ', clients.first_name,clients.last_name) as client_name
,  count(leads.leads_id)
FROM clients
  JOIN sites on sites.client_id = clients.client_id
  JOIN leads on leads.site_id = sites.site_id
WHERE
  leads.registered_datetime BETWEEN  '2011-01-01' AND '2011-12-31'
GROUP BY client_name;

-- 7. What query would you run to get a list of client names and the total # of leads we've generated for each client each month between months 1 - 6 of Year 2011?
SELECT DATE_FORMAT(registered_datetime, '%m') as month
, CONCAT_WS(' ', clients.first_name,clients.last_name) as client_name
, count(leads.leads_id) as num_leads
FROM clients
  JOIN sites on sites.client_id = clients.client_id
  JOIN leads on leads.site_id = sites.site_id
WHERE
  leads.registered_datetime BETWEEN '2011-01-01' AND '2011-06-30'
GROUP BY DATE_FORMAT(registered_datetime, '%m');

-- 8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites between January 1, 2011 to December 31, 2011? Order this query by client id.  Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.
-- query #1 --
SELECT CONCAT_WS(' ', clients.first_name,clients.last_name) as client_name
, count(leads.leads_id) as num_leads
FROM clients
  JOIN sites on sites.client_id = clients.client_id
  JOIN leads on leads.site_id = sites.site_id
WHERE
  leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY clients.client_id
ORDER BY clients.client_id;

-- query #2 --
SELECT CONCAT_WS(' ', clients.first_name,clients.last_name) as client_name
, sites.domain_name
, count(leads.leads_id) as num_leads
FROM clients
  JOIN sites on sites.client_id = clients.client_id
  JOIN leads on leads.site_id = sites.site_id
GROUP BY clients.client_id, sites.domain_name
ORDER BY clients.client_id;

-- 9. Write a single query that retrieves total revenue collected from each client for each month of the year. Order it by client id.
SELECT CONCAT_WS(' ', clients.first_name,clients.last_name) as client_name
, sum(billing.amount) as total_revenue
, DATE_FORMAT(charged_datetime, '%M') as month_charge
, DATE_FORMAT(charged_datetime, '%Y') as year_charge
FROM billing
JOIN clients on billing.client_id = clients.client_id
GROUP BY month_charge, year_charge
ORDER BY billing.client_id, year_charge, month_charge;

-- 10. Write a single query that retrieves all the sites that each client owns. Group the results so that each row shows a new client. It will become clearer when you add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)
SELECT CONCAT_WS(' ', clients.first_name,clients.last_name) as client_name
, GROUP_CONCAT(sites.domain_name SEPARATOR ' / ')
FROM clients
JOIN sites on sites.client_id = clients.client_id
GROUP BY client_name
ORDER BY clients.client_id;