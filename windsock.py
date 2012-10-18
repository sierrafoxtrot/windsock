# Windsock - wifi modem status and management
# Copyright (C) 2012 Scott Finneran
#
# Windsock is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Windsock is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Windsock.  If not, see <http://www.gnu.org/licenses/>.

import xml.etree.ElementTree as ET
import urllib
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--log",
                  action="store", type="string", dest="log_filename")

(options, args) = parser.parse_args()

# Retrieve modem status
f = urllib.urlopen("http://192.168.1.1/api/monitoring/status")
s = f.read()
f.close()

element = ET.fromstring(s)
signal_strength = element.findtext("SignalStrength")
print "SignalStrength = ", signal_strength

if options.log_filename != '':
    log = open(options.log_filename, 'w')
    log.write(s)
    log.close()

