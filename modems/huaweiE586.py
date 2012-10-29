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
import urllib2
import sys
from modem import modemBase
import socket

class modem_huaweiE586(modemBase):
    """
    Driver class for the Huawei E586 wifi-3g modem.
    """

    NETWORK_TYPE_3G = 4
    NETWORK_TYPE_HDSP = 5
    NETWORK_TYPE_HDSP_PLUS = 9

    MACRO_BATTERY_STATUS_NORMAL = 0
    MACRO_BATTERY_STATUS_ELECT = 1
    MACRO_BATTERY_STATUS_CHARGING_INIT = -1

    MACRO_BATTERY_LEVEL_LOW = -1
    MACRO_BATTERY_LEVEL_ZERO = 0
    MACRO_BATTERY_LEVEL_ONE = 1
    MACRO_BATTERY_LEVEL_TWO = 2
    MACRO_BATTERY_LEVEL_THREE = 3
    MACRO_BATTERY_LEVEL_FOUR = 4

    def __init__(self):
        super(modem_huaweiE586, self).__init__()

    def update_status(self, debug):
        try:
            # Retrieve modem status. Would be nice to make this address configurable or
            # extract the IP address from the default gateway
            f = urllib2.urlopen("http://192.168.1.1/api/monitoring/status", timeout = 3)
            s = f.read()
            f.close()
        except urllib2.URLError:
            print "Unable to connect to device"
            self.wan_online = False
            self.signal_strength = 0
            return False
        except socket.timeout:
            print "Timeout attempting to communicate with device"
            self.wan_online = False
            self.signal_strength = 0
            return False
        except:
            print "Unexpected error:", sys.exc_info()[0]
            return False

        # Output debug info (ie the entire XML response) if requested
        if debug:
            print s

        element = ET.fromstring(s)

        # A service domain value of zero implies "no network" at which time,
        # the signal strength appears to be invalid.
        if int(element.findtext("CurrentServiceDomain")) == 0:
            self.wan_online = False
            return False

        # Signal strength is a percentage.
        self.signal_strength = int(element.findtext("SignalStrength"))

        # 2G's data rate is so slow, we may as well just declare if "offline".
        network_type = int(element.findtext("CurrentNetworkType"))
        self.wan_online = bool(network_type >= modem_huaweiE586.NETWORK_TYPE_3G)

        # Convert battery level to a percentage
        battery_level = int(element.findtext("BatteryLevel"))
        if battery_level == -1:
            self.battery_charge = 0
        else:
            self.battery_charge = battery_level * 25

        return True


