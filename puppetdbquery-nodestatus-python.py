#!/usr/bin/env python
import argparse
import sys
from pypuppetdb import connect

# Options
parser = argparse.ArgumentParser("For querying puppetdb for nodes of a particular status")

parser.add_argument("status", metavar="status", choices=['changed', 'failed', 'unreported'], help="status of nodes")
parser.add_argument( "--host", metavar="hostname", default="localhost", help="puppet db host to query")

args = parser.parse_args()

# Establish Connection to PuppetDB
puppetdb = connect( host = args.host )

# Get Nodes with status
nodes = puppetdb.nodes(
        with_status=True)

# Get Status of Nodes
for node in nodes:
        if node.status == args.status:
                print (node)
