import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('scores.csv')

if 'database' in df.columns and 'db' not in df.columns:
    df['db'] = df['database']

plt.figure(figsize=(12, 6))
plt.scatter(df['student_id'], df['math'], color='#1f77b4', label='Math', s=60, alpha=0.8, edgecolors='black', linewidth=0.5)
plt.scatter(df['student_id'], df['python'], color='#2ca02c', label='Python', s=60, alpha=0.8, edgecolors='black', linewidth=0.5)
plt.scatter(df['student_id'], df['db'], color='#ff7f0e', label='DB (Database)', s=60, alpha=0.8, edgecolors='black', linewidth=0.5)

plt.title('Student Scores in Math, Python, and DB', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Student ID', fontsize=12)
plt.ylabel('Score', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=9)
plt.yticks(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title='Courses', fontsize=11, title_fontsize=11)
plt.tight_layout()
plt.savefig('scattered.png', dpi=300)
plt.close()
print("Saved scattered.png")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

courses = [
    ('math', 'Math', '#1f77b4'),
    ('python', 'Python', '#2ca02c'),
    ('db', 'DB (Database)', '#ff7f0e')
]

for ax, (col, title, color) in zip(axes, courses):
    ax.hist(df[col].dropna(), bins=8, color=color, edgecolor='black', alpha=0.7)
    ax.set_title(f'{title} Mark Distribution', fontsize=12, fontweight='bold')
    ax.set_xlabel('Marks', fontsize=10)
    ax.set_ylabel('Number of Students', fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.6)

fig.suptitle("Histogram of Courses' Marks", fontsize=15, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('histo.png', dpi=300)
plt.close()
print("Saved histo.png")

plt.figure(figsize=(8, 6))

data_to_plot = [
    df['math'].dropna(),
    df['python'].dropna(),
    df['db'].dropna()
]
labels = ['Math', 'Python', 'DB']

bp = plt.boxplot(
    data_to_plot,
    tick_labels=labels,
    patch_artist=True,
    medianprops=dict(color='black', linewidth=2),
    flierprops=dict(marker='o', markersize=6, markerfacecolor='red', alpha=0.7)
)

colors = ['#1f77b4', '#2ca02c', '#ff7f0e']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)

plt.title('Box Plot of Course Scores (Math, Python, DB)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Course', fontsize=12)
plt.ylabel('Score', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6, axis='y')
plt.tight_layout()
plt.savefig('box.png', dpi=300)
plt.close()
print("Saved box.png")
