# Create custom HTTP header response

# Install Nginx
class { 'nginx': }

# Configure Nginx
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "add_header X-Served-By $hostname;\n",
  notify  => Service['nginx'],
}
