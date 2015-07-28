from test import CollectorTestCase
from test import get_collector_config
from mock import patch
from diamond.collector import Collector
from shell import ShellCollector

class TestShellCollector(CollectorTestCase):
    def setUp(self):
        config = get_collector_config('ShellCollector', {
            'scripts': {'processes':'ps -ef | wc -l'}
        })
        self.collector = ShellCollector(config, None)

    def test_import(self):
        self.assertTrue(ShellCollector)

    @patch.object(Collector, 'publish')
    def test_should_work_with_example(self, publish_mock):
        self.collector.collect()
        assert len(publish_mock.call_args_list)
        assert publish_mock.call_args_list[0][0][0] == 'processes'
        assert publish_mock.call_args_list[0][0][1] > 0
