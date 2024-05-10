# endpoint to update dns record
# https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-update-dns-record

# endpoint to get dns record id. there is bash file with curl for this
# https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-list-dns-records

# about api token https://developers.cloudflare.com/fundamentals/api/get-started/create-token/

# zone id can watch at https://dash.cloudflare.com /account_id/zone_name in section API - Zone ID

from pathlib import Path
import requests

home = '/root/'  # or /home/user_name/ (or maybe just ~, idk)
dir_ = home + 'ddns'
last = home + 'ddns/last-ip'

cloudflare_api = 'https://api.cloudflare.com/client/v4'
zone_id = ''
dns_record_id = ''
api_path = f'/zones/{zone_id}/dns_records/{dns_record_id}'
cloudflare_token = ''
domain = 'sub.example.com'

# https://core.telegram.org/bots/api#authorizing-your-bot
telegram_bot_token = ''
telegram_user_id = 0000000


def read():
    with open(last, encoding='utf-8') as file:
        return file.read()


def save(data):
    with open(last, 'w', encoding='utf-8') as file:
        return file.write(data)


def log(text):
    s = 'update-dns\n' + text
    print(s)
    if telegram_bot_token != '' and telegram_user_id != 0000000:
        param = {'chat_id': telegram_user_id, 'text': s}
        requests.get(f'https://api.telegram.org/bot{telegram_bot_token}/sendmessage', params=param)


def main():
    response = requests.get('https://ifconfig.me')
    curr_ip = response.text

    if curr_ip == read():
        exit(0)

    print('ip was changed, updating dns...')
    data = {
        'content': curr_ip,
        'name': domain,
        'type': 'A',
        'ttl': 300,
    }

    headers_ = {'authorization': 'Bearer ' + cloudflare_token, 'content-type': 'application/json'}
    put_r = requests.put(cloudflare_api + api_path, json=data, headers=headers_)
    if put_r.status_code == 200:
        save(curr_ip)
        log('ip changed to ' + curr_ip)
    else:
        log('error during update dns: ' + put_r.text)
        exit(1)


if __name__ == '__main__':
    Path(dir_).mkdir(exist_ok=True)
    Path(last).touch(exist_ok=True)

    main()
