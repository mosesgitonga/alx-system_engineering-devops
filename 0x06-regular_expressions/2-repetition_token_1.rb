#!/usr/bin/env ruby

pattern = /h.t{0,1}n/
string = ARGV[0]

matches = string.scan(pattern)

puts matches.first(2)
