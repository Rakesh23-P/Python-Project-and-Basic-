import numpy as np
import pandas as pd
marks = np.array(
    [
        [100, 99, 46],
        [25, 98, 56],
        [90, 99, 78]
    ]
)

subject = ["java", "python", 'sql']
total = np.sum(marks, axis=0)
print(total)
average = np.mean(marks[1:, ])
print(average)

sql_marks = np.max(marks[2:, ])
print(sql_marks)

df = pd.DataFrame(marks, subject)
print(df)
