cat  << EOF
authentication:
  client_key: $TUGBOAT_CLIENT_KEY
  api_key: $TUGBOAT_API_KEY
ssh:
  ssh_user: root
  ssh_key_path: "~/.ssh/id_rsa"
  ssh_port: '22'
defaults:
  region: '8'
  image: '9801950'
  size: '66'
  ssh_key: ''
  private_networking: 'false'
  backups_enabled: 'false'
EOF