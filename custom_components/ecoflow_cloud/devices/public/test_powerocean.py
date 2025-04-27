import pytest
from custom_components.ecoflow_cloud.devices.public.powerocean import PowerOcean
from custom_components.ecoflow_cloud import EcoflowApiClient

class DummyClient(EcoflowApiClient):
    pass

def test_powerocean_sensors():
    device = PowerOcean({"sn": "testsn", "device_type": "PowerOcean"})
    client = DummyClient()
    sensors = device.sensors(client)
    assert any(s.name == "mpptPwr" for s in sensors)
    assert any(s.name == "bpSoc" for s in sensors)
    assert any(s.name == "pcsAPhase.vol" for s in sensors)
    assert any(s.name == "Status" or hasattr(s, "is_status") for s in sensors)

def test_powerocean_numbers_switches_selects():
    device = PowerOcean({"sn": "testsn", "device_type": "PowerOcean"})
    client = DummyClient()
    assert device.numbers(client) == []
    assert device.switches(client) == []
    assert device.selects(client) == []
