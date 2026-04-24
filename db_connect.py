# =============================================================================
# db_connect.py
# Handles MySQL database connection setup.
# Prompts the user for credentials and returns a connection object.
# =============================================================================

import mysql.connector
from mysql.connector import Error
from utils.formatter import print_separator, print_success, print_error, print_info


def setup_connection():
    """
    Prompts the user for MySQL credentials and establishes a connection.
    Returns the connection object on success, or None on failure.
    """
    print_separator("=")
    print_info("  MySQL Database Connection Setup  ")
    print_separator("=")

    host     = input("  Host     (default: localhost): ").strip() or "localhost"
    port     = input("  Port     (default: 3306)     : ").strip() or "3306"
    username = input("  Username                     : ").strip()
    password = input("  Password                     : ").strip()
    database = input("  Database Name                : ").strip()

    if not username or not database:
        print_error("Username and Database Name are required fields.")
        return None

    try:
        port = int(port)
    except ValueError:
        print_error("Port must be a valid number.")
        return None

    print_separator("-")
    print("  Connecting to MySQL...")

    try:
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=username,
            password=password,
            database=database,
            autocommit=False,          # We handle commits manually
            ssl_disabled=False,        # Aiven requires SSL
            ssl_verify_identity=False  # Bypass CA cert verify for simplicity if no cert is provided
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print_success(f"Connected to MySQL Server (version {db_info})")
            print_success(f"Database : '{database}'  |  Host : {host}")
            return connection

    except Error as e:
        print_error(f"Connection failed: {e}")
        return None