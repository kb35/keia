# Device Naming Convention

This document defines the hostname convention used in examples throughout the framework. When populating the framework with your own content, replace this with your team's actual naming convention.

## Hostname Format

```
{site}-{location}-{role}-{instance}
```

| Component | Description | Examples |
|-----------|------------|---------|
| `site` | Office or building identifier | `oak`, `elm`, `pine` |
| `location` | Floor, room name, or area | `f2`, `srv`, `maple`, `lobby` |
| `role` | Device role abbreviation (see table below) | `sw`, `vc`, `dp` |
| `instance` | Unit number | `01`, `02`, `03` |

## DNS Format

```
{hostname}.{site}.example.com
```

Example: `oak-maple-vc-01.oak.example.com`

## Device Role Abbreviations

### Network

| Role | Abbreviation | Example Hostname |
|------|-------------|-----------------|
| Network switch | `sw` | `oak-srv-sw-01` |
| Access point | `ap` | `elm-f4-ap-03` |
| Router | `rtr` | `oak-srv-rtr-01` |
| Firewall | `fw` | `oak-srv-fw-01` |

### Video Conferencing

| Role | Abbreviation | Example Hostname | Notes |
|------|-------------|-----------------|-------|
| Video codec | `vc` | `oak-maple-vc-01` | Codec with external camera |
| Video bar | `vb` | `oak-birch-vb-01` | All-in-one (camera + codec + speaker) |
| VC camera | `cam` | `oak-maple-cam-01` | Standalone camera (PTZ, ceiling) |
| Touch controller | `tc` | `oak-maple-tc-01` | Room control panel |
| Speakerphone | `spk` | `oak-maple-spk-01` | Table or ceiling microphone |

### Display and Signage

| Role | Abbreviation | Example Hostname |
|------|-------------|-----------------|
| Display | `dp` | `oak-maple-dp-01` |
| Signage player | `sgn` | `oak-lobby-sgn-01` |

### Room Infrastructure

| Role | Abbreviation | Example Hostname |
|------|-------------|-----------------|
| Scheduler panel | `sched` | `oak-maple-sched-01` |
| AV switcher | `avsw` | `oak-maple-avsw-01` |
| Audio DSP | `dsp` | `oak-hall-dsp-01` |

### Power

| Role | Abbreviation | Example Hostname |
|------|-------------|-----------------|
| PDU | `pdu` | `oak-srv-pdu-01` |
| UPS | `ups` | `oak-srv-ups-01` |

### Print

| Role | Abbreviation | Example Hostname |
|------|-------------|-----------------|
| Printer | `prn` | `oak-f2-prn-01` |

### Security

| Role | Abbreviation | Example Hostname |
|------|-------------|-----------------|
| Security camera | `sec` | `oak-lobby-sec-01` |
| Door controller | `door` | `oak-entry-door-01` |

## Example Sites

| Site Code | Description |
|-----------|------------|
| `oak` | Headquarters |
| `elm` | Regional office |
| `pine` | Data center |

## Example Rooms

| Room Name | Typical Use |
|-----------|------------|
| `maple` | Medium conference room |
| `cedar` | Small huddle room |
| `birch` | Large conference room |
| `srv` | Server room / MDF |
| `lobby` | Building entrance |
| `hall` | Town hall / all-hands space |
