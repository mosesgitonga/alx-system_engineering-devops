#!/usr/bin/env ruby

pattern = /hbt{1,}n/
string = ARGV[0]

matches = string.scan(pattern)
puts matches
