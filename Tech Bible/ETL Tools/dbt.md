---
{
  "identity": {
    "name": "dbt",
    "vendor": "dbt Labs",
    "licensing": "Apache 2.0 (Core) / Proprietary",
    "categorySubcategory": "ETL Tools / Transformation",
    "architecturePattern": "SQL compiler pushing computations to the underlying warehouse layer",
    "internalMicroserviceArchitecture": [
      "dbt CLI / dbt Cloud Engine: Compiles SQL from Jinja templates and runs tests",
      "Metadata API: Exposes run metrics and model dependency logs"
    ],
    "dataFlow": "Jinja SQL templates compiled to raw SQL -> Sent via connection driver to warehouse -> Executed natively in target warehouse",
    "controlPlaneDataPlane": "dbt CLI compiler manages dependency DAG generation (control plane); The targeted data platform executes queries (data plane)",
    "runtimeTopology": "Client CLI run, Docker container runs on Kubernetes, or SaaS hosted Cloud runners",
    "storageModel": "No storage (stateless engine; writes metadata JSON artifacts locally)",
    "computeModel": "Stateless compiler, CPU usage limited to SQL parsing and connection orchestration",
    "scalingBehavior": "Stateless scaling (run multiple concurrent containers on runner engines)",
    "haFailover": "Executed tasks retried by runner orchestrator; transactional recovery by warehouse",
    "workloadSuitability": "Structured analytical data transformation modeling (SQL analytics)",
    "throughput": "Hundreds of SQL model compilation steps per second",
    "latency": "Compiler compilation delay < 1s; database execution dependent on target warehouse",
    "concurrency": "Dependent on target warehouse concurrency limits",
    "slaSlo": "Stateless engine (no SLA; Cloud tier offers 99.9% uptime SLA)",
    "mttrMtbf": "Instant container restart recovery",
    "rpoRto": "RPO = N/A (Stateless), RTO = instant compilation retry",
    "utilization": "Minimal CPU/RAM footprint, zero permanent disk storage",
    "networkCharacteristics": "Egress SQL queries to targeted warehouse network ports",
    "costDrivers": [
      "dbt Cloud seats / runner run hours",
      "Warehouse computational costs during model runs"
    ],
    "dynamicPricingInputs": [
      "Developer seat licenses",
      "Run compute credits"
    ],
    "integrationInterfaces": [
      "Command Line Interface (CLI)",
      "REST API (Cloud)",
      "Metadata API (GraphQL)"
    ],
    "supportedFormats": [
      "SQL queries",
      "YAML configurations",
      "Markdown documentation blocks"
    ],
    "nativeConnectors": [
      "dbt-snowflake",
      "dbt-bigquery",
      "dbt-postgres",
      "dbt-redshift",
      "dbt-clickhouse"
    ],
    "openStandards": [
      "Jinja templating format",
      "OpenLineage metadata specs"
    ],
    "ecosystemMaturity": "Industry standard for analytics engineering",
    "securityCapabilities": [
      "SSH Tunneling for database connection",
      "MFA/SSO login (Cloud)",
      "API Token auth"
    ],
    "governanceCapabilities": "Auto-generated interactive lineage documentation and testing suites",
    "aiReadiness": "dbt semantic layer integration for LLM SQL generators",
    "vendorLockIn": "Low (dbt SQL models are standard SQL, can be migrated to SQLMesh or run manually)",
    "migrationDifficulty": "Medium (Requires translation of Jinja variables)",
    "benchmarks": [
      "Jinja compilation speed metrics"
    ],
    "knownBottlenecks": [
      "Jinja compilation delays on projects exceeding 2,000 models",
      "Dependency serialization delays"
    ],
    "antiPatterns": [
      "Extracting or importing data into warehouses using dbt",
      "Running operational transactional row writes"
    ],
    "recommendedCombinations": [
      "Fivetran + dbt + Snowflake",
      "Airbyte + dbt + ClickHouse"
    ],
    "unsupportedCombinations": [
      "Executing real-time streaming updates on incoming streams (<1s)"
    ],
    "operationalRunbooks": [
      "dbt Model Cost Optimization Guide",
      "Testing Pipeline Debugging Runbook"
    ],
    "failureScenarios": [
      "Compilation syntax error in Jinja macros",
      "Target warehouse query execution timeouts"
    ],
    "bestPractices": [
      "Keep dbt models modular",
      "Enforce schemas and run unique and referential tests on staging tables"
    ],
    "decisionRules": [
      "If transformation layer is database-centric SQL: Use dbt",
      "If transformation layer requires Spark/Scala: Use Spark DataFrames"
    ]
  },
  "decisionEngineKpis": {
    "functionalFit": {
      "score": 96.0,
      "confidence": 0.95,
      "evidence": "Strong analytical data transformation compilation natively inside warehouses.",
      "contributingFactors": [
        "Modular SQL transformations",
        "Testing structures"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "compatibility": {
      "score": 95.0,
      "confidence": 0.95,
      "evidence": "Decoupled architecture allows dbt adapters to compile for SQL platforms.",
      "contributingFactors": [
        "dbt adapters framework",
        "OpenLineage conformance"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "performanceScalability": {
      "score": 92.0,
      "confidence": 0.95,
      "evidence": "Executes logic in target warehouses, which allows high parallel processing capabilities.",
      "contributingFactors": [
        "Parallel thread execution",
        "Push-down calculations"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "costEfficiency": {
      "score": 85.0,
      "confidence": 0.95,
      "evidence": "Open source core reduces cost, though dbt Cloud tier requires seat licensing.",
      "contributingFactors": [
        "Open source Core tier",
        "Developer seats billing"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "reliabilityResilience": {
      "score": 90.0,
      "confidence": 0.95,
      "evidence": "No state storage minimizes engine faults, SQL runs are rollbacked by target DB.",
      "contributingFactors": [
        "Stateless compile design",
        "Database transactional checks"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "operationalSimplicity": {
      "score": 85.0,
      "confidence": 0.95,
      "evidence": "Declarative YAML models reduce operational overhead.",
      "contributingFactors": [
        "Jinja templating libraries",
        "Auto-generated local schema pages"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "futureReadiness": {
      "score": 92.0,
      "confidence": 0.95,
      "evidence": "Excellent Semantic Layer APIs integration for AI LLM assistants.",
      "contributingFactors": [
        "Semantic Layer metadata",
        "GraphQL metadata API"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "ecosystemAdoption": {
      "score": 100.0,
      "confidence": 0.95,
      "evidence": "The de-facto standard transform engine for modern data stacks.",
      "contributingFactors": [
        "Global user community",
        "Extensive plugin adapters"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "risk": {
      "score": 85.0,
      "confidence": 0.95,
      "evidence": "Low lock-in since code is standard SQL queries; easily migrates to SQLMesh.",
      "contributingFactors": [
        "SQL standardization",
        "No custom data structures"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    }
  }
}
---

# dbt Technology Profile

![dbt Logo](https://raw.githubusercontent.com/devicons/devicon/master/icons/dbt/dbt-original.svg)

## Identity
- **Name**: dbt
- **Vendor**: dbt Labs
- **Licensing**: Apache 2.0 (Core) / Proprietary
- **Category & subcategory**: ETL Tools / Transformation

## Architecture pattern
- **Value**: SQL compiler pushing computations to the underlying warehouse layer

## Internal microservice architecture
- dbt CLI / dbt Cloud Engine: Compiles SQL from Jinja templates and runs tests
- Metadata API: Exposes run metrics and model dependency logs

## Data flow
- **Value**: Jinja SQL templates compiled to raw SQL -> Sent via connection driver to warehouse -> Executed natively in target warehouse

## Control plane / data plane
- **Value**: dbt CLI compiler manages dependency DAG generation (control plane); The targeted data platform executes queries (data plane)

## Runtime topology
- **Value**: Client CLI run, Docker container runs on Kubernetes, or SaaS hosted Cloud runners

## Storage model
- **Value**: No storage (stateless engine; writes metadata JSON artifacts locally)

## Compute model
- **Value**: Stateless compiler, CPU usage limited to SQL parsing and connection orchestration

## Scaling behavior
- **Value**: Stateless scaling (run multiple concurrent containers on runner engines)

## HA & failover
- **Value**: Executed tasks retried by runner orchestrator; transactional recovery by warehouse

## Workload suitability
- **Value**: Structured analytical data transformation modeling (SQL analytics)

## Throughput
- **Value**: Hundreds of SQL model compilation steps per second

## Latency
- **Value**: Compiler compilation delay < 1s; database execution dependent on target warehouse

## Concurrency
- **Value**: Dependent on target warehouse concurrency limits

## SLA/SLO
- **Value**: Stateless engine (no SLA; Cloud tier offers 99.9% uptime SLA)

## MTTR / MTBF
- **Value**: Instant container restart recovery

## RPO / RTO
- **Value**: RPO = N/A (Stateless), RTO = instant compilation retry

## CPU / Memory / Storage utilization
- **Value**: Minimal CPU/RAM footprint, zero permanent disk storage

## Network characteristics
- **Value**: Egress SQL queries to targeted warehouse network ports

## Cost drivers
- dbt Cloud seats / runner run hours
- Warehouse computational costs during model runs

## Dynamic pricing inputs
- Developer seat licenses
- Run compute credits

## Integration interfaces
- Command Line Interface (CLI)
- REST API (Cloud)
- Metadata API (GraphQL)

## Supported formats
- SQL queries
- YAML configurations
- Markdown documentation blocks

## Native connectors
- dbt-snowflake
- dbt-bigquery
- dbt-postgres
- dbt-redshift
- dbt-clickhouse

## Open standards
- Jinja templating format
- OpenLineage metadata specs

## Ecosystem maturity
- **Value**: Industry standard for analytics engineering

## Security capabilities
- SSH Tunneling for database connection
- MFA/SSO login (Cloud)
- API Token auth

## Governance capabilities
- **Value**: Auto-generated interactive lineage documentation and testing suites

## AI readiness
- **Value**: dbt semantic layer integration for LLM SQL generators

## Vendor lock-in
- **Value**: Low (dbt SQL models are standard SQL, can be migrated to SQLMesh or run manually)

## Migration difficulty
- **Value**: Medium (Requires translation of Jinja variables)

## Benchmarks
- Jinja compilation speed metrics

## Known bottlenecks
- Jinja compilation delays on projects exceeding 2,000 models
- Dependency serialization delays

## Anti-patterns
- Extracting or importing data into warehouses using dbt
- Running operational transactional row writes

## Recommended combinations
- Fivetran + dbt + Snowflake
- Airbyte + dbt + ClickHouse

## Unsupported combinations
- Executing real-time streaming updates on incoming streams (<1s)

## Operational runbooks
- dbt Model Cost Optimization Guide
- Testing Pipeline Debugging Runbook

## Failure scenarios
- Compilation syntax error in Jinja macros
- Target warehouse query execution timeouts

## Best practices
- Keep dbt models modular
- Enforce schemas and run unique and referential tests on staging tables

## Decision rules
- If transformation layer is database-centric SQL: Use dbt
- If transformation layer requires Spark/Scala: Use Spark DataFrames

## Decision Engine KPIs
### Functional Fit
- **Score**: 96.0 / 100
- **Confidence**: 95%
- **Evidence**: Strong analytical data transformation compilation natively inside warehouses.
- **Contributing Factors**: Modular SQL transformations, Testing structures

### Compatibility
- **Score**: 95.0 / 100
- **Confidence**: 95%
- **Evidence**: Decoupled architecture allows dbt adapters to compile for SQL platforms.
- **Contributing Factors**: dbt adapters framework, OpenLineage conformance

### Performance Scalability
- **Score**: 92.0 / 100
- **Confidence**: 95%
- **Evidence**: Executes logic in target warehouses, which allows high parallel processing capabilities.
- **Contributing Factors**: Parallel thread execution, Push-down calculations

### Cost Efficiency
- **Score**: 85.0 / 100
- **Confidence**: 95%
- **Evidence**: Open source core reduces cost, though dbt Cloud tier requires seat licensing.
- **Contributing Factors**: Open source Core tier, Developer seats billing

### Reliability Resilience
- **Score**: 90.0 / 100
- **Confidence**: 95%
- **Evidence**: No state storage minimizes engine faults, SQL runs are rollbacked by target DB.
- **Contributing Factors**: Stateless compile design, Database transactional checks

### Operational Simplicity
- **Score**: 85.0 / 100
- **Confidence**: 95%
- **Evidence**: Declarative YAML models reduce operational overhead.
- **Contributing Factors**: Jinja templating libraries, Auto-generated local schema pages

### Future Readiness
- **Score**: 92.0 / 100
- **Confidence**: 95%
- **Evidence**: Excellent Semantic Layer APIs integration for AI LLM assistants.
- **Contributing Factors**: Semantic Layer metadata, GraphQL metadata API

### Ecosystem Adoption
- **Score**: 100.0 / 100
- **Confidence**: 95%
- **Evidence**: The de-facto standard transform engine for modern data stacks.
- **Contributing Factors**: Global user community, Extensive plugin adapters

### Risk
- **Score**: 85.0 / 100
- **Confidence**: 95%
- **Evidence**: Low lock-in since code is standard SQL queries; easily migrates to SQLMesh.
- **Contributing Factors**: SQL standardization, No custom data structures
