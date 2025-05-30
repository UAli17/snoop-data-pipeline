-- Total transaction volume by customer
SELECT customer_id, SUM(amount) AS total_spent
FROM transactions
GROUP BY customer_id
ORDER BY total_spent DESC;

-- Daily Transaction volume
SELECT transaction_date, SUM(amount) AS daily_total
FROM transactions
GROUP BY transaction_date
ORDER BY transaction_date;

-- Currency Breakdown
SELECT currency, SUM(amount) AS total_amount, COUNT(*) AS num_transactions
FROM transactions
GROUP BY currency
ORDER BY total_amount DESC;

-- Running total of transactions per customer
SELECT
  customer_id,
  transaction_date,
  amount,
  SUM(amount) OVER (
    PARTITION BY customer_id
    ORDER BY transaction_date
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS running_total
FROM transactions
ORDER BY customer_id, transaction_date;

-- Rank customers by total spending
WITH customer_totals AS (
  SELECT
    customer_id,
    SUM(amount) AS total_spent
  FROM transactions
  GROUP BY customer_id
)
SELECT
  customer_id,
  total_spent,
  RANK() OVER (ORDER BY total_spent DESC) AS spend_rank
FROM customer_totals;

-- Rolling 7-day average of daily transaction volume
WITH daily_totals AS (
  SELECT
    transaction_date,
    SUM(amount) AS daily_total
  FROM transactions
  GROUP BY transaction_date
)
SELECT
  transaction_date,
  daily_total,
  ROUND(AVG(daily_total) OVER (
    ORDER BY transaction_date
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ), 2) AS rolling_7day_avg
FROM daily_totals
ORDER BY transaction_date;