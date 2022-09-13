# Election Analysis

## Overview

We've been tasked with auditing the tabulated results of a U.S. congressional precinct in Colorado. Using the CSV file provided, we will parse the dataset to determine its contents, tally results, and output a report based on our findings. We'll be using Python for this task because it's much more responsive than Excel when dealing with large datasets.

## Results

* By importing our CSV file, then initializing a `total_votes` integer variable, we are able to iterate through every row in the dataset (except for the header) in order to count all of the rows.

        file_to_load = os.path.join("Resources", "election_results.csv")
        with open(file_to_load) as election_data:
            reader = csv.reader(election_data)
            header = next(reader)
            for row in reader:
                total_votes = total_votes + 1
        print(total_votes)

* We can determine how many votes occurred in each county, but first we need to establish how many counties participated in the election. We do this by declaring an empty list variable called `county names`, then iterating through the datasat and adding county names to our list on the condition that the county has not been added yet. When a new county is found, we'll also start compiling any votes that correspond with that county. We'll store vote counts per county in `votes_per_county` dictionary.

		county_names = []
		votes_per_county = {}
		for row in reader:
		    if county_name not in county_names:
		        county_names.append(county_name)
		        votes_per_county[county_name] = 0
            votes_per_county[county_name] += 1

    We'll need to print the output of this tally and their percentages too. 

        county_votes = votes_per_county[county]
		for county in county_names:
	        county_votes = votes_per_county[county]
    	    county_percentage = '{:.1%}'.format(county_votes / total_votes)
	        print(f"{county}: {county_percentage} ({county_votes:,})")

		>>> Jefferson: 10.5% (38,855)
		>>> Denver: 82.8% (306,055)
		>>> Arapahoe: 6.7% (24,801)

    Our output shows that 38,855 (10.5%) votes were cast in Jefferson County, 306,055 (82.8%) votes were cast in Denver County, and 24,801 (6.7%) votes were cast in Arapahoe.

* We'll use a conditional statement to isolate which county had the most votes cast.

        if (county_votes > winning_county_count):
            winning_county = county
        print(f"Largest County Turnout: {winning_county}")


		>>> Largest County Turnout: Denver

* Identical to establishing the number of votes per county, we also want to establish the number of votes per candidate. We'll use the same loop to establish the winner as well.

	    candidate_results = (
	            f"\nVotes Per Candidate:\n"
	            f"-------------------------\n")
	    for candidate_name in candidate_votes:
	        votes = candidate_votes.get(candidate_name)
	        vote_percentage = float(votes) / float(total_votes) * 100
	        candidate_results += (
	            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
	        if (votes > winning_count) and (vote_percentage > winning_percentage):
	            winning_count = votes
	            winning_candidate = candidate_name
	            winning_percentage = vote_percentage
	    print(candidate_results)

		>>> Votes Per Candidate:
		>>> -------------------------
		>>> Charles Casper Stockham: 23.0% (85,213)
		>>> Diana DeGette: 73.8% (272,892)
		>>> Raymon Anthony Doane: 3.1% (11,606)

* We can see the results are very decisive, with Degette receiving 272,892 votes for a total of 73.8%, Stockham receiving 85,213 votes for a total of 23.0%, and Doane receiving a paltry 111,606 votes for a total of 3.1%. We'll summarize the winning candidate's victory here.

	    winning_candidate_summary = (
	        f"\nWinning Candidate Summary\n"
	        f"-------------------------\n"
	        f"Winner: {winning_candidate}\n"
	        f"Winning Vote Count: {winning_count:,}\n"
	        f"Winning Percentage: {winning_percentage:.1f}%\n"
	        f"-------------------------\n")
    	print(winning_candidate_summary)


		>>> Winning Candidate Summary
		>>> -------------------------
		>>> Winner: Diana DeGette
		>>> Winning Vote Count: 272,892
		>>> Winning Percentage: 73.8%

## Summary

This script doesn't need any modification to operate with other election data with different precincts, candidates, etcetera. However, there are two points to consider if you wish to utilize this script using different datasets.

1. If the dataset provided has a different column order, then the script would need to be adapted to match. Our two most important columns are defined with `county_name = row[1]` and `candidate_name = row[2]`.

2. Keep in mind that this script automatically skips over the first row because we assume that our dataset's top row is used to define column names. If the new dataset does not include a header row, then we should remove the `header = next(reader)` line to ensure that we aren't skipping it.