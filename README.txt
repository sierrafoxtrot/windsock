What is Windsock?

Windsock is a program which reads status information from a 3G, 4G (or latest
buzzword compliant) portable wifi router and displays it in the system tray or
indicator area. It is also able to perform management operations such as
resetting the device.



What was the itch that Windsock originally scratched?

During my daily commute, I use a 3G to wifi router to stay connected. Coverage
along the train line is patch in some areas and out of habbit when the
connection is slow I look up to the signal strength meter for Network
Manager. Of course it shows 100% because the wifi router is about 1 meter away
from the laptop. Windsock adds a secondary signal strength meter for the wifi
router.



How does it work?

Most (all?) wifi routers have an internal web interface for configuration and
reporting status. Often this includes a signal strength meter in a bar at the
top of the page. Windsock reads data from this web interface and extracts the
necessary info updating the indicator/system-tray icon.



But it doesn't support my FOOBAR model XYZ router! Help!

Windsock currently supports only the devices that I can get my hands on. If you
have another device, get in touch. Alternatively, add support yourself and send
a patch/pull-request.


Supported Devices:
Huawei E586

Scott Finneran (SierraFoxtrot)
scottfinneran+githubATgmailDOTcom
