# edits an incorrect file name
file { '/var/www/html/wp-includes/class-wp-locale.phpp':
  ensure => absent,
}

file { '/var/www/html/wp-includes/class-wp-locale.php':
  ensure => present,
}