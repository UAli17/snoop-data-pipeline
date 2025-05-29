from datetime import datetime

def validate_record(record):
    required_fields = ['customerId', 'customerName', 'transactionId', 'transactionDate', 'sourceDate', 'amount']
    missing_fields = [field for field in required_fields if not record.get(field)]
    
    if missing_fields:
        return False, f"Missing fields: {missing_fields}"
    
    try:
        datetime.strptime(record['transactionDate'], '%Y-%m-%d')
        datetime.strptime(record['sourceDate'], '%Y-%m-%dT%H:%M:%S')
        float(record['amount'])
    except Exception as e:
        return False, f"Invalid format: {e}"
    
    return True, None
