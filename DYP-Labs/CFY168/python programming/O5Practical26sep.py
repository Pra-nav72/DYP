#Q2
arr = []
total_run =0
for i in range(20):
    runs_per_over = int(input(f"enter runs of over {i+1}: "))
    total_run += runs_per_over
    arr.append(runs_per_over)

run_rate = total_run/20

print(f"total score: {total_run}")
print(f"highest run in an over: {max(arr)}")
print(f"lowest run in an over: {min(arr)}")
print(f"RunRate: {run_rate:.2f}")
for run in arr:
    if run>=run_rate:
        print(run, end=" ")
