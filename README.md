# Test Database Schema
<img width="640" height="314" alt="image" src="https://github.com/user-attachments/assets/7abdce06-f3fb-4d5e-85ce-9c309ba3d05b" />

# PostgreSQL Learning Notes

## Key Concepts & Learnings

### Database Configuration
- Use `ConfigParser` to read database credentials from `.ini` files
- Store connection parameters (host, database, user, password) in `database.ini`
- Use `load_config()` function to parse configuration files

### Connection Management
- Use `psycopg2.connect(**config)` to establish connections
- Always use context managers (`with` statements) for automatic connection cleanup
- Context managers handle closing connections and rolling back on errors

### Table Creation
- Use `SERIAL PRIMARY KEY` for auto-incrementing IDs
- Define foreign key relationships with `REFERENCES` clause
- Use `ON UPDATE CASCADE ON DELETE CASCADE` for referential integrity
- Execute multiple DDL commands sequentially using cursor iteration

### Data Insertion
- Use parameterized queries with `%s` placeholders to prevent SQL injection
- For single inserts: `cur.execute(sql, (param,))`
- For multiple inserts: `cur.executemany(sql, data_list)`
- **Important**: Each element in data_list must be a tuple - use trailing comma for single-element tuples: `('value',)`

### Data Querying
- Use `cur.fetchall()` to get all results
- Use `cur.fetchone()` to get single result
- Use `cur.fetchmany(size)` for memory-efficient iteration over large datasets
- `cur.rowcount` returns number of affected rows

### Data Updates
- Use parameterized queries for UPDATE statements
- Return `cur.rowcount` to verify how many rows were affected during ana operation
- Always commit changes with `conn.commit()`

### Advanced Queries
- Use INNER JOIN to combine data from multiple tables
- Use ORDER BY for sorted results
- Iterator pattern with `fetchmany()` keeps memory usage low for large result sets

### Error Handling
- Wrap database operations in try-catch blocks
- Catch `psycopg2.DatabaseError` for database-specific errors
- Use context managers to ensure proper cleanup even on errors

### Python-PostgreSQL Data Types
- VARCHAR(n) for variable-length strings
- INTEGER for whole numbers
- SERIAL for auto-incrementing integers
- BYTEA for binary data

### Common Mistakes learnt
- **Tuple syntax**: `('value')` is a string, `('value',)` is a tuple
- **executemany parameters**: Pass the list directly, not wrapped in another tuple
- **Context managers**: Always use `with` statements for connections and cursors
