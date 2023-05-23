#!/usr/bin/env ruby

import re

IP= input('Please insert your IP address here: ')

pattern = re.compile('re.compile("^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')

if re.search(pattern,IP):
    print('Your IP address of {} has been successfully found'.format(IP))
else:
    print('Invalid entry please try again')
