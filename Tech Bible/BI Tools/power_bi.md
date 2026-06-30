---
{
  "identity": {
    "name": "Power BI",
    "vendor": "Microsoft",
    "licensing": "Proprietary",
    "categorySubcategory": "BI Tools / Reporting",
    "architecturePattern": "Enterprise BI Semantic Layer & Report Visualization Engine",
    "internalMicroserviceArchitecture": [
      "Power BI Service: Cloud SaaS management portal",
      "VertiPaq Engine: In-memory columnar database compression",
      "Gateway Service: Links on-premises databases with SaaS Cloud"
    ],
    "dataFlow": "Data imported / queried via DirectQuery -> VertiPaq database processes aggregations -> Rendered charts returned to browser",
    "controlPlaneDataPlane": "Power BI Service manages reports and access rules (control plane); VertiPaq Engine processes analytics (data plane)",
    "runtimeTopology": "SaaS multi-tenant web application, local desktop designer apps",
    "storageModel": "In-memory VertiPaq compressed columnar cache or direct queries to SQL warehouses",
    "computeModel": "Heavy CPU and RAM multi-threaded computation on cloud nodes for data model evaluations",
    "scalingBehavior": "Automatic cloud scale-up based on dedicated capacity tiers (P capacities)",
    "haFailover": "Microsoft managed SaaS geo-redundancy, failover clusters",
    "workloadSuitability": "Executive dash boarding, analytical report publishing, business metric semantic modeling",
    "throughput": "Millions of dashboard renders per day",
    "latency": "Sub-second interactive click aggregations in memory",
    "concurrency": "Thousands of concurrent viewing business users per cluster capacity",
    "slaSlo": "99.9% platform availability SLA",
    "mttrMtbf": "SaaS managed, transparent to enterprise customer",
    "rpoRto": "Import cache data refresh intervals down to 30 minutes",
    "utilization": "Extremely high RAM consumption for import caches, CPU spikes on visualization rendering",
    "networkCharacteristics": "HTTPS/WSS client connections, secure data gateway channels",
    "costDrivers": [
      "Pro/Premium User Licenses",
      "Dedicated Capacity Sizing (P Tiers)",
      "Data storage capacities in cloud"
    ],
    "dynamicPricingInputs": [
      "User seat count",
      "Dedicated compute capacity tiers"
    ],
    "integrationInterfaces": [
      "Power BI REST API",
      "XMLA Read/Write Endpoint",
      "Power Automate triggers"
    ],
    "supportedFormats": [
      "DAX formulas",
      "Power Query M Language",
      "JSON theme files"
    ],
    "nativeConnectors": [
      "Microsoft SQL Server Native Connect",
      "Snowflake Connector",
      "Salesforce Connector",
      "Web connector"
    ],
    "openStandards": [
      "XMLA protocol",
      "OpenAPI schemas"
    ],
    "ecosystemMaturity": "Corporate enterprise BI market leader",
    "securityCapabilities": [
      "Active Directory integration",
      "Row-Level Security (RLS)",
      "Microsoft Purview data labeling"
    ],
    "governanceCapabilities": "Workspace workspace access control, Tenant setting logs, and audit trails",
    "aiReadiness": "Q&A natural language prompts, Copilot for report creation, integration with Azure OpenAI",
    "vendorLockIn": "High (Visual reports and DAX schemas are locked into Microsoft platform)",
    "migrationDifficulty": "High (Requires rewriting DAX schemas and rebuilding report interfaces)",
    "benchmarks": [
      "VertiPaq compression performance ratios"
    ],
    "knownBottlenecks": [
      "Import model size limitations under shared capacities (1GB max)",
      "DirectQuery performance delays under slow source databases"
    ],
    "antiPatterns": [
      "Using Power BI import memory cache as a large-scale data lake database (>100GB)",
      "Row-by-row transactional writes from visualization screens"
    ],
    "recommendedCombinations": [
      "Power BI + Azure SQL",
      "Power BI + Fabric + Snowflake"
    ],
    "unsupportedCombinations": [
      "Real-time video or high-frequency telemetry visualization (<100ms)"
    ],
    "operationalRunbooks": [
      "Capacity Refresh Failure Troubleshooting Guide",
      "Gateway Configuration Manual"
    ],
    "failureScenarios": [
      "Gateway connection loss to on-premises data sources",
      "Capacity memory exhaustion under massive import refreshes"
    ],
    "bestPractices": [
      "Optimize DAX measures to avoid nested iteration loops",
      "Use DirectQuery mode for datasets exceeding 10GB"
    ],
    "decisionRules": [
      "If enterprise uses Microsoft 365: Choose Power BI",
      "If visualization requires pure open-source embedding: Choose Apache Superset"
    ]
  },
  "decisionEngineKpis": {
    "functionalFit": {
      "score": 97.0,
      "confidence": 0.95,
      "evidence": "Superb dashboard rendering and business semantic data modeling.",
      "contributingFactors": [
        "Tabular semantic modeling",
        "DAX calculations"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "compatibility": {
      "score": 92.0,
      "confidence": 0.95,
      "evidence": "Integrates well via XMLA protocol, but proprietary visual layer restricts custom wrappers.",
      "contributingFactors": [
        "XMLA read/write endpoint",
        "DirectQuery connector bindings"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "performanceScalability": {
      "score": 90.0,
      "confidence": 0.95,
      "evidence": "VertiPaq engine compresses data up to 10x, enabling rapid local in-memory queries.",
      "contributingFactors": [
        "VertiPaq in-memory compression",
        "Query aggregator caches"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "costEfficiency": {
      "score": 75.0,
      "confidence": 0.95,
      "evidence": "Requires capacity tier sizing (P capacities) or seat billing per user.",
      "contributingFactors": [
        "Capacity tier credit limits",
        "User subscription seats"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "reliabilityResilience": {
      "score": 95.0,
      "confidence": 0.95,
      "evidence": "Microsoft SaaS cloud SLA, geo-replicated visual dashboards.",
      "contributingFactors": [
        "Microsoft SaaS SLA",
        "On-Premises Gateway standbys"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "operationalSimplicity": {
      "score": 80.0,
      "confidence": 0.95,
      "evidence": "Power BI Desktop requires Windows OS installations, Cloud Service is zero-admin.",
      "contributingFactors": [
        "Power BI service administration",
        "SaaS dashboard access control"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "futureReadiness": {
      "score": 90.0,
      "confidence": 0.95,
      "evidence": "Direct integration with Microsoft Fabric and Azure OpenAI Copilots.",
      "contributingFactors": [
        "Microsoft Fabric integration",
        "Copilot visual generator"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "ecosystemAdoption": {
      "score": 98.0,
      "confidence": 0.95,
      "evidence": "Adopted by millions of corporate users within the M365 suite.",
      "contributingFactors": [
        "Corporate enterprise ubiquity",
        "Global partner network"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "risk": {
      "score": 65.0,
      "confidence": 0.95,
      "evidence": "High platform lock-in; reports cannot run on non-Microsoft viewer engines.",
      "contributingFactors": [
        "Visual layer lock-in",
        "DAX calculations proprietary"
      ],
      "penalties": [
        {
          "factor": "Microsoft lock-in",
          "deduction": -10
        }
      ],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    }
  }
}
---

# Power BI Technology Profile

![Power BI Logo](https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg)

## Identity
- **Name**: Power BI
- **Vendor**: Microsoft
- **Licensing**: Proprietary
- **Category & subcategory**: BI Tools / Reporting

## Architecture pattern
- **Value**: Enterprise BI Semantic Layer & Report Visualization Engine

## Internal microservice architecture
- Power BI Service: Cloud SaaS management portal
- VertiPaq Engine: In-memory columnar database compression
- Gateway Service: Links on-premises databases with SaaS Cloud

## Data flow
- **Value**: Data imported / queried via DirectQuery -> VertiPaq database processes aggregations -> Rendered charts returned to browser

## Control plane / data plane
- **Value**: Power BI Service manages reports and access rules (control plane); VertiPaq Engine processes analytics (data plane)

## Runtime topology
- **Value**: SaaS multi-tenant web application, local desktop designer apps

## Storage model
- **Value**: In-memory VertiPaq compressed columnar cache or direct queries to SQL warehouses

## Compute model
- **Value**: Heavy CPU and RAM multi-threaded computation on cloud nodes for data model evaluations

## Scaling behavior
- **Value**: Automatic cloud scale-up based on dedicated capacity tiers (P capacities)

## HA & failover
- **Value**: Microsoft managed SaaS geo-redundancy, failover clusters

## Workload suitability
- **Value**: Executive dash boarding, analytical report publishing, business metric semantic modeling

## Throughput
- **Value**: Millions of dashboard renders per day

## Latency
- **Value**: Sub-second interactive click aggregations in memory

## Concurrency
- **Value**: Thousands of concurrent viewing business users per cluster capacity

## SLA/SLO
- **Value**: 99.9% platform availability SLA

## MTTR / MTBF
- **Value**: SaaS managed, transparent to enterprise customer

## RPO / RTO
- **Value**: Import cache data refresh intervals down to 30 minutes

## CPU / Memory / Storage utilization
- **Value**: Extremely high RAM consumption for import caches, CPU spikes on visualization rendering

## Network characteristics
- **Value**: HTTPS/WSS client connections, secure data gateway channels

## Cost drivers
- Pro/Premium User Licenses
- Dedicated Capacity Sizing (P Tiers)
- Data storage capacities in cloud

## Dynamic pricing inputs
- User seat count
- Dedicated compute capacity tiers

## Integration interfaces
- Power BI REST API
- XMLA Read/Write Endpoint
- Power Automate triggers

## Supported formats
- DAX formulas
- Power Query M Language
- JSON theme files

## Native connectors
- Microsoft SQL Server Native Connect
- Snowflake Connector
- Salesforce Connector
- Web connector

## Open standards
- XMLA protocol
- OpenAPI schemas

## Ecosystem maturity
- **Value**: Corporate enterprise BI market leader

## Security capabilities
- Active Directory integration
- Row-Level Security (RLS)
- Microsoft Purview data labeling

## Governance capabilities
- **Value**: Workspace workspace access control, Tenant setting logs, and audit trails

## AI readiness
- **Value**: Q&A natural language prompts, Copilot for report creation, integration with Azure OpenAI

## Vendor lock-in
- **Value**: High (Visual reports and DAX schemas are locked into Microsoft platform)

## Migration difficulty
- **Value**: High (Requires rewriting DAX schemas and rebuilding report interfaces)

## Benchmarks
- VertiPaq compression performance ratios

## Known bottlenecks
- Import model size limitations under shared capacities (1GB max)
- DirectQuery performance delays under slow source databases

## Anti-patterns
- Using Power BI import memory cache as a large-scale data lake database (>100GB)
- Row-by-row transactional writes from visualization screens

## Recommended combinations
- Power BI + Azure SQL
- Power BI + Fabric + Snowflake

## Unsupported combinations
- Real-time video or high-frequency telemetry visualization (<100ms)

## Operational runbooks
- Capacity Refresh Failure Troubleshooting Guide
- Gateway Configuration Manual

## Failure scenarios
- Gateway connection loss to on-premises data sources
- Capacity memory exhaustion under massive import refreshes

## Best practices
- Optimize DAX measures to avoid nested iteration loops
- Use DirectQuery mode for datasets exceeding 10GB

## Decision rules
- If enterprise uses Microsoft 365: Choose Power BI
- If visualization requires pure open-source embedding: Choose Apache Superset

## Decision Engine KPIs
### Functional Fit
- **Score**: 97.0 / 100
- **Confidence**: 95%
- **Evidence**: Superb dashboard rendering and business semantic data modeling.
- **Contributing Factors**: Tabular semantic modeling, DAX calculations

### Compatibility
- **Score**: 92.0 / 100
- **Confidence**: 95%
- **Evidence**: Integrates well via XMLA protocol, but proprietary visual layer restricts custom wrappers.
- **Contributing Factors**: XMLA read/write endpoint, DirectQuery connector bindings

### Performance Scalability
- **Score**: 90.0 / 100
- **Confidence**: 95%
- **Evidence**: VertiPaq engine compresses data up to 10x, enabling rapid local in-memory queries.
- **Contributing Factors**: VertiPaq in-memory compression, Query aggregator caches

### Cost Efficiency
- **Score**: 75.0 / 100
- **Confidence**: 95%
- **Evidence**: Requires capacity tier sizing (P capacities) or seat billing per user.
- **Contributing Factors**: Capacity tier credit limits, User subscription seats

### Reliability Resilience
- **Score**: 95.0 / 100
- **Confidence**: 95%
- **Evidence**: Microsoft SaaS cloud SLA, geo-replicated visual dashboards.
- **Contributing Factors**: Microsoft SaaS SLA, On-Premises Gateway standbys

### Operational Simplicity
- **Score**: 80.0 / 100
- **Confidence**: 95%
- **Evidence**: Power BI Desktop requires Windows OS installations, Cloud Service is zero-admin.
- **Contributing Factors**: Power BI service administration, SaaS dashboard access control

### Future Readiness
- **Score**: 90.0 / 100
- **Confidence**: 95%
- **Evidence**: Direct integration with Microsoft Fabric and Azure OpenAI Copilots.
- **Contributing Factors**: Microsoft Fabric integration, Copilot visual generator

### Ecosystem Adoption
- **Score**: 98.0 / 100
- **Confidence**: 95%
- **Evidence**: Adopted by millions of corporate users within the M365 suite.
- **Contributing Factors**: Corporate enterprise ubiquity, Global partner network

### Risk
- **Score**: 65.0 / 100
- **Confidence**: 95%
- **Evidence**: High platform lock-in; reports cannot run on non-Microsoft viewer engines.
- **Contributing Factors**: Visual layer lock-in, DAX calculations proprietary
