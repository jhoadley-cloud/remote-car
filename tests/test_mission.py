import json
import pytest
from remote_car.mission import load_mission, MissionError


def test_valid_mission(tmp_path):
    path = tmp_path / "mission.json"
    path.write_text(json.dumps([{"lat": 37.0, "lon": -122.0, "alt": 0}]))
    mission = load_mission(path)
    assert len(mission) == 1


def test_invalid_latitude(tmp_path):
    path = tmp_path / "mission.json"
    path.write_text(json.dumps([{"lat": 137.0, "lon": -122.0}]))
    with pytest.raises(MissionError):
        load_mission(path)


def test_missing_lon(tmp_path):
    path = tmp_path / "mission.json"
    path.write_text(json.dumps([{"lat": 37.0}]))
    with pytest.raises(MissionError):
        load_mission(path)
