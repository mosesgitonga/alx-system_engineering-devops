#!/usr/bin/env ruby

pattern = /h.?n/
string = ARGV[0]

matches = string.scan(pattern)

puts(matches)
