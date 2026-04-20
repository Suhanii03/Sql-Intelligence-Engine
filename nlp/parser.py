import re

def clean_query(query):
    query = query.lower()
    query = query.replace("?", "")
    query = query.strip()
    return query


def nl_to_sql(query):
    query = clean_query(query)

    base = "SELECT * FROM sales"
    where_clauses = []
    group_by = ""
    order_by = ""
    limit = ""

    # 🔹 TOP N (e.g., top 5 customers)
    top_match = re.search(r"top (\d+)", query)
    if top_match:
        limit = f"LIMIT {top_match.group(1)}"
        order_by = "ORDER BY total_revenue DESC"

    # 🔹 TOTAL revenue
    if "total revenue" in query:
        return "SELECT SUM(revenue) as total_revenue FROM sales;"

    # 🔹 AVERAGE revenue
    if "average revenue" in query:
        return "SELECT AVG(revenue) as avg_revenue FROM sales;"

    # 🔹 GROUP BY logic
    if "by city" in query:
        base = "SELECT city, SUM(revenue) as total_revenue FROM sales"
        group_by = "GROUP BY city"

    elif "by product" in query:
        base = "SELECT product, SUM(revenue) as total_revenue FROM sales"
        group_by = "GROUP BY product"

    elif "by customer" in query or "customers" in query:
        base = "SELECT customer_id, SUM(revenue) as total_revenue FROM sales"
        group_by = "GROUP BY customer_id"

    # 🔹 CITY filters
    cities = ["hyderabad", "bangalore", "chennai", "delhi", "mumbai", "pune"]
    for city in cities:
        if city in query:
            where_clauses.append(f"city = '{city.capitalize()}'")

    # 🔹 MONTH filters
    if "march" in query:
        where_clauses.append("date LIKE '2024-03%'")
    elif "february" in query:
        where_clauses.append("date LIKE '2024-02%'")
    elif "january" in query:
        where_clauses.append("date LIKE '2024-01%'")

    # 🔹 WHERE clause
    where_sql = ""
    if where_clauses:
        where_sql = "WHERE " + " AND ".join(where_clauses)

    # 🔹 Final SQL
    sql = f"""
    {base}
    {where_sql}
    {group_by}
    {order_by}
    {limit};
    """

    return sql