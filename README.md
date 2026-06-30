# 3D Data Stack - AXIMATLAS Workspace

This repository serves as the master workspace for the **AXIMATLAS Enterprise Data Architecture Decision Intelligence Platform**. 

It contains the overarching business research, the technology knowledge base, the application source code, and agent capabilities used to build and define the product.

## Repository Structure

- `/aximatlas`
  - The primary Next.js MVP application for AXIMATLAS. This contains the `React Flow` based 2D Architecture Canvas, the Right Inspector, the Pipeline View, and the overarching application shell. This is the main UI deliverable.
  
- `/architecture-builder`
  - Legacy or supplementary architecture tools/UI components.

- `/Business Research`
  - Contains extensive markdown documentation around Product-Market Fit (PMF) analysis, Competitive Landscape mapping, SWOT analysis, and Gap analysis.

- `/Tech Bible`
  - The core knowledge base for the platform. It contains the JSON definitions of technology stacks, compatibility rules, pricing data, and the scoring engine configuration (`rules.json`).

- `/.agents`
  - Contains AI agent skills, rules, and customizations that guide the development of this project.

## AXIMATLAS MVP

**AXIMATLAS** is not a generic diagramming tool. It is an **Enterprise Data Architecture Decision Intelligence Platform**. It is designed to allow enterprise teams to quickly define business requirements, visually map out data architectures (Sources, Ingestion, Processing, Storage, Analytics), and receive instant, deterministic feedback on:
- Architecture Health (Scores, Risks, Latency, KPIs)
- Total Cost of Ownership (TCO) & Monthly Estimates
- Compatibility edges
- Technology comparisons and alternatives

### Development

To run the main application:
```bash
cd aximatlas
npm install
npm run dev
```

Open `http://localhost:3000` to interact with the MVP.
