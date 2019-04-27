# This file handles


# importing libraries
import rcpy
import sys
import gpiod
import config
import io
import threading
import time
import os
import select


class InputEvent(threading.Thread):

    LOW = 1
    HIGH = 2

    class InputEventInterrupt(Exception):
        pass

    def __init__(self, input, event, debounce=0, timeout=None,
                 target=None, vargs=(), kwargs={}):

        super().__init__()

        self.input = input
        self.event = event
        self.target = target
        self.vargs = vargs
        self.kwargs = kwargs
        self.timeout = timeout
        self.debounce = 0
        self.pipe = rcpy.create_pipe()

    def action(self, event):
        if self.target:
            # call target
            self.target(self.input, event, *self.vargs, **self.kwargs)
        else:
            # just check for valid event
            if event != InputEvent.HIGH and event != InputEvent.LOW:
                raise Exception('Unkown InputEvent {}'.format(event))

    def run(self):
        self.run = True
        while rcpy.get_state() != rcpy.EXITING and self.run:

            try:
                evnt = self.input.high_or_low(self.debounce,
                                              self.timeout,
                                              self.pipe)
                if evnt is not None:
                    evnt = 1 << evnt
                    if evnt & self.event:
                        # fire callback
                        self.action(evnt)

            except InputTimeout:
                self.run = False

    def stop(self):
        self.run = False
        # write to pipe to abort
        os.write(self.pipe[1], bytes(str(rcpy.EXITING), 'UTF-8'))
        # sleep and destroy pipe
        time.sleep(1)
        rcpy.destroy_pipe(self.pipe)
        self.pipe = None
