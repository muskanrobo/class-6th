from collections import Counter

# List of scores
scores = [15, 18, 21, 15, 24, 18, 24, 30, 18, 24]

# 1. Mean
mean_score = sum(scores) / len(scores)
print("Mean (Average) Score:", mean_score)

# 2. Median
sorted_scores = sorted(scores)
middle_index = len(sorted_scores) // 2

# Check if the list has an odd or even length for median calculation
if len(sorted_scores) % 2 == 0:
    median_score = (sorted_scores[middle_index - 1] + sorted_scores[middle_index]) / 2
else:
    median_score = sorted_scores[middle_index]
print("Median Score:", median_score)

# 3. Mode
count = Counter(scores)
mode_score = max(count, key=count.get)
print("Mode Score:", mode_score)

# 4. Converting list to tuple and set
scores_tuple = tuple(scores)  # Tuple: Useful for fixed data that won't change
scores_set = set(scores)      # Set: Useful to remove duplicates and get unique scores

print("Scores as Tuple:", scores_tuple)
print("Scores as Set (Unique Scores):", scores_set)
