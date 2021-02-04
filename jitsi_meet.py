import requests
import collectd


class JitsiMeetService:

    def __init__(self):
        self.endpoint = None

    def dispatch(self, name, value, data_type="count"):
        cld_dispatch = collectd.Values(
            plugin='jitsi_meet',
            type=data_type,
            type_instance=name
        )
        cld_dispatch.dispatch(values=[value])

    def config(self, config):
        endpoint_set = False

        for node in config.children:
            key = node.key.lower()
            val = node.values[0]

            if key == 'url':
                self.endpoint = val
                endpoint_set = True
            else:
                collectd.debug('jitsi_meet: Unknown config key "%s"' % key)

        if not endpoint_set:
            collectd.error('jitsi_meet: URL not set. Exiting')
            raise ValueError

        collectd.debug("jitsi_meet: Plugin Configured")

    def read(self):

        collectd.debug('jitsi_meet: Getting data from API')

        response = requests.get(self.endpoint)

        # Get JSON Object from request
        r = response.json()

        # Dispatch Conference Stats
        self.dispatch(name='conferences', value=r['conferences'])
        self.dispatch(name='participants', value=r['participants'])
        self.dispatch(name='largest_conference', value=r['largest_conference'])
        self.dispatch(name='total_conference_seconds', value=r['total_conference_seconds'])
        self.dispatch(name='total_conferences_completed', value=r['total_conferences_completed'])

        # Dispatch Network Stats
        self.dispatch(name='total_packets_sent', value=r['total_packets_sent'])
        self.dispatch(name='total_packets_received', value=r['total_packets_received'])
        self.dispatch(name='total_bytes_sent', value=r['total_bytes_sent'], data_type='bytes')
        self.dispatch(name='total_bytes_received', value=r['total_bytes_received'], data_type='bytes')


jms = JitsiMeetService()

collectd.register_config(jms.config)
collectd.register_read(jms.read)
