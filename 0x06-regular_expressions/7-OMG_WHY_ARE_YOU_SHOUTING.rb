#!/usr/bin/env ruby

pattern = /[A-Z]/
string = ARGV[0]

matches = string.scan(pattern).join
puts matches
