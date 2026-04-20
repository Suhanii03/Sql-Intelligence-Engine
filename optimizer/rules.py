def optimize_query(sql):
    suggestions = []

    sql_upper = sql.upper()

    # 🔹 Rule 1: Avoid SELECT *
    if "SELECT *" in sql_upper:
        suggestions.append("Avoid using SELECT *. Specify only required columns.")

    # 🔹 Rule 2: Missing WHERE clause
    if "WHERE" not in sql_upper:
        suggestions.append("Consider adding a WHERE clause to filter data and improve performance.")

    # 🔹 Rule 3: ORDER BY without LIMIT
    if "ORDER BY" in sql_upper and "LIMIT" not in sql_upper:
        suggestions.append("Use LIMIT with ORDER BY to reduce result size.")

    # 🔹 Rule 4: No aggregation optimization
    if "GROUP BY" in sql_upper and "ORDER BY" not in sql_upper:
        suggestions.append("Consider sorting aggregated results using ORDER BY.")

    # 🔹 Rule 5: Possible indexing suggestion
    if "WHERE" in sql_upper:
        suggestions.append("Ensure columns used in WHERE clause are indexed for faster queries.")

    # 🔹 Default message
    if not suggestions:
        suggestions.append("Query looks optimized!")

    return suggestions