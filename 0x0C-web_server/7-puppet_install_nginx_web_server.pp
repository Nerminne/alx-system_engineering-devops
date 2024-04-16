#install Nginx web server
package { 'nginx':
  ensure => installed,
}

file_line { 'redirect':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'sever_name _;',
  line   => '\n\tlocation \/redirect_me {\n\t\treturn 301 https:\/\/www.youtube.com\/watch\?v=QH2-TGUlwu4;\n\t}',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  file_line['redirect'],
}
