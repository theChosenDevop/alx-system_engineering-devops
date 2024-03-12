# wordpresss_setup.pp

# define file resource to manage wp-settings.php
file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => template('wordpress/wp-settings.erb'),
  require => Package['wordpress'], 
  notify  => Service['apache2'],
}
