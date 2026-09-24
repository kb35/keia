#!/bin/bash
# Create a new topic index within a domain.
# Usage: ./setup/create-topic.sh <domain-name> <topic-name>

set -e

DOMAIN_NAME="$1"
TOPIC_NAME="$2"

if [ -z "$DOMAIN_NAME" ] || [ -z "$TOPIC_NAME" ]; then
    echo "Usage: ./setup/create-topic.sh <domain-name> <topic-name>"
    echo "Example: ./setup/create-topic.sh infrastructure network-devices"
    exit 1
fi

DOMAIN_FILE="references/domains/${DOMAIN_NAME}.md"
TOPIC_FILE="references/topics/${DOMAIN_NAME}/${TOPIC_NAME}.md"

if [ ! -f "$DOMAIN_FILE" ]; then
    echo "Error: Domain '${DOMAIN_NAME}' does not exist. Create it first:"
    echo "  ./setup/create-domain.sh ${DOMAIN_NAME}"
    exit 1
fi

if [ -f "$TOPIC_FILE" ]; then
    echo "Error: Topic '${TOPIC_NAME}' already exists at ${TOPIC_FILE}"
    exit 1
fi

mkdir -p "$(dirname "$TOPIC_FILE")"
cat > "$TOPIC_FILE" << TEMPLATE
# ${DOMAIN_NAME} Topic: ${TOPIC_NAME}

## Scope

{What this topic covers, in one paragraph.}

## Relevant Objects

- {object type 1}
- {object type 2}

## Evidence Surfaces

- \`references/object-profiles/{object-type}.yaml\`
- \`registry/sources/{category}.yaml\`
- {Platform 1} ({what it provides})
- {Platform 2} ({what it provides})

## Comparison Questions

- {Key question the agent should answer when working in this topic}
- {Another comparison question}
- {Another comparison question}

## Expansion Triggers

- {condition} -> expand into {other domain}
- {condition} -> expand into {other domain}
TEMPLATE

echo "Created: ${TOPIC_FILE}"
echo ""
echo "Next steps:"
echo "  1. Edit ${TOPIC_FILE} and fill in the placeholders"
echo "  2. Link it from ${DOMAIN_FILE} in the relevant topic section"
