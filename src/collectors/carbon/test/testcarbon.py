from test import CollectorTestCase
from test import get_collector_config
from mock import patch, MagicMock, Mock
from diamond.collector import Collector
from carbon import CarbonCollector

NOW = \
{
    "info": {
        "now": "1438153899528851"
    },
    "module": {
        "NSMTPHandler": {
            "command": {
                "auth": {
                    "elapsed": "0",
                    "exec": "0"
                },
                "connect": {
                    "elapsed": "43875",
                    "exec": "24"
                },
                "data": {
                    "elapsed": "1947",
                    "exec": "22"
                },
                "ehlo": {
                    "elapsed": "1550",
                    "exec": "7"
                },
                "eof": {
                    "elapsed": "9",
                    "exec": "22"
                },
                "etc": {
                    "elapsed": "2840",
                    "exec": "19"
                },
                "mail": {
                    "elapsed": "35266",
                    "exec": "23"
                },
                "quit": {
                    "elapsed": "1738",
                    "exec": "20"
                },
                "rcpt": {
                    "elapsed": "124508",
                    "exec": "23"
                },
                "rset": {
                    "elapsed": "1941",
                    "exec": "18"
                },
                "starttls": {
                    "elapsed": "1396042",
                    "exec": "2"
                },
                "tmperr": "1"
            },
            "interop": {
                "arc": {
                    "elapsed": "135040",
                    "exec": "151"
                },
                "deque": {
                    "elapsed": "87207921",
                    "exec": "7734616"
                },
                "memberbo": {
                    "elapsed": "64422",
                    "exec": "23"
                },
                "mimefilter": {
                    "elapsed": "21699",
                    "exec": "22"
                },
                "mimeparse": {
                    "elapsed": "121098",
                    "exec": "22"
                },
                "smtpclient": {
                    "elapsed": "688838",
                    "eoftimeout": "0",
                    "exec": "22"
                },
                "virus": {
                    "elapsed": "829",
                    "exec": "22"
                }
            },
            "queue": {
                "dequed": "0",
                "pool": {
                    "busycount": "0",
                    "taskscount": "0",
                    "threadcount": "10"
                },
                "queued": "0"
            },
            "result": {
                "enque": "0",
                "error": "0",
                "reject": "0",
                "reque": "0",
                "return": "0",
                "success": "22"
            }
        },
        "ScribedLogModule": {
            "1": {
                "errorCount": "0",
                "size": "0"
            },
            "FileLoggingThread": {
                "errorCount": "0",
                "size": "0"
            },
            "Total": {
                "errorCount": "0",
                "size": "0"
            }
        },
        "_monitor": {
            "sampling": {
                "history": "3600",
                "period": "1000000"
            }
        },
        "_server0": {
            "config": {
                "net": {
                    "addr": "\"0.0.0.0\"",
                    "backlog": "1000",
                    "port": "25",
                    "secured": "\"false\""
                },
                "pool": {
                    "idleWait": "100",
                    "max": "100",
                    "min": "100",
                    "queue": "100"
                },
                "service": {
                    "handler": "\"smtp\""
                },
                "timeout": {
                    "idle": "10000",
                    "read": "10000",
                    "write": "10000"
                }
            },
            "statistics": {
                "accept": "24",
                "busy": "0",
                "pool": {
                    "busycount": "0",
                    "taskscount": "0",
                    "threadcount": "100"
                }
            }
        },
        "_server1": {
            "config": {
                "net": {
                    "addr": "\"0.0.0.0\"",
                    "backlog": "1000",
                    "port": "8888",
                    "secured": "\"false\""
                },
                "pool": {
                    "idleWait": "100",
                    "max": "5",
                    "min": "5",
                    "queue": "100"
                },
                "service": {
                    "handler": "\"http\""
                },
                "timeout": {
                    "idle": "-1",
                    "read": "10000",
                    "write": "10000"
                }
            },
            "statistics": {
                "accept": "43",
                "busy": "0",
                "pool": {
                    "busycount": "0",
                    "taskscount": "0",
                    "threadcount": "5"
                }
            }
        },
        "http": {
            "config": {
                "logic": {
                    "ref": "\"NSMTPHandler\""
                },
                "static": {
                    "baseurl": "\"\/doc\/\""
                }
            },
            "statistics": {
                "active": "0",
                "elapsed": "83901398",
                "exec": "43"
            }
        },
        "smtp": {
            "config": {
                "logic": {
                    "ref": "\"NSMTPHandler\""
                }
            },
            "statistics": {
                "active": "0",
                "elapsed": "34055144",
                "exec": "24"
            }
        }
    }
}

