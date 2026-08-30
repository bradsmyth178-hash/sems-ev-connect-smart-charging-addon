# SEMS EV CONNECT Smart Charging

Adds a guided Smart Charging controller to Home Assistant. The controller uses
the charger and home-energy entities that are already available in Home
Assistant, so normal setup is completed entirely through on-screen forms.

[![Add the Smart Charging repository to Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fbradsmyth178-hash%2Fsems-ev-connect-smart-charging-addon)

If the button does not open your Home Assistant, copy this address into
**Settings → Apps → App store → Repositories**:

`https://github.com/bradsmyth178-hash/sems-ev-connect-smart-charging-addon`

The installed app appears as **SEMS EV CONNECT Smart Charging**. Open it from
the Home Assistant sidebar and follow the setup assistant.

## Included releases

- SEMS EV CONNECT Smart Charging `0.1.0`
- EVCC `0.314.5`

The container is published for Home Assistant systems using `aarch64` or
`amd64`. Configuration and charging history are stored in Home Assistant's
persistent app data and are included in backups.

MIT licensed. This repository includes software based on EVCC.
