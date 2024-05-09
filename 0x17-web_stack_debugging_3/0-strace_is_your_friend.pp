# edits an incorrect file name

exec { 'rename_file':
  command => 'sed -i "s/.phpp/.php /var/www/html/wp-settings.php',
  onlyif  => 'test -e /var/www/html/wp-settings.php',
}
