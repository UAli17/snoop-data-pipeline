import json

def log_error(conn, error_type, error_message, raw_data):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO error_log (error_type, error_message, raw_data)
            VALUES (%s, %s, %s::jsonb)
        """, (error_type, error_message, json.dumps(raw_data)))
    conn.commit()
