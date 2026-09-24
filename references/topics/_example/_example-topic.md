# Infrastructure Topic: Network Devices

## Scope

Network switches, access points, routers, and out-of-band management devices. Covers provisioning, troubleshooting, and lifecycle management.

## Relevant Objects

- device (with class: network_switch, access_point, router, oob_device)

## Evidence Surfaces

- `references/object-profiles/_example-profile.yaml`
- `registry/sources/_example-source.yaml`
- Inventory system (device record, interfaces, connections)
- DNS system (host records, DHCP reservations)
- Monitoring system (health, alerts, metrics)
- Port management (VLAN assignments, PoE status)

## Comparison Questions

- Does the device identity match across inventory and DNS?
- Is the monitoring profile correct for this device type?
- Are all ports configured as expected?
- Is firmware at the expected version?
- Are connected devices healthy?

## Expansion Triggers

- Identity mismatch -> expand into Asset Management
- Connected device failures -> expand into AV or Print (depending on device type)
- Power issue suspected -> expand into Infrastructure / Power Distribution
- Multiple site-wide failures -> likely ISP circuit or core switch, expand scope to site
