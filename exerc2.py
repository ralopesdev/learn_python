# Calculate a student’s GPA
 # Collect subject scores
print("Please, enter scores out of 100 for each subject: \n")
math_score = float(input("Math score: "))
english_score = float(input("English score: "))
science_score = float(input("Science score: "))
history_score = float(input("History score: "))
 # Display the entered scores
print("Scores entered:")
print(f"Math: {math_score}")
print(f"English: {english_score}")
print(f"Science: {science_score}")
print(f"history: {history_score}")

 # Calculate the total, average, and GPA
total = round(math_score + english_score + science_score + history_score, 2)
num_subjects = 4
average = total / num_subjects
gpa = round((average / 100) * 4.0, 2)

 # Display the results
print(f"\nTotal score: {total}")
print(f"Number of subjects: {num_subjects}")
print(f"Average score: {average}")
print(f"\nStudent GPA: {round(gpa, 2)} / 4.0")