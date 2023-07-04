#!/usr/bin/env ruby

string = ARGV[0]

pattern = /School/

matches = string.scan(pattern)

joined_matches = matches.join

puts joined_matches
