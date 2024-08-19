# volatility_database_practice

- Using PostgreSQL and Psycopg2, create a database housing VIX data.
    1) Download VIX data from CBOE
    2) Clean data to have correct date format
    3) Connect to PostgreSQL
    4) Create "volatility" database
    5) Connect to "volatility" database
    6) Create "vix" table
    7) Upload VIX data (housed in a dataframe) to "vix" table
    8) Query "vix" table to get average VIX close
- If you would like to learn about the VIX, please follow this [link](https://www.cboe.com/tradable_products/vix/)
- Learnings
    - Using Psycopg2 to:
        - Connect to PostgreSQL
        - Create a database
        - Create a table
        - Upload data using copy_from
        - Query table
    - Pandas to:
        - Download or read a CSV
        - Format date data
    - Convert Pandas DataFrame to a readable file in memory
    - Importing sensitive information through a .env file
- Potential Improvements
    - Create a python class for database connection through Psycopg2?
        - Seems unecessary with a small program
    - Readable code
    