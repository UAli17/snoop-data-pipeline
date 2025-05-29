DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS error_log;

-- Customers table with last_transaction_date
CREATE TABLE IF NOT EXISTS customers (
    customer_id UUID PRIMARY KEY,
    last_transaction_date DATE
);


-- Transactions table with composite primary key
CREATE TABLE IF NOT EXISTS transactions (
    customer_id UUID REFERENCES customers(customer_id),
    transaction_id UUID,
    transaction_date DATE,
    source_date TIMESTAMP,
    merchant_id INT,
    category_id INT,
    currency TEXT,
    amount NUMERIC,
    description TEXT,
    PRIMARY KEY (customer_id, transaction_id)
);

-- Error log table remains the same
CREATE TABLE IF NOT EXISTS error_log (
    id SERIAL PRIMARY KEY,
    error_type TEXT,
    error_message TEXT,
    raw_data JSONB,
    logged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
