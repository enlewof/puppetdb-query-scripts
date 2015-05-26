#!/usr/bin/env python
import argparse
import sys
from pypuppetdb import connect

# Options
parser = argparse.ArgumentParser("For querying puppetdb for a report on a particular node")

parser.add_argument("node", help="report for a particular node")
parser.add_argument( "--host", metavar="hostname", default="localhost", help="puppet db host to query")

args = parser.parse_args()

# Establish Connection to PuppetDB
puppetdb = connect( host = args.host )

# Get Report for Node
events = puppetdb.events('["and", ["=", "certname", "{0}" ], ["=", "status", "failure"], ["=", "latest-report?", "true"]]'.format(args.node))

for event in events:
        print '{0}[{1}]: {2}'.format(event.item["type"], event.item["title"], event.item["message"])
