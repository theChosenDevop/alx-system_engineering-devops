# fixes bad "phpp" extension to "php" in "wp-settings.php"

exec { 'fix-wordpress':
  command => '/bin/sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/usr/local/bin/', '/usr/bin/'],
}
