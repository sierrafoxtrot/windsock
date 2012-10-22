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
from modem import modemBase

class modem_huaweiE586(modemBase):
    """
    Driver class for the Huawei E586 wifi-3g modem.
    """

    NETWORK_TYPE_3G = 4
    NETWORK_TYPE_HDSP = 5
    NETWORK_TYPE_HDSP_PLUS = 9

    def __init__(self):
        super(modem_huaweiE586, self).__init__()

    def update_status(self):
        # Retrieve modem status
        f = urllib.urlopen("http://192.168.1.1/api/monitoring/status")
        s = f.read()
        f.close()

        element = ET.fromstring(s)
        self.signal_strength = int(element.findtext("SignalStrength"))

        # 2G's data rate is so slow, we may as well just declare if "offline".
        networkType = int(element.findtext("CurrentNetworkType"))
        self.wan_online = bool(networkType >= modem_huaweiE586.NETWORK_TYPE_3G)

        return True


