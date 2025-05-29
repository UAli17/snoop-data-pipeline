import psycopg2
from data_loader import load_json_data
from processor import validate_record
from db_writer import upsert_customer, upsert_transaction
from error_logger import log_error

def main():
    conn = psycopg2.connect(
        dbname='snoop_data_pipeline',
        user='postgres',     
        password='MITTS',
        host='localhost',
        port='5432'
    )
    
    records = load_json_data('./data')

    for record in records:
        is_valid, error = validate_record(record)
        if not is_valid:
            log_error(conn, "ValidationError", error, record)
            continue

        upsert_customer(conn, record['customerId'], record['transactionDate'])
        upsert_transaction(conn, record)
    
    conn.close()

if __name__ == '__main__':
    main()
