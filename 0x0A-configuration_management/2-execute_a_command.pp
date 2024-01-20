# Using Puppet, create a manifest that kills a process named killmenow.
exec { 'kill-killmenow':
  command  => 'pkll killmenow',
  path     => '/usr/bin',
}
