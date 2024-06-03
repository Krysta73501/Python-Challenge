import csv

# Define the path to the CSV file
file_path = "C:\Classwork\Homework\python-challenge\PyPoll\Resources\election_data.csv"
output_path = 'C:/Classwork/Homework/python-challenge/PyPoll/election_results.txt'

# Initialize variables
total_votes = 0
candidates = {}
candidate_list = []

# Read the CSV file
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    
    for row in reader:
        total_votes += 1
        candidate = row[2]  # Candidate is in the third column (index 2)
        
        if candidate not in candidates:
            candidates[candidate] = 0
            candidate_list.append(candidate)
        
        candidates[candidate] += 1

# Calculate vote percentages and determine the winner
vote_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}
winner = max(candidates, key=candidates.get)

# Print the results
print(f"Total Votes Cast: {total_votes}")


# Creating a summary list to display
summary = []
for candidate in candidate_list:
    summary.append({
        'Candidate': candidate,
        'Total Votes': candidates[candidate],
        'Percentage of Votes': vote_percentages[candidate]
    })

# Print the summary
print("\nElection Results Summary:")
for item in summary:
    print(f"{item['Candidate']}: {item['Total Votes']} votes, {item['Percentage of Votes']:.2f}%")
  
with open(output_path, mode='w') as output_file:
    output_file.write(summary)