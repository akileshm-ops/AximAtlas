---
{
  "identity": {
    "name": "OpenMetadata",
    "vendor": "Collate Inc. (backed)",
    "licensing": "Apache 2.0",
    "categorySubcategory": "Cloud Services / Infrastructure",
    "architecturePattern": "Centralized Metadata Engine with Unified Schema Standard",
    "internalMicroserviceArchitecture": [
      "OpenMetadata Server: Java/Dropwizard REST API application",
      "Elasticsearch / OpenSearch: Search index store",
      "Database: Stores core metadata entities"
    ],
    "dataFlow": "Ingestion connectors poll system APIs -> Publish metadata JSON payloads to OM Server -> Server writes to DB and indexing search engine",
    "controlPlaneDataPlane": "Server API and relational DB store metadata entities (control plane); Elasticsearch indexes search queries (data plane)",
    "runtimeTopology": "Docker Compose deployment or Kubernetes pods",
    "storageModel": "MySQL/PostgreSQL storing system records, Elasticsearch storing search indexes",
    "computeModel": "Stateful Java API runtime, CPU utilization tied to metadata ingestion runs",
    "scalingBehavior": "Scale server instances horizontally behind load balancers",
    "haFailover": "Multi-instance API server deployments, Elasticsearch cluster redundancy",
    "workloadSuitability": "Enterprise metadata cataloging, data lineage tracking, collaboration around data quality",
    "throughput": "Thousands of metadata ingestion updates per second",
    "latency": "Sub-100ms API response times for queries",
    "concurrency": "Hundreds of concurrent metadata developers and business users",
    "slaSlo": "99.9% platform availability SLO",
    "mttrMtbf": "MTTR < 10 min, MTBF > 8,000 hrs",
    "rpoRto": "RPO = 5s DB transaction log, RTO < 2 min",
    "utilization": "Low CPU/RAM database engine footprint, Elasticsearch memory intensive",
    "networkCharacteristics": "HTTP/JSON REST API, TLS 1.3, internal gRPC profiling",
    "costDrivers": [
      "Elasticsearch storage/compute pricing",
      "Database backend sizing",
      "Connector ingestion VM runtime"
    ],
    "dynamicPricingInputs": [
      "Number of metadata assets ingested",
      "Server instance sizing"
    ],
    "integrationInterfaces": [
      "REST API",
      "Python SDK",
      "dbt manifest integration hooks"
    ],
    "supportedFormats": [
      "JSON Schema metadata specs",
      "JSON-LD graph patterns"
    ],
    "nativeConnectors": [
      "Snowflake Catalog Connect",
      "Tableau Lineage Connect",
      "dbt Core Manifest Connect",
      "Kafka Schema Registry Connect"
    ],
    "openStandards": [
      "W3C Metadata standards",
      "OpenMetadata Schema spec"
    ],
    "ecosystemMaturity": "Evolving standard for modern data governance catalogs",
    "securityCapabilities": [
      "SSO integrations (Okta, Azure AD, Auth0)",
      "JWT token API authentication",
      "RBAC policy manager"
    ],
    "governanceCapabilities": "Schema version change tracing, taxonomy glossary assignments, and ownership metrics",
    "aiReadiness": "Metadata semantic search powered by OpenSearch vectors",
    "vendorLockIn": "Low (Metadata definitions are open JSON schema models, easily exportable)",
    "migrationDifficulty": "Medium (Requires translating asset configurations from legacy systems)",
    "benchmarks": [
      "Ingestion performance tests with >100k metadata assets"
    ],
    "knownBottlenecks": [
      "Lineage generation speeds on complex tables with millions of queries",
      "Elasticsearch synchronization delays"
    ],
    "antiPatterns": [
      "Storing raw target transactional data inside OpenMetadata database",
      "Using OM API as a high-frequency real-time messaging queue"
    ],
    "recommendedCombinations": [
      "OpenMetadata + dbt + Snowflake",
      "OpenMetadata + Airflow + Spark"
    ],
    "unsupportedCombinations": [
      "Visual reporting database storage"
    ],
    "operationalRunbooks": [
      "Metadata DB Migration Runbook",
      "Search Index Rebuild Guide"
    ],
    "failureScenarios": [
      "Database out-of-sync with Elasticsearch",
      "Ingestion pipeline credentials loss"
    ],
    "bestPractices": [
      "Automate metadata updates via Airflow workflows",
      "Define clear glossary naming rules before tagging assets"
    ],
    "decisionRules": [
      "If unified API-driven metadata model is required: Choose OpenMetadata",
      "If pure lineage with no collaboration controls: Choose OpenLineage"
    ]
  },
  "decisionEngineKpis": {
    "functionalFit": {
      "score": 95.0,
      "confidence": 0.95,
      "evidence": "Excellent metadata cataloging with unified schema specifications.",
      "contributingFactors": [
        "Unified schema models",
        "Data lineage graphs"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "compatibility": {
      "score": 95.0,
      "confidence": 0.95,
      "evidence": "Provides JSON schema specs and W3C standard compliance.",
      "contributingFactors": [
        "W3C Metadata spec",
        "REST API interfaces"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "performanceScalability": {
      "score": 85.0,
      "confidence": 0.95,
      "evidence": "Handles hundreds of thousands of catalog records, backed by OpenSearch indexing.",
      "contributingFactors": [
        "Elasticsearch index scans",
        "Ingestion scheduling"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "costEfficiency": {
      "score": 80.0,
      "confidence": 0.95,
      "evidence": "Open source core reduces cost, though hosted SaaS capacities apply.",
      "contributingFactors": [
        "Open source core standard",
        "Ingestion VM resource costs"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "reliabilityResilience": {
      "score": 90.0,
      "confidence": 0.95,
      "evidence": "Standard multi-instance deployments, backend relational DB clustering.",
      "contributingFactors": [
        "MySQL/Postgres standbys",
        "Elasticsearch replication"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "operationalSimplicity": {
      "score": 75.0,
      "confidence": 0.95,
      "evidence": "Requires managing Elasticsearch and ingestion agents alongside Java server.",
      "contributingFactors": [
        "Elasticsearch maintenance",
        "Ingestion connector keys"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "futureReadiness": {
      "score": 92.0,
      "confidence": 0.95,
      "evidence": "API-first model easily feeds AI search agents and LLM catalogs.",
      "contributingFactors": [
        "Semantic open catalog",
        "JSON schema standards"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "ecosystemAdoption": {
      "score": 88.0,
      "confidence": 0.95,
      "evidence": "Highly adopted by modern enterprise governance teams.",
      "contributingFactors": [
        "Broad enterprise support",
        "Active Collate SaaS"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "risk": {
      "score": 90.0,
      "confidence": 0.95,
      "evidence": "Low lock-in since metadata schemas are open standards.",
      "contributingFactors": [
        "JSON schema compliance",
        "Open API data outputs"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    }
  }
}
---

# OpenMetadata Technology Profile

![OpenMetadata Logo](https://github.com/open-metadata/OpenMetadata/raw/main/openmetadata-docs-v1/images/openmetadata-logo.png)

## Identity
- **Name**: OpenMetadata
- **Vendor**: Collate Inc. (backed)
- **Licensing**: Apache 2.0
- **Category & subcategory**: Cloud Services / Infrastructure

## Architecture pattern
- **Value**: Centralized Metadata Engine with Unified Schema Standard

## Internal microservice architecture
- OpenMetadata Server: Java/Dropwizard REST API application
- Elasticsearch / OpenSearch: Search index store
- Database: Stores core metadata entities

## Data flow
- **Value**: Ingestion connectors poll system APIs -> Publish metadata JSON payloads to OM Server -> Server writes to DB and indexing search engine

## Control plane / data plane
- **Value**: Server API and relational DB store metadata entities (control plane); Elasticsearch indexes search queries (data plane)

## Runtime topology
- **Value**: Docker Compose deployment or Kubernetes pods

## Storage model
- **Value**: MySQL/PostgreSQL storing system records, Elasticsearch storing search indexes

## Compute model
- **Value**: Stateful Java API runtime, CPU utilization tied to metadata ingestion runs

## Scaling behavior
- **Value**: Scale server instances horizontally behind load balancers

## HA & failover
- **Value**: Multi-instance API server deployments, Elasticsearch cluster redundancy

## Workload suitability
- **Value**: Enterprise metadata cataloging, data lineage tracking, collaboration around data quality

## Throughput
- **Value**: Thousands of metadata ingestion updates per second

## Latency
- **Value**: Sub-100ms API response times for queries

## Concurrency
- **Value**: Hundreds of concurrent metadata developers and business users

## SLA/SLO
- **Value**: 99.9% platform availability SLO

## MTTR / MTBF
- **Value**: MTTR < 10 min, MTBF > 8,000 hrs

## RPO / RTO
- **Value**: RPO = 5s DB transaction log, RTO < 2 min

## CPU / Memory / Storage utilization
- **Value**: Low CPU/RAM database engine footprint, Elasticsearch memory intensive

## Network characteristics
- **Value**: HTTP/JSON REST API, TLS 1.3, internal gRPC profiling

## Cost drivers
- Elasticsearch storage/compute pricing
- Database backend sizing
- Connector ingestion VM runtime

## Dynamic pricing inputs
- Number of metadata assets ingested
- Server instance sizing

## Integration interfaces
- REST API
- Python SDK
- dbt manifest integration hooks

## Supported formats
- JSON Schema metadata specs
- JSON-LD graph patterns

## Native connectors
- Snowflake Catalog Connect
- Tableau Lineage Connect
- dbt Core Manifest Connect
- Kafka Schema Registry Connect

## Open standards
- W3C Metadata standards
- OpenMetadata Schema spec

## Ecosystem maturity
- **Value**: Evolving standard for modern data governance catalogs

## Security capabilities
- SSO integrations (Okta, Azure AD, Auth0)
- JWT token API authentication
- RBAC policy manager

## Governance capabilities
- **Value**: Schema version change tracing, taxonomy glossary assignments, and ownership metrics

## AI readiness
- **Value**: Metadata semantic search powered by OpenSearch vectors

## Vendor lock-in
- **Value**: Low (Metadata definitions are open JSON schema models, easily exportable)

## Migration difficulty
- **Value**: Medium (Requires translating asset configurations from legacy systems)

## Benchmarks
- Ingestion performance tests with >100k metadata assets

## Known bottlenecks
- Lineage generation speeds on complex tables with millions of queries
- Elasticsearch synchronization delays

## Anti-patterns
- Storing raw target transactional data inside OpenMetadata database
- Using OM API as a high-frequency real-time messaging queue

## Recommended combinations
- OpenMetadata + dbt + Snowflake
- OpenMetadata + Airflow + Spark

## Unsupported combinations
- Visual reporting database storage

## Operational runbooks
- Metadata DB Migration Runbook
- Search Index Rebuild Guide

## Failure scenarios
- Database out-of-sync with Elasticsearch
- Ingestion pipeline credentials loss

## Best practices
- Automate metadata updates via Airflow workflows
- Define clear glossary naming rules before tagging assets

## Decision rules
- If unified API-driven metadata model is required: Choose OpenMetadata
- If pure lineage with no collaboration controls: Choose OpenLineage

## Decision Engine KPIs
### Functional Fit
- **Score**: 95.0 / 100
- **Confidence**: 95%
- **Evidence**: Excellent metadata cataloging with unified schema specifications.
- **Contributing Factors**: Unified schema models, Data lineage graphs

### Compatibility
- **Score**: 95.0 / 100
- **Confidence**: 95%
- **Evidence**: Provides JSON schema specs and W3C standard compliance.
- **Contributing Factors**: W3C Metadata spec, REST API interfaces

### Performance Scalability
- **Score**: 85.0 / 100
- **Confidence**: 95%
- **Evidence**: Handles hundreds of thousands of catalog records, backed by OpenSearch indexing.
- **Contributing Factors**: Elasticsearch index scans, Ingestion scheduling

### Cost Efficiency
- **Score**: 80.0 / 100
- **Confidence**: 95%
- **Evidence**: Open source core reduces cost, though hosted SaaS capacities apply.
- **Contributing Factors**: Open source core standard, Ingestion VM resource costs

### Reliability Resilience
- **Score**: 90.0 / 100
- **Confidence**: 95%
- **Evidence**: Standard multi-instance deployments, backend relational DB clustering.
- **Contributing Factors**: MySQL/Postgres standbys, Elasticsearch replication

### Operational Simplicity
- **Score**: 75.0 / 100
- **Confidence**: 95%
- **Evidence**: Requires managing Elasticsearch and ingestion agents alongside Java server.
- **Contributing Factors**: Elasticsearch maintenance, Ingestion connector keys

### Future Readiness
- **Score**: 92.0 / 100
- **Confidence**: 95%
- **Evidence**: API-first model easily feeds AI search agents and LLM catalogs.
- **Contributing Factors**: Semantic open catalog, JSON schema standards

### Ecosystem Adoption
- **Score**: 88.0 / 100
- **Confidence**: 95%
- **Evidence**: Highly adopted by modern enterprise governance teams.
- **Contributing Factors**: Broad enterprise support, Active Collate SaaS

### Risk
- **Score**: 90.0 / 100
- **Confidence**: 95%
- **Evidence**: Low lock-in since metadata schemas are open standards.
- **Contributing Factors**: JSON schema compliance, Open API data outputs
