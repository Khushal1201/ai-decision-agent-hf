def build_order_context(row):
    return f"""
OrderID: {row['OrderID']}
OrderValueUSD: {row['OrderValueUSD']}
Country: {row['Country']}
City: {row['City']}
ProductCode: {row['ProductCode']}
CustomerNotes: {row['CustomerNotes']}
DeliveryContext: {row['DeliveryContext']}
CustomerType: {row['CustomerType']}
"""
