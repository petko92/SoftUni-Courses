# Read user input
number_of_pages = int(input())
pages_reads_in_one_hour = int(input())
days_needs_to_finish_book = int(input())

# Logic
total_reading_time = number_of_pages // pages_reads_in_one_hour
required_hours_per_day = total_reading_time // days_needs_to_finish_book

# Print result
print(required_hours_per_day)
