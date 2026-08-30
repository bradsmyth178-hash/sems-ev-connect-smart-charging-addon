from __future__ import annotations

import pathlib
import re

import yaml


ROOT = pathlib.Path(__file__).resolve().parents[1]
ADDON = ROOT / "smart-charging"


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    print(f"PASS {message}")


repository = yaml.safe_load((ROOT / "repository.yaml").read_text(encoding="utf-8"))
config = yaml.safe_load((ADDON / "config.yaml").read_text(encoding="utf-8"))

check(repository["name"] == "SEMS EV CONNECT Smart Charging", "repository metadata")
check(config["version"] == "0.1.0", "app release is 0.1.0")
check(config["image"] == "ghcr.io/bradsmyth178-hash/sems-ev-connect-evcc", "release image contract")
check(config["arch"] == ["aarch64", "amd64"], "aarch64 and amd64 are supported")
check(config["homeassistant_api"] is True, "Home Assistant API permission is enabled")
check(config["ingress"] is True and config["ingress_port"] == 7070, "ingress opens the Web UI")
check(config["boot"] == "auto" and config["backup"] == "cold", "automatic boot and safe backup")
check(config["options"]["sqlite_file"] == "/data/evcc.db", "persistent database path")

docs = "\n".join(
    path.read_text(encoding="utf-8")
    for path in [ROOT / "README.md", ADDON / "README.md", ADDON / "DOCS.md"]
)
for required in [
    "Solar Saver",
    "Solar + Battery",
    "Cheap Overnight",
    "Boost Now",
    "SEMS EV CONNECT Smart Charging",
    "EVCC `0.314.5`",
    "simulated readings",
]:
    check(required in docs, f"customer guidance includes {required}")

for forbidden in [r"\bRon\b", r"\bHCA\b", r"\bGen(?:eration)?\s*[12]\b", r"sponsorToken", r"long-lived access token to copy"]:
    check(re.search(forbidden, docs, re.IGNORECASE) is None, f"customer guidance excludes {forbidden}")

secrets = re.compile(r"(?i)(password|token|secret)\s*[:=]\s*['\"]?[A-Za-z0-9_-]{8,}")
for path in ROOT.rglob("*"):
    if path.is_file() and ".git" not in path.parts:
        check(secrets.search(path.read_text(encoding="utf-8", errors="ignore")) is None, f"no embedded secret in {path.relative_to(ROOT)}")
