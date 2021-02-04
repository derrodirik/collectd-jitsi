# collectd-jitsi-meet

collectd-jitsi-meet is a CollectD Python plugin to get Jitsi Meet Statistics from the Colibri API

## Dependencies

Python Module: Requests [https://pypi.org/project/requests/](https://pypi.org/project/requests/)

## Configuration

1. Activate "Colibri" on your Jitsi Server [https://github.com/jitsi/jitsi-videobridge/blob/master/doc/rest.md](https://github.com/jitsi/jitsi-videobridge/blob/master/doc/rest.md#configuration)
2. Configure the Plugin
  ```
  LoadPlugin python
  <Plugin python>
    ModulePath "<Path to Folder>"
    Import "jitsi_meet"
    <Module jitsi_meet>
        url "<https://meet.your-server.de:8000/colibri/stats>"
    </Module>
  </Plugin>
  ```
3. Done
