# Updating the package list
exec { 'update_package_list':
  command => '/usr/bin/apt-get update',
}

# Installing Nginx
package { 'nginx':
  ensure => 'present',
} -> Service['nginx']

# Configure Nginx
file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
} -> Service['nginx']

# Restarting
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
