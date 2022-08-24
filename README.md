# wiki-search.com

This is a little flask app that searches wikipedia articles using the wikipedia API.

You'll need to set up DNS using dnsmasq as I did for easy use of all subdomains, or you can add
each desired search term to /etc/hosts like so:

```
## Local for Axuall Project - Start ##
127.0.0.1 wiki-search.com
::1 wiki-search.com
127.0.0.1 dogs.wiki-search.com
::1 dogs.wiki-search.com
127.0.0.1 dog.wiki-search.com
::1 dog.wiki-search.com
127.0.0.1 ordinary.wiki-search.com
::1 ordinary.wiki-search.com
127.0.0.1 uk.wiki-search.com
::1 uk.wiki-search.com
## Local for Axuall Project - End ##
```

dnsmasq:
https://firxworx.com/blog/it-devops/sysadmin/using-dnsmasq-on-macos-to-setup-a-local-domain-for-development/

Install python here: https://www.python.org/downloads/

Install dependencies with: `pip install -r requirements.txt`

Run the flask app with this command in the project folder:
`flask run`