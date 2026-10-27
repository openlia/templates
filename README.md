# OpenLia Templates (`https://github.com/openlia/templates.git`)

> Public community catalog of workspace profiles, modular domain features, OpenUI Mini-Projects, and workflow skills for [OpenLia](https://github.com/openlia/openlia).

OpenLia starts with an ultra-minimal generic workspace (`AGENTS.md`, `sources/`, and `inbox/ingestion/`). From this repository, you can pick and install only the profiles, domain features, Mini-Projects, and skills you need—and customize them freely while retaining upstream 3-way rebase support.

---

## Repository Structure

```text
openlia/templates
├── catalog.json             # Machine-readable index of profiles, features, and skills
├── feature.schema.json      # JSON Schema for feature.yaml manifests
├── profiles/                # Complete starter profiles (e.g., personal-os)
│   └── personal-os/
│       ├── profile.yaml
│       ├── SOUL.md
│       ├── AGENTS.md
│       └── WORKSPACE_AGENTS.md
├── features/                # Modular domain packages (workspace templates + schemas + OpenUI + skills)
│   ├── areas/
│   ├── calendar/            # requires.tools: ["remind"]
│   ├── claims/
│   ├── daily-briefing/
│   ├── decision-analysis/
│   ├── deep-research/
│   ├── goals/
│   ├── ideas/
│   ├── monitors/
│   ├── people/
│   ├── personal-finance/    # requires.tools: ["hledger"]
│   ├── personal-health/
│   ├── shopping/
│   ├── tasks/
│   └── travel/
├── skills/                  # Standalone workflow skills
│   ├── calendar/
│   ├── daily-briefing/
│   ├── document-intelligence/
│   ├── inbox-triage/
│   ├── weekly-review/
│   ├── workspace-git/
│   └── workspace-organize/
└── scripts/
    └── validate_catalog.py  # Offline validator for manifests, templates, schemas, and skill self-tests
```

---

## Usage with `openlia` CLI

```bash
# Sync the latest catalog from https://github.com/openlia/templates.git
openlia features sync

# List available features and skills
openlia features list
openlia skills list

# Install a feature (automatically provisions required tools like hledger/remind into /opt/data/.local)
openlia features install tasks
openlia features install personal-finance

# Or initialize a deployment with a starter profile
openlia init --local --template personal-os
```

## Validating the Catalog

```bash
python3 scripts/validate_catalog.py
```
