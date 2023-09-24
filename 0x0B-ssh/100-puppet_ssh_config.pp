#puppet client configuration

exec { 'configure_ssh':
  command => '/bin/sh -c \'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config\'',
  path    => '/bin/',
  unless  => 'grep -E "^(PasswordAuthentication no|IdentityFile ~/.ssh/school)" /etc/ssh/ssh_config',
}




