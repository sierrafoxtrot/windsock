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

class modemBase(object):
    "Generic base class for a modem."
    def __init__(self):
        # Signal Strength as a percentage
        self.signal_strength = 0

        # Is the connection to the internet "up"?
        self.wan_online = False

        # Battery Charge as a percetage
        self.battery_charge = 0

    # This is the guts of the modem "driver" class. It needs to update
    # the state variables (initialised above) and return a bool indicating
    # whether comms is working correctly.
    def update_status(self):
        raise NotImplementedError
