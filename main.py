# -*- coding: utf-8 -*-
# =============================================================================
# main.py
# Entry point for the MySQL CLI application.
# Manages the main menu loop and dispatches commands to the correct handlers.
# =============================================================================

import sys
from db_connect import setup_connection
from utils.formatter import (
    print_separator, print_success, print_error,
    print_info, print_warning
)

# DDL
from commands.ddl import (
    handle_create, handle_alter,
    handle_drop, handle_truncate, handle_rename
)

# DML
from commands.dml import (
    handle_select, handle_insert,
    handle_update, handle_delete
)

# DCL
from commands.dcl import handle_grant, handle_revoke

# TCL
from commands.tcl import (
    handle_commit, handle_rollback,
    handle_savepoint, handle_release_savepoint, handle_rollback_to
)

# Manual query
from commands.query import handle_manual_query


# =============================================================================
# Menu definitions
# =============================================================================

MAIN_MENU = """
  ┌─────────────────────────────────────────────────┐
  │           MySQL CLI Application                 │
  ├─────────────────────────────────────────────────┤
  │  1. DDL Commands  (CREATE / ALTER / DROP …)     │
  │  2. DML Commands  (SELECT / INSERT / UPDATE …)  │
  │  3. DCL Commands  (GRANT / REVOKE)              │
  │  4. TCL Commands  (COMMIT / ROLLBACK / …)       │
  │  5. Manual Query  (Free-form SQL)               │
  │  0. Exit                                        │
  └─────────────────────────────────────────────────┘
"""

DDL_MENU = """
  -- DDL Sub-menu --
  1. CREATE
  2. ALTER
  3. DROP
  4. TRUNCATE
  5. RENAME
  0. Back
"""

DML_MENU = """
  -- DML Sub-menu --
  1. SELECT
  2. INSERT
  3. UPDATE
  4. DELETE
  0. Back
"""

DCL_MENU = """
  -- DCL Sub-menu --
  1. GRANT
  2. REVOKE
  0. Back
"""

TCL_MENU = """
  -- TCL Sub-menu --
  1. COMMIT
  2. ROLLBACK
  3. SAVEPOINT
  4. RELEASE SAVEPOINT
  5. ROLLBACK TO SAVEPOINT
  0. Back
"""


# =============================================================================
# Sub-menu loops
# =============================================================================

def ddl_loop(cursor, connection):
    """Loop for DDL sub-menu."""
    while True:
        print(DDL_MENU)
        choice = input("  DDL> ").strip()
        if   choice == "1": handle_create(cursor, connection)
        elif choice == "2": handle_alter(cursor, connection)
        elif choice == "3": handle_drop(cursor, connection)
        elif choice == "4": handle_truncate(cursor, connection)
        elif choice == "5": handle_rename(cursor, connection)
        elif choice == "0": break
        else:               print_warning("Invalid choice. Please try again.")


def dml_loop(cursor, connection):
    """Loop for DML sub-menu."""
    while True:
        print(DML_MENU)
        choice = input("  DML> ").strip()
        if   choice == "1": handle_select(cursor, connection)
        elif choice == "2": handle_insert(cursor, connection)
        elif choice == "3": handle_update(cursor, connection)
        elif choice == "4": handle_delete(cursor, connection)
        elif choice == "0": break
        else:               print_warning("Invalid choice. Please try again.")


def dcl_loop(cursor, connection):
    """Loop for DCL sub-menu."""
    while True:
        print(DCL_MENU)
        choice = input("  DCL> ").strip()
        if   choice == "1": handle_grant(cursor, connection)
        elif choice == "2": handle_revoke(cursor, connection)
        elif choice == "0": break
        else:               print_warning("Invalid choice. Please try again.")


def tcl_loop(cursor, connection):
    """Loop for TCL sub-menu."""
    while True:
        print(TCL_MENU)
        choice = input("  TCL> ").strip()
        if   choice == "1": handle_commit(cursor, connection)
        elif choice == "2": handle_rollback(cursor, connection)
        elif choice == "3": handle_savepoint(cursor, connection)
        elif choice == "4": handle_release_savepoint(cursor, connection)
        elif choice == "5": handle_rollback_to(cursor, connection)
        elif choice == "0": break
        else:               print_warning("Invalid choice. Please try again.")


# =============================================================================
# Main application loop
# =============================================================================

def main():
    """Main entry point: connect to DB then run the command loop."""

    # ── Connection setup ─────────────────────────────────────────────────────
    connection = None
    while connection is None:
        connection = setup_connection()
        if connection is None:
            retry = input("\n  Connection failed. Retry? (yes/no): ").strip().lower()
            if retry != "yes":
                print_info("Goodbye!")
                sys.exit(0)

    # Create a reusable cursor (buffered to avoid unread-result errors)
    cursor = connection.cursor(buffered=True)

    # ── Main menu loop ────────────────────────────────────────────────────────
    try:
        while True:
            print(MAIN_MENU)
            choice = input("  Enter choice: ").strip()

            if   choice == "1": ddl_loop(cursor, connection)
            elif choice == "2": dml_loop(cursor, connection)
            elif choice == "3": dcl_loop(cursor, connection)
            elif choice == "4": tcl_loop(cursor, connection)
            elif choice == "5": handle_manual_query(cursor, connection)
            elif choice == "0":
                print_info("Exiting application...")
                break
            else:
                print_warning("Invalid choice. Please enter a number from the menu.")

    except KeyboardInterrupt:
        print_warning("\nInterrupted by user (Ctrl+C).")

    finally:
        # ── Resource cleanup ──────────────────────────────────────────────────
        print_separator("-")
        print_info("Closing database resources...")
        try:
            if cursor:
                cursor.close()
                print_success("Cursor closed.")
        except Exception as e:
            print_error(f"Error closing cursor: {e}")
        try:
            if connection and connection.is_connected():
                connection.close()
                print_success("Database connection closed.")
        except Exception as e:
            print_error(f"Error closing connection: {e}")
        print_info("Goodbye!")


# =============================================================================
# Entry guard
# =============================================================================

if __name__ == "__main__":
    main()
