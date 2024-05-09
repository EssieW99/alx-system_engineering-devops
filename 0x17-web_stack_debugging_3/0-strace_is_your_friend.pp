# edits an incorrect file name
file { '/var/www/html/wp-includes/class-wp-locale.phpp':
  ensure => absent,
}

file { '/var/www/html/wp-includes/class-wp-locale.php':
  ensure => present,
}

exec { 'rename_file':
  command => 'mv /var/www/html/wp-includes/class-wp-locale.phpp /var/www/html/wp-includes/class-wp-locale.php',
  unless  => 'test -f /var/www/html/wp-includes/class-wp-locale.php',
}