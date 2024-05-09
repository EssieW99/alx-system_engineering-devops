# edits an incorrect file name

exec { 'rename_file':
  command => 'mv /var/www/html/wp-includes/class-wp-locale.phpp /var/www/html/wp-includes/class-wp-locale.php',
  onlyif  => 'test -e /var/www/html/wp-includes/class-wp-locale.phpp',
}
