#!/usr/bin/env ruby

pattern = /^h.n$/
string = ARGV[0]

matches = string.scan(pattern)
if matches.empty?
  puts ""
else
  puts matches
end
