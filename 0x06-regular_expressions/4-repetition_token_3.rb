#!/usr/bin/env ruby

pattern = /h.t{0,}n/
string = ARGV[0]

matches = string.scan(pattern)

puts matches
