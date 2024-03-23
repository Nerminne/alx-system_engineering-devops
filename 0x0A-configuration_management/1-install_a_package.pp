# installing python
package { 'python3-pip':
  ensure => installed,
}

#installing flask
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
