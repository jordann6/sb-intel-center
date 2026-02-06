# Super Bowl LX Intelligence Center

### Automated Cloud-Native Performance Analytics Platform

An end-to-end data engineering and AI pipeline designed to generate predictive scouting reports for Super Bowl LX. The system integrates real-time NFL telemetry with Large Language Models (LLMs) to provide automated player performance analysis.

## Core Architecture

- **Infrastructure-as-Code (IaC):** Provisioned Azure OpenAI, Key Vault, and Managed Identities using Terraform.
- **Data Engineering:** Extracted and processed NFLverse datasets with Python, implementing manual override logic to handle API synchronization lags.
- **Artificial Intelligence:** Leveraged Azure OpenAI (GPT-4o) for high-dimensional analysis of player prop lines versus seasonal averages.
- **Containerization & CI/CD:** Developed a Docker-based deployment model with automated builds and pushes to GitHub Container Registry (GHCR) via GitHub Actions.

## Technical Stack

- **Cloud:** Azure (OpenAI Service, Key Vault, Resource Management)
- **DevOps:** Terraform, Docker, GitHub Actions, Git
- **Language:** Python 3.11+
- **Data:** NFLverse (via nflreadpy/successor)

## Key Engineering Achievements

- **Dynamic Data Fallback:** Engineered a resilient data injection layer to bypass library-specific seasonal delays, ensuring high data accuracy during time-sensitive events.
- **Automated Lifecycle:** Managed a full SDLC from automated infrastructure provisioning to decommissioning, optimizing cloud expenditure and security.
- **Environment Parity:** Utilized Docker to ensure consistency across local development and cloud execution environments.
