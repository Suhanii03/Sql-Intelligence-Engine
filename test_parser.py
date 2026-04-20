from nlp.parser import nl_to_sql

queries = [
    "top 5 customers by revenue",
    "total revenue",
    "revenue by city",
    "top 3 products in March",
    "customers in Hyderabad"
]

for q in queries:
    print("\nQuery:", q)
    print(nl_to_sql(q))