# installing flask

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => package['Werkzeug'],

package { 'Werkzeug':
  ensure => 2.1.1,
}
