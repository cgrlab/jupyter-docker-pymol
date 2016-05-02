%pylab inline
from ipymol import viewer as v
import xmlrpc.client as xc
import time

v._thread.start();

time.sleep(0.5);

v._server = xc.ServerProxy( uri="http://localhost:9123/RPC2" );


v.do('fetch 3odu; as cartoon; bg white');
v.show();

img0 = v.to_png();

img0.save("testPng0.png", "PNG");
