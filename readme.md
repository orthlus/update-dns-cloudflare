# info

python script for update dns record at cloudflare dns like [dynamic dns](https://en.wikipedia.org/wiki/Dynamic_DNS)

file `update-dns.py` can be installed in cron on local system, which need to be access from the internet
```bash
crontab -e
```
```bash
5 * * * * python3 update-dns.py
```

also enabled logging to [telegram bot](https://core.telegram.org/bots/api#authorizing-your-bot) 

## cloudflare info

endpoint to update dns record https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-update-dns-record

endpoint to get dns record id. there is bash file with curl for this
https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-list-dns-records

about api token https://developers.cloudflare.com/fundamentals/api/get-started/create-token/

zone id can watch at https://dash.cloudflare.com /account_id/zone_name in section API - Zone ID