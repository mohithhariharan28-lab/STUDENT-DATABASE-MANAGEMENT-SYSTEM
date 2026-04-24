# STUDENT-DATABASE-MANAGEMENT-SYSTEM
I# MySQL CLI Application 🐬

A terminal-based Python application for interacting with a MySQL database. Supports all four SQL command categories — DDL, DML, DCL, and TCL — through an interactive menu, plus a free-form manual query mode.

---

## Features

- 🔌 **Secure connection setup** — prompts for host, username, password, and database at startup
- 📋 **Structured menus** — hierarchical navigation per command category
- 📊 **Auto-formatted SELECT results** — aligned table output with column headers
- 💾 **Auto-commit** — DML changes are committed automatically; DDL/DCL commit implicitly
- ↩️ **Transaction control** — manual COMMIT, ROLLBACK, SAVEPOINT support
- ✍️ **Manual query mode** — type any SQL with multi-line input support
- ⚠️ **Error handling** — descriptive error messages and automatic rollback on failure
- 🎨 **Coloured output** — ANSI colours for success, error, warning, and info messages

---

## Project Structure

```
dbms/
├── main.py              # Entry point — menus & command dispatcher
├── db_connect.py        # MySQL connection setup
├── requirements.txt     # Python dependencies
├── utils/
│   ├── __init__.py
│   └── formatter.py     # Coloured terminal output helpers
└── commands/
    ├── __init__.py
    ├── ddl.py           # CREATE, ALTER, DROP, TRUNCATE, RENAME
    ├── dml.py           # SELECT, INSERT, UPDATE, DELETE
    ├── dcl.py           # GRANT, REVOKE
    ├── tcl.py           # COMMIT, ROLLBACK, SAVEPOINT
    └── query.py         # Free-form / manual SQL query handler
```

---

## Requirements

- Python 3.7+
- MySQL Server (running locally or remotely)
- `mysql-connector-python` library

---

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/dbms.git
   cd dbms
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

---

## Usage

When the app starts, it will prompt you for your MySQL credentials:

```
═══════════════════════════════════════════════════════
  MySQL Database Connection Setup
═══════════════════════════════════════════════════════
  Host     (default: localhost): 
  Username                     : root
  Password                     : 
  Database Name                : mydb
```

You are then taken to the main menu where you can choose a command category:

```
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
```

Each category has its own sub-menu with prompts and examples for every supported statement.

---

## Supported Commands

| Category | Commands |
|----------|----------|
| **DDL** | `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `RENAME` |
| **DML** | `SELECT`, `INSERT`, `UPDATE`, `DELETE` |
| **DCL** | `GRANT`, `REVOKE` |
| **TCL** | `COMMIT`, `ROLLBACK`, `SAVEPOINT`, `RELEASE SAVEPOINT`, `ROLLBACK TO SAVEPOINT` |
| **Manual** | Any valid SQL statement |

---

## License

This project is open-source and available under the [MIT License](LICENSE).
