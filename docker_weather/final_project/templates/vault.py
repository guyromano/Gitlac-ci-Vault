import hvac
client = hvac.Client(
    url='http://54.152.205.100:8200',
    verify=False)
client.auth.approle.login(
    role_id="91410109-d361-420c-5de6-d4fc86998706",
    secret_id="f0c6a0b5-dabf-39e3-0ae2-59036a010dc2",)

read_response = client.secrets.kv.read_secret_version(mount_point="kv", path='weatherapp/text')

password = read_response['data']['data']['Assignment']
print(password)

