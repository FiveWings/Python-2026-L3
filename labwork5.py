import pandas as po

# load students.csv
df = po.read_csv('students.csv')

# five rows
print(df.head())

# find num
print(df.shape)          # returns (30, 5) → 30 rows, 5 columns

# name and gpa
print(df[['name', 'GPA']])

# gpa better than 3.5
high_gpa = df[df['GPA'] >= 3.5]
print(high_gpa)

# sort by gpa
sorted_df = df.sort_values('GPA', ascending=False)
print(sorted_df)

# avg gpa
avg_gpa = df.groupby('major')['GPA'].mean()
print(avg_gpa)


# scores.csv also


# load
students = po.read_csv('students.csv')
scores = po.read_csv('scores.csv')

# check missing
print(students.isnull().sum())
print(scores.isnull().sum())


students['age'] = students['age'].fillna(students['age'].median())
students['GPA'] = students['GPA'].fillna(students['GPA'].mean())
scores['math'] = scores['math'].fillna(scores['math'].mean())
scores['database'] = scores['database'].fillna(scores['database'].mean())
merged = po.merge(students, scores, on='student_id')

merged['avg_score'] = merged[['python', 'math', 'database']].mean(axis=1)
print(merged[['name', 'avg_score']])

top5 = merged.sort_values('avg_score', ascending=False).head(5)
print(top5[['name', 'avg_score']])

avg_by_major = merged.groupby('major')['avg_score'].mean()
print(avg_by_major)