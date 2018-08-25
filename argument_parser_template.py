import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-z","--zabbix")
parser.add_argument("-v","--verbose",action="store_true")
parser.add_argument("-lb","--load-balancer",choices=[1,2,3,4], type=int,nargs='*',
                   help="1. BidSwitch-SSP-LB \n 2. Google-Bidder-US \n 3. smaato-LB \n 4. XML-LB")
args = parser.parse_args()
print args

if args.zabbix:
    print "Argument passed for zabbix.".format(args.zabbix)
if args.verbose:
    print "Argument passed {}".format(args.verbose)
if args.load_balancer:
    print "Argument passed {}".format(args.load_balancer)
