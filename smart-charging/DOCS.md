# SEMS EV CONNECT Smart Charging

This app coordinates your EV charging with the information already available
in Home Assistant. It uses the SEMS EV CONNECT charger entities for control and
the GoodWe inverter entities for grid, solar and battery readings.

## Before you start

Confirm these four Home Assistant automations are disabled before activating
Smart Charging:

- Solar Saver
- Solar + Battery
- Cheap Overnight
- Boost Now

This prevents two controllers from trying to change the charger at the same
time. You can re-enable those automations later only after Smart Charging has
been turned off.

## Setup

1. In HACS, update **SEMS EV CONNECT** to version `1.2.0` or later and restart
   Home Assistant.
2. Open this app, turn on **Start on boot** and **Watchdog**, then press
   **Start**.
3. Press **Open Web UI**. Home Assistant authorisation is supplied securely by
   the app, so there is no access token to copy or paste.
4. In the setup assistant, add a charger and choose **SEMS EV CONNECT Smart
   Charging**. Select the suggested status, charging switch, current limit,
   power, current and voltage entities.
5. Add the home-energy devices with **SEMS GoodWe Home Energy System**. Create
   a grid meter and solar meter, then add the battery meter and its state of
   charge. Select the matching GoodWe entities suggested by Home Assistant.
6. Create the charging point, select the charger, and keep its initial charging
   mode set to **Off**.
7. Review the live grid, solar, battery and charger readings. When all four
   readings are current, select the charging mode you want to use.

Normal setup is completed in the Web UI. You do not need to edit YAML or create
a Home Assistant long-lived access token.

## Charging modes

- **Off** leaves charging control stopped.
- **Solar** uses available solar generation and respects the configured battery
  reserve.
- **Minimum + solar** maintains the minimum charging current and adds available
  solar.
- **Fast** charges at the configured current limit.

The charger accepts current limits from 6 A up to its rated ceiling. Rapid
changes are coalesced, spaced and verified by the SEMS EV CONNECT integration.
If the charger state is stale or unavailable, new control commands are blocked.

## Test drive

Use the `1602` journey on the SEMS EV CONNECT setup site before enabling this
app. Its Test Drive uses simulated readings and never sends a command to your
equipment. It is designed to familiarise you with each status and control.

## Backups and updates

Home Assistant stores the app database at `/data/evcc.db`. The database holds
the setup, preferences and charging history and is included in Home Assistant
backups. The app uses a cold backup so the database is closed cleanly while the
backup is made.

Before updating, create a Home Assistant backup. After updating, open the app
and confirm the versions shown are:

- SEMS EV CONNECT Smart Charging `0.1.0`
- EVCC `0.314.5`

## Diagnostics

If a reading shows unavailable:

1. Check **Settings → Devices & services → SEMS EV CONNECT** and confirm the
   charger entities are available.
2. Check **Settings → Devices & services → GoodWe Inverter** and confirm the
   grid, solar, battery power and battery state-of-charge entities are updating.
3. Open this app's **Log** tab and copy the entries around the most recent
   connection or command attempt. Passwords and Home Assistant tokens should
   never be included in a support message.
4. Keep the charging mode set to **Off** until every required reading is
   available again.
