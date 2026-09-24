#!/bin/bash
# Create a new object profile.
# Usage: ./setup/create-profile.sh <object-name>
#
# Creates references/object-profiles/<object-name>-profile.yaml

set -e

OBJECT_NAME="$1"

if [ -z "$OBJECT_NAME" ]; then
    echo "Usage: ./setup/create-profile.sh <object-name>"
    echo "Example: ./setup/create-profile.sh network-switch"
    exit 1
fi

PROFILE_FILE="references/object-profiles/${OBJECT_NAME}-profile.yaml"

if [ -f "$PROFILE_FILE" ]; then
    echo "Error: Profile '${OBJECT_NAME}' already exists at ${PROFILE_FILE}"
    exit 1
fi

mkdir -p "$(dirname "$PROFILE_FILE")"
cat > "$PROFILE_FILE" << TEMPLATE
# Object Profile: ${OBJECT_NAME}
# What a healthy ${OBJECT_NAME} looks like across all platforms.

schema: object-profile

profile:
  name: "${OBJECT_NAME}"
  object_role: "{What this object does}"
  naming_prefixes: []
  version: "1.0"
  last_updated: "$(date +%Y-%m-%d)"
  owner: "{your name}"

sources:
  - file: "{path to relevant standard or reference}"
    provides: "{what this source contributes}"

platforms:
  # Add one section per platform this object should be tracked in.
  # Example:
  #
  # inventory:
  #   required_fields: [hostname, ip_address, serial, status]
  #   healthy_indicators:
  #     - status: active
  #     - all required fields populated
  #   naming_convention: "{pattern}"

  platform_1:
    required_fields: []
    healthy_indicators: []

consistency:
  # What should match across platforms.
  # Example:
  #
  # - check: "hostname match"
  #   compare: [inventory.hostname, dns.hostname]

  - check: "{what to compare}"
    compare: ["{platform1.field}", "{platform2.field}"]

discrimination:
  # Troubleshooting logic: symptom -> likely causes -> where to look first.
  # Example:
  #
  # device_unreachable:
  #   likely_causes: [power_failure, network_issue, hardware_failure]
  #   first_check: monitoring

  symptom_1:
    likely_causes: []
    first_check: "{platform}"

not_applicable:
  # Platforms that do NOT apply to this object type.
  # Example: [fleet_management, content_management]
  []
TEMPLATE

echo "Created: ${PROFILE_FILE}"
echo ""
echo "Next steps:"
echo "  1. Edit ${PROFILE_FILE} and fill in the platforms, consistency checks, and discrimination logic"
echo "  2. Link it from the relevant domain index and topic index"