PRE = \
{
    "info": {
        "now": "1438150370190832"
    },
    "module": {
        "NSMTPHandler": {
            "command": {
                "auth": {
                    "elapsed": "0",
                    "exec": "0"
                },
                "connect": {
                    "elapsed": "40575",
                    "exec": "22"
                },
                "data": {
                    "elapsed": "1762",
                    "exec": "20"
                },
                "ehlo": {
                    "elapsed": "1550",
                    "exec": "7"
                },
                "eof": {
                    "elapsed": "9",
                    "exec": "20"
                },
                "etc": {
                    "elapsed": "2561",
                    "exec": "17"
                },
                "mail": {
                    "elapsed": "33157",
                    "exec": "21"
                },
                "quit": {
                    "elapsed": "1558",
                    "exec": "18"
                },
                "rcpt": {
                    "elapsed": "112469",
                    "exec": "21"
                },
                "rset": {
                    "elapsed": "1707",
                    "exec": "16"
                },
                "starttls": {
                    "elapsed": "1396042",
                    "exec": "2"
                },
                "tmperr": "1"
            },
            "interop": {
                "arc": {
                    "elapsed": "121609",
                    "exec": "137"
                },
                "deque": {
                    "elapsed": "83300404",
                    "exec": "7383897"
                },
                "memberbo": {
                    "elapsed": "58129",
                    "exec": "21"
                },
                "mimefilter": {
                    "elapsed": "19886",
                    "exec": "20"
                },
                "mimeparse": {
                    "elapsed": "116713",
                    "exec": "20"
                },
                "smtpclient": {
                    "elapsed": "654909",
                    "eoftimeout": "0",
                    "exec": "20"
                },
                "virus": {
                    "elapsed": "755",
                    "exec": "20"
                }
            },
            "queue": {
                "dequed": "0",
                "pool": {
                    "busycount": "0",
                    "taskscount": "0",
                    "threadcount": "10"
                },
                "queued": "0"
            },
            "result": {
                "enque": "0",
                "error": "0",
                "reject": "0",
                "reque": "0",
                "return": "0",
                "success": "20"
            }
        },
        "ScribedLogModule": {
            "1": {
                "errorCount": "0",
                "size": "0"
            },
            "FileLoggingThread": {
                "errorCount": "0",
                "size": "0"
            },
            "Total": {
                "errorCount": "0",
                "size": "0"
            }
        },
        "_monitor": {
            "sampling": {
                "history": "3600",
                "period": "1000000"
            }
        },
        "_server0": {
            "config": {
                "net": {
                    "addr": "\"0.0.0.0\"",
                    "backlog": "1000",
                    "port": "25",
                    "secured": "\"false\""
                },
                "pool": {
                    "idleWait": "100",
                    "max": "100",
                    "min": "100",
                    "queue": "100"
                },
                "service": {
                    "handler": "\"smtp\""
                },
                "timeout": {
                    "idle": "10000",
                    "read": "10000",
                    "write": "10000"
                }
            },
            "statistics": {
                "accept": "22",
                "busy": "0",
                "pool": {
                    "busycount": "0",
                    "taskscount": "0",
                    "threadcount": "100"
                }
            }
        },
        "_server1": {
            "config": {
                "net": {
                    "addr": "\"0.0.0.0\"",
                    "backlog": "1000",
                    "port": "8888",
                    "secured": "\"false\""
                },
                "pool": {
                    "idleWait": "100",
                    "max": "5",
                    "min": "5",
                    "queue": "100"
                },
                "service": {
                    "handler": "\"http\""
                },
                "timeout": {
                    "idle": "-1",
                    "read": "10000",
                    "write": "10000"
                }
            },
            "statistics": {
                "accept": "1",
                "busy": "0",
                "pool": {
                    "busycount": "0",
                    "taskscount": "0",
                    "threadcount": "5"
                }
            }
        },
        "http": {
            "config": {
                "logic": {
                    "ref": "\"NSMTPHandler\""
                },
                "static": {
                    "baseurl": "\"\/doc\/\""
                }
            },
            "statistics": {
                "active": "0",
                "elapsed": "13284",
                "exec": "42"
            }
        },
        "smtp": {
            "config": {
                "logic": {
                    "ref": "\"NSMTPHandler\""
                }
            },
            "statistics": {
                "active": "0",
                "elapsed": "32825638",
                "exec": "22"
            }
        }
    }
}

class TestCarbonCollector(CollectorTestCase):
    def setUp(self):
        config = get_collector_config('CarbonCollector', {
            'exclude' : ['config'],
            'gauge' : ['statistics.pool', 'statistics.active'],
        })
        self.collector = CarbonCollector(config, None)

    def test_import(self):
        self.assertTrue(CarbonCollector)

    @patch.object(Collector, 'publish')
    def test_should_work_with_example(self, publish):
        global PRE, NOW
        mock = Mock(self.collector.entries)
        self.collector.entries = mock
        mock.return_value = NOW
        self.collector._predata = PRE
        self.collector.collect()
        assert len(publish.call_args_list)

    @patch.object(Collector, 'publish')
    def test_reset_monitoring_data(self, publish):
        pre = {
            "module": {
                "NSMTPHandler": {
                    "command": {
                        "elapsed": "2000",
                        "exec": "1000"
                    }}}
        }
        now = {
            "module": {
                "NSMTPHandler": {
                    "command": {
                        "elapsed": "0",
                        "exec": "0"
            }}}
        }
        mock = Mock(self.collector.entries)
        self.collector.entries = mock
        mock.return_value = now
        self.collector._predata = pre
        self.collector.collect()
        assert not publish.called
