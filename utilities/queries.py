QUERIES = {
    'insert_to_crypto':"""
        INSERT INTO {schema_name}.{table_name} 
        (price, timestamp)
        VALUES
        (%s,%s)
"""
}
