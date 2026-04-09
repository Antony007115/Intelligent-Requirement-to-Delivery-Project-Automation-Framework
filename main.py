from requirement_analysis import extract_features
from task_generation import generate_tasks
from timeline_estimation import estimate_time

requirement = input("Enter project requirement: ")

features = extract_features(requirement)

print("\nExtracted Features:")
print(features)

tasks = generate_tasks(features)

print("\nGenerated Tasks:")
for t in tasks:
    print(t)

time = estimate_time(tasks)

print("\nEstimated Project Duration:", time, "days")