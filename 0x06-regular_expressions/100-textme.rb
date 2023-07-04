#!/usr/bin/env ruby

# Accept the log file path as the argument
log_data = ARGV[0]


# Define the regular expression pattern to extract the required information
pattern = /\[from:([\w+\s]+|\+\d+)\] \[to:([\w+\s]+|\+\d+)\] \[flags:(.*?)\]/

# Find all matches in the log data
matches = log_data.scan(pattern)

# Process the matches and output the required information
matches.each do |match|
  sender = match[0]
  receiver = match[1]
  flags = match[2]
  puts "#{sender},#{receiver},#{flags}"
end
