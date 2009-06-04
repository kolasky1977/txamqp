#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

from time import time
#from txamqp.client import Closed
#from txamqp.queue import Empty
#from txamqp.content import Content
from txamqp.testlib import TestBase

#from twisted.internet.defer import, returnValue,
from twisted.internet.defer import Deferred, inlineCallbacks

class TxTests(TestBase):
    """
    Tests handling of heartbeat frames
    """

    
    @inlineCallbacks
    def setUp(self):
        """ Set up a heartbeat frame per second """
        self.client = yield self.connect(heartbeat=1)

        self.channel = yield self.client.channel(1)
        yield self.channel.channel_open()


    @inlineCallbacks
    def test_heartbeat(self):
        """
        Test that heartbeat frames are sent and received
        """
        d = Deferred()
        d.setTimeout(8)
        d.addBoth(lambda x:True)
        yield d
        t = time()
        self.assertTrue(self.client.lastSent > t - 3,
                        "A heartbeat frame was recently sent")
        self.assertTrue(self.client.lastReceived > t - 3,
                        "A heartbeat frame was recently received")
