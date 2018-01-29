"""Testing utilities for running test suites."""
from unittest import mock

from hermes.publisher import Publisher
from thoth.core.websocket import WebsocketConnector


def mocked_publisher():
    m = mock.Mock(spec=Publisher)
    m.publish.return_value = True
    return m


def mocked_wss():
    return mock.Mock(spec=WebsocketConnector)
