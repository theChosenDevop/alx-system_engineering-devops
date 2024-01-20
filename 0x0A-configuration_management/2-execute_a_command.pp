# Using Puppet, create a manifest that kills a process named killmenow.
exec { 'kill-killmenow':
  command  => 'pkill killmenow',
  path     => '/alx-system_engineering-devops/0x0A-configuration_management/',
}
