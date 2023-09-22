#killing a process called killmenow
exec {'kill a process':
    command => '/usr/bin/pkill -f killmenow',
    onlyif  => '/usr/bin/pgrep -f killmenow',
}