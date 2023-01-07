import random
from prettytable import PrettyTable
table = PrettyTable()

ran = lambda: round(random.random(), 4)
table.field_names = ["Month","Earning"]
table.add_rows(
    [        
        ["JAN.", ran()],
        ["FEB.", ran()],
        ["MAR.", ran()],
        ["APR.", ran()],
    ]
)
print(table) 
"""
+-------+---------+
| Month | Earning |
+-------+---------+
|  JAN. |  0.8967 |
|  FEB. |  0.176  |
|  MAR. |  0.2654 |
|  APR. |  0.9531 |
+-------+---------+
"""