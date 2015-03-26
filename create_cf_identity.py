#! /usr/bin/env python

# this script will create a CloudFront Origin Access Identity. More info on this topic can be found here:
# http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html
# Usage:
#   ./create_cf_identity.py "Description or comment " aws_profile

# the aws profile is the credentials profile that will be used to connect . This is optional

import boto
import sys

identity_comment = sys.argv[1]

try:
    aws_profile = sys.argv[2]
    conn = boto.connect_cloudfront(profile_name=aws_profile)
except IndexError:
    print "profile not specified using default connection"
    conn = boto.connect_cloudfront()

#this creates the identity
origin_identity = conn.create_origin_access_identity(comment=identity_comment )