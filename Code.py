import csv

# Open the CSV file
with open('data1.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    # Read the values from each column
    data = list(zip(*reader))

# Extract the values from each column
SNP = list(map(int, data[0]))
Start = list(map(int, data[1]))
End = list(map(int, data[2]))
QTL = data[3]  # Assuming the QTL column is the fourth column

# Check if each value in List SNP falls between values in List Start and End
results = []
for value in SNP:
    for i in range(len(Start)):
        if Start[i] <= value <= End[i]:
            results.append([value, Start[i], End[i], QTL[i]])

# Export the results as a CSV file with headers
with open('results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['SNP', 'Start', 'End', 'QTL'])  # Write the headers
    writer.writerows(results)

#All the columns must have the same row numbers. Fill the empty cells with 0 
