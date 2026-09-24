#!/bin/bash
# Create a new domain with all required files.
# Usage: ./setup/create-domain.sh <domain-name>
#
# Creates:
#   references/domains/<domain-name>.md       (from schema template)
#   references/topics/<domain-name>/           (empty directory)
#   One starter topic index and object profile (optional, prompted)

set -e

DOMAIN_NAME="$1"

if [ -z "$DOMAIN_NAME" ]; then
    echo "Usage: ./setup/create-domain.sh <domain-name>"
    echo "Example: ./setup/create-domain.sh infrastructure"
    exit 1
fi

DOMAIN_FILE="references/domains/${DOMAIN_NAME}.md"
TOPIC_DIR="references/topics/${DOMAIN_NAME}"

if [ -f "$DOMAIN_FILE" ]; then
    echo "Error: Domain '${DOMAIN_NAME}' already exists at ${DOMAIN_FILE}"
    exit 1
fi

# Create domain index from template
mkdir -p "$(dirname "$DOMAIN_FILE")"
cat > "$DOMAIN_FILE" << 'TEMPLATE'
# DOMAIN_PLACEHOLDER

> **Owner:** {owner name}

## Scope

{What falls in this domain and what doesn't. One paragraph.}

## Topics

### {Topic 1 Name}

{Brief description of what this topic covers.}

- **Topic index:** `references/topics/DOMAIN_PLACEHOLDER/{topic-1}.md`
- **Object profile:** `references/object-profiles/{object-type}.yaml`
- **Reference data:** `references/{platform}-reference.yaml`
- **Tools:** {MCP server names}
- **Source Registry:** `registry/sources/{category}.yaml`

### {Topic 2 Name}

{Brief description.}

- **Topic index:** (create when needed)
- **Tools:** {MCP server names}

## Cross-Domain Connections

- When {condition} -> check {other domain}
- When {condition} -> check {other domain}

## Knowledge Layer Checklist

- [ ] {Standard or guide 1}
- [ ] {Standard or guide 2}
TEMPLATE

# Replace placeholder with actual domain name
sed -i '' "s/DOMAIN_PLACEHOLDER/${DOMAIN_NAME}/g" "$DOMAIN_FILE" 2>/dev/null || \
sed -i "s/DOMAIN_PLACEHOLDER/${DOMAIN_NAME}/g" "$DOMAIN_FILE"

# Create topics directory
mkdir -p "$TOPIC_DIR"

echo "Created:"
echo "  ${DOMAIN_FILE}"
echo "  ${TOPIC_DIR}/"
echo ""
echo "Next steps:"
echo "  1. Edit ${DOMAIN_FILE} and fill in the placeholders"
echo "  2. Create topic indexes: ./setup/create-topic.sh ${DOMAIN_NAME} <topic-name>"
echo "  3. Create object profiles: ./setup/create-profile.sh <object-name>"
echo "  4. Add a route in config/routing/registry.yaml"
