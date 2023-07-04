#!/usr/bin/env ruby

pattern = /^\d{10}/

string = ARGV[0]

if matches = string.scan(pattern)
  puts matches[0]
else
  puts "$"
end
