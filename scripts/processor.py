def validate_record(record):
    required_fields = ['customerId', 'transactionId', 'transactionDate', 'sourceDate', 'currency']
    for field in required_fields:
        if field not in record:
            return False, f"Missing required field: {field}"

    if record['currency'] not in ['EUR', 'GBP', 'USD']:
        return False, f"Invalid currency: {record['currency']}"

    try:
        from datetime import datetime
        datetime.strptime(record['transactionDate'], '%Y-%m-%d')
    except (ValueError, TypeError):
        return False, f"Invalid transactionDate: {record['transactionDate']}"

    return True, None
