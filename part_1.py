# The storage bay 
sample_bay = ["Basalt", "Silica", "Iron", "Dust"]
print(sample_bay[0])
print(sample_bay[-1])
print(len(sample_bay))


#Analysing Samples (Iteration)
for sample in sample_bay:
    print(f"Transmitting data for: {sample}")


new_findings = []
for _ in range(3):
    rock_type = input("Enter a new rock type: ")
    new_findings.append(rock_type)
    print(new_findings)

if "Dust" in sample_bay:
    sample_bay.remove("Dust")
    print(sample_bay)


