#!/usr/bin/python
"""
Update a dynamic DNS entry from your external IP address.

Make an API_KEY in the Memset control panel.  This will need to have
these permissions at minimum.

  dns.zone_domain_list
  dns.zone_info
  dns.zone_record_update
  dns.reload
  job.status

Pass in API_KEY and HOSTNAME and this script will set the HOSTNAME to
have your current external IP address.
"""

uri = "https://%s:x@api.memset.com/v1/xmlrpc"

import os
import sys
from xmlrpclib import ServerProxy
from pprint import pformat
from urllib2 import urlopen
from time import sleep

def change_ip(s, hostname, new_ip):
    """
    Find the zone record for domain and adjust the A record for
    hostname to new_ip

    Returns a boolean if the record changed
    """
    # import ipdb; ipdb.set_trace()
    chunks = hostname.split(".")
    domain = ".".join(chunks[-2:])
    leafname = ".".join(chunks[:-2])
    # leafname, domain = hostname.split(".", 1)

    # Find the zone that the domain is in first
    zone_domains = s.dns.zone_domain_list()
    for zone_domain in zone_domains:
        if zone_domain['domain'] == domain:
            break
    else:
        raise ValueError("Couldn't find domain %r" % domain)
    zone_id = zone_domain['zone_id']
    print "Domain", pformat(domain)

    # List the zone to find the record to change
    zone = s.dns.zone_info(dict(id=zone_id))
    for record in zone['records']:
        if record['record'] == leafname and record['type'] == 'A':
            break
    else:
        raise ValueError("Couldn't find record for %r" % hostname)

    # Change the zone record
    print "Old Zone Record", pformat(record)
    new_record = s.dns.zone_record_update(dict(id=record['id'], address=new_ip))
    print "New Zone Record", pformat(new_record)
    return record != new_record

def reload_dns(s):
    """
    Reload the DNS servers
    """
    print "Reloading DNS",
    job = s.dns.reload()
    while not job['finished']:
        sys.stdout.flush()
        job = s.job.status(dict(id=job['id']))
        print ".",
        sleep(5)
    if not job['error']:
        print "OK"
    else:
        print "FAILED"

def main():
    """
    Find the external IP and update the zone with it
    """
    if len(sys.argv) != 4:
        print >>sys.stderr, "Syntax: %s <api_key> <hostname> <docker-machine>" % sys.argv[0]
        sys.exit(1)
    api_key, parent_hostname, docker_machine = sys.argv[1:]
    hostname = ".".join([docker_machine, parent_hostname])
    # external_ip = urlopen("http://api.externalip.net/ip/").read().strip()
    docker_ip = os.popen("docker-machine ip {}".format(docker_machine)).read().strip()
    print "Docker Machine IP is {}".format(docker_ip)
    s = ServerProxy(uri % api_key)
    if change_ip(s, hostname, docker_ip):
        reload_dns(s)
    else:
        print "Zone record unchanged, not reloading"

if __name__ == "__main__":
    main()
