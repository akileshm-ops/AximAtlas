# Research Sources & Evidence Log

---

## Source Classification

All evidence used in this research is classified by reliability tier:

### Tier 1 — User-Generated Content (Highest Priority)

| Source | Type | Key Findings |
|--------|------|-------------|
| r/dataengineering (Reddit) | Community discussion | "Spreadsheet hell" for tool comparisons; "I wish" sentiment for objective evaluation tools; Excel remains "dark secret" for data teams; Engineers warn against "resume-driven" tool selection |
| Hacker News | Community discussion | Infrastructure-first approaches fail without data flow reliability; Over-engineering warnings; "Architecture Group" viewed as bureaucracy |
| CNCF Community | Technical community | 1,200+ tools in landscape; 82% K8s production adoption; Cultural change now #1 barrier (47%), overtaking technical complexity |
| dbt Community | Product community | dbt + Snowflake is "canonical modern data stack"; Strong community consensus on transformation layer best practices |
| Stack Overflow / GitHub | Developer forums | Integration compatibility is discovered too late; Version conflict resolution is manual and painful |

### Tier 2 — Enterprise Engineering Content

| Source | Type | Key Findings |
|--------|------|-------------|
| M&A Integration Case Studies | Industry reports | 70-90% of acquisitions fail to deliver expected value from poor IT integration; "Speed vs Accuracy trap" in post-merger consolidation |
| Architecture Evolution Blogs | Technical content | Shift from monolithic to modular; Lakehouse convergence; Data Mesh as organizational paradigm, not competing architecture |
| Migration Postmortems | Engineering blogs | Wrong technology decisions cost $500K-$5M in remediation; Hidden egress costs are primary TCO surprise |
| Conference Talks (2024-2025) | Technical presentations | "Agentic Data Architecture" trend; AI-ready data foundations as prerequisite; Platform engineering reducing "YAML fatigue" |

### Tier 3 — Vendor Documentation

| Vendor | Products Reviewed | Key Extracted Data |
|--------|------------------|-------------------|
| SAP LeanIX | LeanIX EA Suite | APM-focused, SaaS-native, ~$50K-$300K/yr, no data-stack scoring |
| Bizzdesign | HoriZZon | TOGAF/ArchiMate deep modeling, ~$100K-$500K/yr, complex implementation |
| Ardoq | Ardoq Platform | Graph-based, collaborative, ~$50K-$200K/yr, no compatibility engine |
| Atlan | Data Catalog | "Context Layer for AI", ~$100K+/yr, post-deployment only |
| Collibra | Data Governance | Comprehensive governance, high TCO, long implementation cycles |
| Vantage | FinOps Platform | Multi-cloud cost visibility, post-deployment, 20+ provider integrations |
| CloudZero | Cost Intelligence | Unit economics focus, AI-native, SaaS-company-oriented |
| Infracost | Shift-Left Cost | Terraform-only IaC cost estimation, free/enterprise tiers |
| Monte Carlo | Data Observability | Category creator, ~$50K-$100K+/yr, post-deployment monitoring |
| Lucidchart | Diagramming | Enterprise standard, $7.95-$19/user/mo, static diagrams |
| Eraser.io | Technical Docs | Diagram-as-code, $8-$12/user/mo, no intelligence layer |

### Tier 4 — Independent Research

| Source | Type | Key Data Points |
|--------|------|----------------|
| Fortune Business Insights | Market sizing | EA tools market $1.2-1.35B in 2025, CAGR 4.6-8% |
| Gartner | Magic Quadrant | EA tools MQ updated October 2025; LeanIX, Bizzdesign, Ardoq as leaders |
| CNCF Annual Survey 2025 | Adoption data | 82% K8s production; 66% K8s for GenAI; 79% stateful workloads |
| G2/PeerSpot/Capterra | User reviews | Validated vendor strengths/weaknesses with real user feedback |
| Business Research Company | Market forecast | EA tools projected to $1.8-2.1B by 2034-2035 |
| Data Observability Market Reports | Market sizing | ~$1.4B in 2025, projected $3.3B by 2035 |
| Modern Data Stack Reports | Market sizing | ~$600-700M in 2025, >24% CAGR |

---

## Uncertainty Log

| Claim | Confidence | Source | Uncertainty Reason |
|-------|------------|--------|-------------------|
| Market size $1.2-1.35B for EA tools | Medium-High | Multiple analyst firms | Scope varies by report; our category doesn't cleanly map |
| 70-90% M&A failure rate | Medium | Industry reports, McKinsey | Often-cited statistic but definition of "failure" varies |
| Engineers prefer scored recommendations over gut feel | Medium | Community inference | No direct validation; assumption based on "spreadsheet fatigue" sentiment |
| $50K-$100K/yr pricing is viable | Medium | Competitor pricing | New category has no pricing anchor; may need lower entry point |
| 6 capabilities are truly unique | High | Feature matrix analysis | Competitors could add these features; uniqueness is time-bound |
| First-mover advantage is durable | Medium | Strategic analysis | Fast followers in SaaS can replicate features quickly |

---

## Research Methodology Notes

1. **Triangulation**: Every major conclusion was validated across at least 2 independent source types
2. **Vendor claims were NOT treated as validation** — corroborated with community evidence where possible
3. **Community sentiment was weighted highest** as it represents unfiltered user experience
4. **Market sizing uses conservative estimates** from the range of available analyst figures
5. **Feature matrix was constructed from actual product documentation**, not marketing pages
6. **Scoring was calibrated** to be challenging — 82/100 PMF score reflects genuine uncertainties, not optimism bias
