from fastapi import FastAPI
import sqlite3
from nlp.parser import nl_to_sql
from optimizer.rules import optimize_query

app = FastAPI()

DB_PATH = "database/database.db"


@app.get("/")
def home():
    return {"message": "SQL Intelligence Engine is running 🚀"}


@app.get("/query")
def run_query(user_query: str):
    try:
        # 🔹 Step 1: Convert NL → SQL
        sql = nl_to_sql(user_query)

        # 🔹 Step 2: Get optimization suggestions
        suggestions = optimize_query(sql)

        # 🔹 Step 3: Connect to database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # 🔹 Step 4: Execute query
        cursor.execute(sql)
        rows = cursor.fetchall()

        # 🔹 Step 5: Extract column names
        columns = [desc[0] for desc in cursor.description]

        # 🔹 Step 6: Convert results to JSON
        data = [dict(zip(columns, row)) for row in rows]

        conn.close()

        # 🔥 Step 7: Generate insights
        insights = {}

        if data:
            insights["total_rows"] = len(data)

            if "total_revenue" in data[0]:
                total = sum(item.get("total_revenue", 0) for item in data)
                insights["total_revenue_sum"] = total

            # Top result
            insights["top_result"] = data[0]

        # 🔹 Step 8: Return response
        return {
            "generated_sql": sql,
            "row_count": len(data),
            "results": data,
            "insights": insights,
            "optimization_suggestions": suggestions
        }

    except Exception as e:
        return {"error": str(e)}