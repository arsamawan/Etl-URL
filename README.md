# ETL Pipeline: Extract, Transform, and Load to PostgreSQL

This repository contains an ETL (Extract, Transform, Load) pipeline that extracts data from a public API, transforms it, and loads the processed data into a PostgreSQL database.

## Features

- **Extract**: Fetch data from a specified public API.
- **Transform**: Clean and preprocess the data for further use.
- **Load**: Insert the transformed data into a PostgreSQL database.

## Requirements

- Python 3.8+
- PostgreSQL 13+
- Installed dependencies from `requirements.txt`

## Setup

1. **Clone the Repository**  
   git clone https://github.com/your-username/etl-pipeline.git

2. **Install Dependencies**  
   pip install -r requirements.txt

3. **Set Up PostgreSQL**  
   Create a database and note its credentials.

4. **Environment Variables**  
   Create a `.env` file with the following structure:  
   ```env
   API_URL=<public_api_endpoint>
   DB_HOST=<your_db_host>
   DB_PORT=<your_db_port>
   DB_NAME=<your_db_name>
   DB_USER=<your_db_user>
   DB_PASSWORD=<your_db_password>
   ```

## Usage

1. **Run the ETL Script**  
   Execute the ETL pipeline:  
   ```bash
   python etl.py
   ```

2. **Verify Data in PostgreSQL**  
   Use a PostgreSQL client to query the database and confirm the data has been loaded successfully.

## File Structure

```
etl-pipeline/
├── etl.py               # Main ETL script
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment variables file
├── README.md            # Project documentation
```

## Contributing

Contributions are welcome! Feel free to fork this repository and create a pull request with your enhancements or fixes.
