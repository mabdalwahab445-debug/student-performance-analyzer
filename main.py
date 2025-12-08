
import pandas as pd
import matplotlib.pyplot as plt

# Read data
df = pd.read_csv("data.csv")

# Calculations
average = df['Grade'].mean()
highest = df['Grade'].max()
lowest = df['Grade'].min()

# Save results
with open("result.txt", "w") as f:
    f.write(f"Average Grade: {average}\n")
    f.write(f"Highest Grade: {highest}\n")
    f.write(f"Lowest Grade: {lowest}\n")

# Plot
plt.figure()
plt.plot(df['Name'], df['Grade'], marker='o')
plt.title("Student Grades")
plt.xlabel("Student")
plt.ylabel("Grade")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grades_plot.png")

print("Analysis complete! Files generated: result.txt, grades_plot.png")
