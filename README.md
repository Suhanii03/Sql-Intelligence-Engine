# 🚀 SQL Intelligence Engine

## 📌 Project Description

The SQL Intelligence Engine is a data interaction system designed to simplify database querying by enabling users to work with structured data in a more intuitive way. Instead of manually writing SQL queries, users can input requests in natural language through a simple interface.

The system processes these inputs and maps them to appropriate SQL operations, which are then executed on a connected database (SQLite). The results are retrieved and displayed in a structured format, making data analysis faster and more accessible, especially for beginners and non-technical users.

The project integrates a Streamlit-based frontend with a FastAPI backend to handle user requests efficiently. Data is initially sourced from a CSV file and converted into a structured database to support query execution.

The key objective of this system is to reduce the dependency on manual SQL writing, improve accessibility to data insights, and demonstrate practical integration of frontend, backend, and database technologies in a single workflow.
---

## 📌 Features

- 🧠 Natural Language → SQL conversion
- 📊 Query execution on SQLite database
- 📈 Automatic data insights generation
- ⚡ SQL optimization suggestions
- 📉 Basic data visualization
- 🖥️ Simple Streamlit-based UI

---

## 🏗️ Project Architecture
📂 Project Structure

```
SQL-INTELLIGENCE-ENGINE/
│── app.py / main.py        # Main application
│── model/                  # AI/logic components (if any)
│── database/               # SQL database files
│── utils/                  # Helper functions
│── requirements.txt        # Dependencies
│── README.md               # Project documentation
```
---

## ⚙️ Tech Stack

- Python 🐍
- FastAPI ⚡
- SQLite 🗄️
- Pandas 📊
- Streamlit 🎨
- NLP (rule-based parsing)

---

## 🧠 How It Works

1. User enters a natural language query  
2. NLP module converts it into SQL  
3. SQL is executed on SQLite database  
4. System returns:

   - Query results
   - Insights
   - Optimization suggestions

---

## 📊 Example Queries

- "top 5 customers by revenue"
- "revenue by city"
- "average revenue"
- "sales in March"

---

## 🔥 Output Includes

- Generated SQL query  
- Tabular results  
- Data insights (row count, totals)  
- Optimization suggestions for better SQL performance
