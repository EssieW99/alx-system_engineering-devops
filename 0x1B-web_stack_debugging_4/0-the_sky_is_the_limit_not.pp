# increase the limit of open files

exec { 'fix config':
  environment => ['DIR=/etc/default/nginx',
                  'OLD_VAL=ULIMIT="-n 15"',
                  'NEW_VAL=ULIMIT="-n 10000"'],
  command     => 'sudo sed -i "s/$OLD_VAL/$NEW_VAL/" $DIR; sudo service nginx restart',
  path        => ['/usr/bin', '/bin'],
  returns     => [0, 1]
}
