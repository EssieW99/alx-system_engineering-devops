# edits an incorrect file name

exec { 'rename_file':
  command => 'sed -i "s/.phpp/.php" /var/www/html/wp-settings.php',
  path    =>  '/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => 'test -e /var/www/html/wp-settings.php',
}
