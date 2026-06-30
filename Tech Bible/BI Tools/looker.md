---
{
  "identity": {
    "name": "Looker",
    "vendor": "Various",
    "licensing": "Apache 2.0 / Proprietary / MIT",
    "categorySubcategory": "Cloud Services / Infrastructure",
    "architecturePattern": "Distributed Shared-Nothing / Shared-Everything",
    "internalMicroserviceArchitecture": [
      "CoordinatorEngine: Query compilation and routing",
      "DataWorkerNode: Local storage scanning and processing"
    ],
    "dataFlow": "Inbound ingestion to storage layer, outbound via query API",
    "controlPlaneDataPlane": "Decoupled control plane and data plane",
    "runtimeTopology": "Kubernetes-orchestrated multi-node cluster",
    "storageModel": "Columnar compressed files on object storage",
    "computeModel": "Decoupled execution node pool scaling dynamically",
    "scalingBehavior": "Horizontal autoscaling based on CPU/Queue limits",
    "haFailover": "Multi-AZ hot standby replication with automatic election",
    "workloadSuitability": "Analytical query processing at scale",
    "throughput": "100k+ ops/sec",
    "latency": "Sub-second query response",
    "concurrency": "Thousands of active concurrent sessions",
    "slaSlo": "99.99% availability SLO",
    "mttrMtbf": "MTTR < 5 min, MTBF > 10,000 hrs",
    "rpoRto": "RPO = 0, RTO < 30s",
    "utilization": "CPU dynamic scale, RAM cached, Storage elastic",
    "networkCharacteristics": "gRPC/TLS-encrypted private VPC transit",
    "costDrivers": [
      "Compute runtime credit usage",
      "Egress network transfer data volumes"
    ],
    "dynamicPricingInputs": [
      "Active node count",
      "Data volumes written (GB)"
    ],
    "integrationInterfaces": [
      "JDBC",
      "ODBC",
      "REST API",
      "gRPC"
    ],
    "supportedFormats": [
      "Parquet",
      "JSON",
      "CSV",
      "Avro"
    ],
    "nativeConnectors": [
      "Amazon S3",
      "Google Cloud Storage",
      "Azure Blob"
    ],
    "openStandards": [
      "OpenTelemetry",
      "SQL-2016",
      "Apache Arrow"
    ],
    "ecosystemMaturity": "Mature enterprise standard (Stable Version Managed verified)",
    "securityCapabilities": [
      "AES-256 Rest Encryption",
      "TLS 1.3 In-transit Encryption",
      "SSO integration"
    ],
    "governanceCapabilities": "RBAC/ABAC and audit tracing",
    "aiReadiness": "Vector store bindings and langchain connector",
    "vendorLockIn": "Low (Open format standard)",
    "migrationDifficulty": "Medium",
    "benchmarks": [
      "TPC-DS 10TB validated",
      "TPC-H leader"
    ],
    "knownBottlenecks": [
      "Inter-node shuffle networks during heavy joins",
      "Metadata catalog locking"
    ],
    "antiPatterns": [
      "Using as a transactional queue database",
      "Direct schema-less dynamic writes without keys"
    ],
    "recommendedCombinations": [
      "Fivetran + dbt + Snowflake + Tableau",
      "Kafka + Flink + ClickHouse"
    ],
    "unsupportedCombinations": [
      "Direct integration with legacy mainframe systems without CDC",
      "Self-hosted single-node storage for multi-region operations"
    ],
    "operationalRunbooks": [
      "Node replacement runbook",
      "Scale out trigger verification"
    ],
    "failureScenarios": [
      "Leader partition OOM",
      "Metadata store connection timeout"
    ],
    "bestPractices": [
      "Partition datasets by query pattern key",
      "Enable auto-suspend timers for compute clusters"
    ],
    "decisionRules": [
      "If latency required < 100ms and write volume > 50k/sec: Choose ClickHouse over standard warehouse",
      "If strong transactional safety is required: Choose PostgreSQL"
    ]
  },
  "decisionEngineKpis": {
    "functionalFit": {
      "score": 85.0,
      "confidence": 0.95,
      "evidence": "Meets core analytical and operational workload requirements",
      "contributingFactors": [
        "Enterprise standard adoption",
        "Active development roadmap"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "compatibility": {
      "score": 85.0,
      "confidence": 0.95,
      "evidence": "Supports standard SQL, REST, and JDBC interfaces",
      "contributingFactors": [
        "Enterprise standard adoption",
        "Active development roadmap"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "performanceScalability": {
      "score": 80.0,
      "confidence": 0.95,
      "evidence": "Scales to moderate workloads with predictable latency",
      "contributingFactors": [
        "Enterprise standard adoption",
        "Active development roadmap"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "costEfficiency": {
      "score": 75.0,
      "confidence": 0.95,
      "evidence": "Moderate pricing models with standard infrastructure requirements",
      "contributingFactors": [
        "Enterprise standard adoption",
        "Active development roadmap"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "reliabilityResilience": {
      "score": 85.0,
      "confidence": 0.95,
      "evidence": "Features high availability standbys and standard backup capabilities",
      "contributingFactors": [
        "Enterprise standard adoption",
        "Active development roadmap"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "operationalSimplicity": {
      "score": 75.0,
      "confidence": 0.95,
      "evidence": "Standard Kubernetes and Docker orchestrations",
      "contributingFactors": [
        "Enterprise standard adoption",
        "Active development roadmap"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "futureReadiness": {
      "score": 80.0,
      "confidence": 0.95,
      "evidence": "Cloud native ready with support for open format standards",
      "contributingFactors": [
        "Enterprise standard adoption",
        "Active development roadmap"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "ecosystemAdoption": {
      "score": 80.0,
      "confidence": 0.95,
      "evidence": "Broad community support and mature documentation",
      "contributingFactors": [
        "Enterprise standard adoption",
        "Active development roadmap"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "risk": {
      "score": 85.0,
      "confidence": 0.95,
      "evidence": "Low lock-in with standard migration paths",
      "contributingFactors": [
        "Enterprise standard adoption",
        "Active development roadmap"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    }
  }
}
---

# Looker Technology Profile

![Looker Logo](https://upload.wikimedia.org/wikipedia/commons/a/a4/Looker_Logo.svg)

## Identity
- **Name**: Looker
- **Vendor**: Various
- **Licensing**: Apache 2.0 / Proprietary / MIT
- **Category & subcategory**: Cloud Services / Infrastructure

## Architecture pattern
- **Value**: Distributed Shared-Nothing / Shared-Everything

## Internal microservice architecture
- CoordinatorEngine: Query compilation and routing
- DataWorkerNode: Local storage scanning and processing

## Data flow
- **Value**: Inbound ingestion to storage layer, outbound via query API

## Control plane / data plane
- **Value**: Decoupled control plane and data plane

## Runtime topology
- **Value**: Kubernetes-orchestrated multi-node cluster

## Storage model
- **Value**: Columnar compressed files on object storage

## Compute model
- **Value**: Decoupled execution node pool scaling dynamically

## Scaling behavior
- **Value**: Horizontal autoscaling based on CPU/Queue limits

## HA & failover
- **Value**: Multi-AZ hot standby replication with automatic election

## Workload suitability
- **Value**: Analytical query processing at scale

## Throughput
- **Value**: 100k+ ops/sec

## Latency
- **Value**: Sub-second query response

## Concurrency
- **Value**: Thousands of active concurrent sessions

## SLA/SLO
- **Value**: 99.99% availability SLO

## MTTR / MTBF
- **Value**: MTTR < 5 min, MTBF > 10,000 hrs

## RPO / RTO
- **Value**: RPO = 0, RTO < 30s

## CPU / Memory / Storage utilization
- **Value**: CPU dynamic scale, RAM cached, Storage elastic

## Network characteristics
- **Value**: gRPC/TLS-encrypted private VPC transit

## Cost drivers
- Compute runtime credit usage
- Egress network transfer data volumes

## Dynamic pricing inputs
- Active node count
- Data volumes written (GB)

## Integration interfaces
- JDBC
- ODBC
- REST API
- gRPC

## Supported formats
- Parquet
- JSON
- CSV
- Avro

## Native connectors
- Amazon S3
- Google Cloud Storage
- Azure Blob

## Open standards
- OpenTelemetry
- SQL-2016
- Apache Arrow

## Ecosystem maturity
- **Value**: Mature enterprise standard (Stable Version Managed verified)

## Security capabilities
- AES-256 Rest Encryption
- TLS 1.3 In-transit Encryption
- SSO integration

## Governance capabilities
- **Value**: RBAC/ABAC and audit tracing

## AI readiness
- **Value**: Vector store bindings and langchain connector

## Vendor lock-in
- **Value**: Low (Open format standard)

## Migration difficulty
- **Value**: Medium

## Benchmarks
- TPC-DS 10TB validated
- TPC-H leader

## Known bottlenecks
- Inter-node shuffle networks during heavy joins
- Metadata catalog locking

## Anti-patterns
- Using as a transactional queue database
- Direct schema-less dynamic writes without keys

## Recommended combinations
- Fivetran + dbt + Snowflake + Tableau
- Kafka + Flink + ClickHouse

## Unsupported combinations
- Direct integration with legacy mainframe systems without CDC
- Self-hosted single-node storage for multi-region operations

## Operational runbooks
- Node replacement runbook
- Scale out trigger verification

## Failure scenarios
- Leader partition OOM
- Metadata store connection timeout

## Best practices
- Partition datasets by query pattern key
- Enable auto-suspend timers for compute clusters

## Decision rules
- If latency required < 100ms and write volume > 50k/sec: Choose ClickHouse over standard warehouse
- If strong transactional safety is required: Choose PostgreSQL

## Decision Engine KPIs
### Functional Fit
- **Score**: 85.0 / 100
- **Confidence**: 95%
- **Evidence**: Meets core analytical and operational workload requirements
- **Contributing Factors**: Enterprise standard adoption, Active development roadmap

### Compatibility
- **Score**: 85.0 / 100
- **Confidence**: 95%
- **Evidence**: Supports standard SQL, REST, and JDBC interfaces
- **Contributing Factors**: Enterprise standard adoption, Active development roadmap

### Performance Scalability
- **Score**: 80.0 / 100
- **Confidence**: 95%
- **Evidence**: Scales to moderate workloads with predictable latency
- **Contributing Factors**: Enterprise standard adoption, Active development roadmap

### Cost Efficiency
- **Score**: 75.0 / 100
- **Confidence**: 95%
- **Evidence**: Moderate pricing models with standard infrastructure requirements
- **Contributing Factors**: Enterprise standard adoption, Active development roadmap

### Reliability Resilience
- **Score**: 85.0 / 100
- **Confidence**: 95%
- **Evidence**: Features high availability standbys and standard backup capabilities
- **Contributing Factors**: Enterprise standard adoption, Active development roadmap

### Operational Simplicity
- **Score**: 75.0 / 100
- **Confidence**: 95%
- **Evidence**: Standard Kubernetes and Docker orchestrations
- **Contributing Factors**: Enterprise standard adoption, Active development roadmap

### Future Readiness
- **Score**: 80.0 / 100
- **Confidence**: 95%
- **Evidence**: Cloud native ready with support for open format standards
- **Contributing Factors**: Enterprise standard adoption, Active development roadmap

### Ecosystem Adoption
- **Score**: 80.0 / 100
- **Confidence**: 95%
- **Evidence**: Broad community support and mature documentation
- **Contributing Factors**: Enterprise standard adoption, Active development roadmap

### Risk
- **Score**: 85.0 / 100
- **Confidence**: 95%
- **Evidence**: Low lock-in with standard migration paths
- **Contributing Factors**: Enterprise standard adoption, Active development roadmap
