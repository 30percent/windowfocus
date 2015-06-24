windowfocus
===========

WindowFocus extends [OpenGazer](http://www.inference.phy.cam.ac.uk/opengazer/), an open source gaze tracking software that uses any standard webcam, to change window focus based on where the user is looking.

### Description

Using Python's socket library to capture the results from a running [OpenGazer](http://www.inference.phy.cam.ac.uk/opengazer/) process, the software in real time changes between windows based on where the user is looking. To do this, a couple of addition libraries are needed:

* wnck
* Qt through PySide

OpenGazer's use of a standard webcam and local sockets allows anyone with a UNIX operating system to write programs that are linked directly to a user's gaze.
