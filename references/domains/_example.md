# Example Domain: Infrastructure

> **Owner:** {your infrastructure lead}

## Scope

Network devices, power distribution, structured cabling, server rooms, and circuit management. Everything that keeps the physical and network infrastructure running.

## Topics

### Network Devices

Switches, access points, routers, out-of-band management.

- **Topic index:** `references/topics/_example/_example-topic.md`
- **Object profile:** `references/object-profiles/_example-profile.yaml`
- **Reference data:** `references/_example-platform-reference.yaml`
- **Tools:** inventory_read, dns_read, monitoring_read, port_management
- **Source Registry:** `registry/sources/_example-source.yaml` -> Network device config guides

**Why this matters:** Network devices are the foundation everything else depends on. A switch outage affects every device connected to it. Always check network path before concluding a device issue is isolated.

### Power Distribution

PDUs, UPS units, power panels.

- **Topic index:** (create when needed)
- **Object profile:** (create when needed)
- **Tools:** pdu_management, inventory_read, monitoring_read

## Cross-Domain Connections

- When a device troubleshoot reveals a network path issue -> check Infrastructure
- When a new installation is planned -> check Infrastructure for port availability
- When monitoring shows power alerts -> check Infrastructure for UPS/PDU status
- When multiple devices at one site fail simultaneously -> likely Infrastructure root cause

## Knowledge Layer Checklist

- [ ] Network device configuration guides (Source Registry)
- [ ] Naming conventions (platform reference)
- [ ] VLAN assignments per site
- [ ] Port allocation standards
- [ ] Power redundancy requirements
