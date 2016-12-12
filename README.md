#How to Remotely Monitor Your Pi Processes
---
_by Jamie Bailey, December 12, 2016_

![Process Dashboard Hero](https://github.com/InitialState/pi-process-dashboard/wiki/img/hero.jpg)

If you are using one or more Raspberry Pis to run a dedicated task (such as monitoring [who's at home](https://github.com/initialstate/pi-sensor-free-presence-detector/wiki) or [the weather](https://github.com/initialstate/wunderground-sensehat/wiki) or [your beer fridge](https://github.com/initialstate/beerfridge/wiki)), you need those processes to run uninterrupted. A task that exits unexpectedly may need your immediate attention to avoid lost data, project delays, or a system failure. It is impractical to manually babysit a bunch of Pis to make sure everything keeps running. A better way to ensure continuous operation is to be alerted when a process exits and be able to pull up a single dashboard at anytime to see the status of every important process running on every one of your deployed Pis.

In this tutorial, we will use a couple of simple scripts to:
- create a web-based dashboard that monitors the status of multiple processes
- configure our Pi to launch the dedicated process and its monitor on boot
- create an email/SMS notification when a process exits

[Read More ...](https://github.com/initialstate/pi-process-dashboard/wiki)
