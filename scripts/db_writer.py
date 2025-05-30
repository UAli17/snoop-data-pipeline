def upsert_customer(conn, customer_id, transaction_date):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO customers (customer_id, last_transaction_date)
            VALUES (%s, %s)
            ON CONFLICT (customer_id) DO UPDATE
            SET last_transaction_date = EXCLUDED.last_transaction_date
        """, (customer_id, transaction_date))


def upsert_transaction(conn, record):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO transactions (
                customer_id, transaction_id, transaction_date, source_date,
                merchant_id, category_id, currency, amount, description
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (customer_id, transaction_id) DO UPDATE SET
                merchant_id = EXCLUDED.merchant_id,
                category_id = EXCLUDED.category_id,
                currency = EXCLUDED.currency,
                amount = EXCLUDED.amount,
                description = EXCLUDED.description,
                source_date = EXCLUDED.source_date,
                transaction_date = EXCLUDED.transaction_date
        """, (
            record['customerId'],
            record['transactionId'],
            record['transactionDate'],
            record['sourceDate'],
            record.get('merchantId'),
            record.get('categoryId'),
            record.get('currency'),
            record.get('amount'),
            record.get('description')
        ))
    conn.commit()
