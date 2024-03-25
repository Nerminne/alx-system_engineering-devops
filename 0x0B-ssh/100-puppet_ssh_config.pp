# using puppet as in previous task

file { '/etc/ssh/ssh_config':
  ensure => 'present',
  content => "
    PasswordAuthentication no
    IdentityFile ~/.ssh/school
  ",
}
