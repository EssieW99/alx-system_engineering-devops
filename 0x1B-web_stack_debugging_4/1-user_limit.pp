# Change the OS configuration to login  holberton user and open a file

exec { 'add holberton user':
  environment => ['DIR=/etc/security/limits.conf',
                  'OLD_VAL=hard nofile 5',
                  'NEW_VAL=hard nofile 50000',
                  'OLD_VAL2=soft nofile 4',
                  'NEW_VAL2=soft nofile 40000'],
  command     => 'sudo sed -i "s/$OLD_VAL/$NEW_VAL/" $DIR; sudo sed -i "s/$OLD_VAL2/$NEW_VAL2/" $DIR',
  path        => ['/usr/bin', '/bin'],
  returns     => [0, 1]
}
