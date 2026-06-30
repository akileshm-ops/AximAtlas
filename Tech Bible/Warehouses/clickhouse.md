---
{
  "identity": {
    "name": "ClickHouse",
    "vendor": "ClickHouse, Inc.",
    "licensing": "Apache 2.0",
    "categorySubcategory": "Warehouses / OLAP",
    "architecturePattern": "Columnar Distributed Massively Parallel Processing (MPP) Database",
    "internalMicroserviceArchitecture": [
      "ClickHouse Keeper: Consensus coordinator",
      "MergeTree Engine: Segment data storage writer",
      "Distributed Query Processor: Aggregates sub-query results"
    ],
    "dataFlow": "Client inserts batch data -> Write to MergeTree partition segment -> Column files compressed -> Query scans columns parallelly",
    "controlPlaneDataPlane": "Keeper/ZooKeeper coordinate tables replica metadata (control plane); Distributed query execution engines scan blocks (data plane)",
    "runtimeTopology": "ClickHouse cluster nodes, replica pairs, partitioned shards",
    "storageModel": "Columnar stored data blocks, heavily compressed using LZ4/ZSTD, stored on SSDs or Object Storage",
    "computeModel": "Vectorized SIMD instruction query processing, multi-core CPU usage per query execution",
    "scalingBehavior": "Horizontal scaling by adding shards, vertical scaling by adding cores",
    "haFailover": "ReplicatedMergeTree engine, clickhouse-keeper failover automatic updates",
    "workloadSuitability": "Log analytics dashboards, high-volume clickstream analytics, time-series telemetry processing",
    "throughput": "Millions of rows inserted per second in batches",
    "latency": "Sub-100ms analytical aggregation query times",
    "concurrency": "Hundreds of concurrent complex queries per cluster",
    "slaSlo": "99.9% analytical query availability SLO",
    "mttrMtbf": "MTTR < 5 min, MTBF > 15,000 hrs",
    "rpoRto": "RPO < 1s (asynchronous replication), RTO < 10s node failover",
    "utilization": "High CPU utilization during vectorized queries, RAM cached blocks, low storage usage due to 5x+ compression ratios",
    "networkCharacteristics": "Native TCP TCP protocol, HTTP interface, high inter-node data transfer during sharded joins",
    "costDrivers": [
      "Query node compute core capacity",
      "SSD storage IOPS capability",
      "Cross-shard network egress"
    ],
    "dynamicPricingInputs": [
      "Instance CPU core counts",
      "Storage sizing volume (GB)"
    ],
    "integrationInterfaces": [
      "ClickHouse HTTP API",
      "Native TCP Driver",
      "JDBC/ODBC Drivers",
      "ClickHouse SQL Dialect"
    ],
    "supportedFormats": [
      "CSV",
      "TSV",
      "JSONEachRow",
      "Parquet",
      "Native binary"
    ],
    "nativeConnectors": [
      "Kafka Table engine",
      "S3 Table engine",
      "PostgreSQL integration engine"
    ],
    "openStandards": [
      "SQL compatibility support",
      "OpenTelemetry integration"
    ],
    "ecosystemMaturity": "Standard OLAP engine for high-performance open-source analytics",
    "securityCapabilities": [
      "LDAP/Active Directory auth integrations",
      "Row-level security policies",
      "IP address firewall restrictions"
    ],
    "governanceCapabilities": "Detailed system logs tables (query_log, part_log) for resource auditing",
    "aiReadiness": "Vector search distance functions natively built-in (L2, Cosine)",
    "vendorLockIn": "Low (Open-source analytical engine, files stored as standard columns)",
    "migrationDifficulty": "Medium (Requires schema restructuring to MergeTree partition keys)",
    "benchmarks": [
      "ClickHouse Benchmark Leaderboard positions"
    ],
    "knownBottlenecks": [
      "High latency on single-row inserts (must insert in batches > 1,000 rows)",
      "Heavy memory usage on large distributed JOIN queries"
    ],
    "antiPatterns": [
      "Using ClickHouse for point OLTP transactional updates or deletes",
      "Using as a transaction lock manager database"
    ],
    "recommendedCombinations": [
      "Kafka + ClickHouse + Grafana",
      "Airbyte + ClickHouse + Superset"
    ],
    "unsupportedCombinations": [
      "High-concurrency transactional row-level updates (OLTP)"
    ],
    "operationalRunbooks": [
      "ClickHouse Cluster Shard Rescaling Guide",
      "MergeTree Data Part Compaction Guide"
    ],
    "failureScenarios": [
      "ClickHouse Keeper consensus loss locking writes",
      "Data parts corruption on disk partition"
    ],
    "bestPractices": [
      "Always insert data in large batches (10,000+ rows)",
      "Define partition keys by date/time fields"
    ],
    "decisionRules": [
      "If analytical query latency must be < 1s over billions of rows: Choose ClickHouse",
      "If structured report BI requires SaaS warehouse: Choose Snowflake"
    ]
  },
  "decisionEngineKpis": {
    "functionalFit": {
      "score": 98.0,
      "confidence": 0.95,
      "evidence": "Superb aggregate speed OLAP database built for log analytics and telemetry datasets.",
      "contributingFactors": [
        "Columnar indexing layout",
        "Partition grouping keys"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "compatibility": {
      "score": 92.0,
      "confidence": 0.95,
      "evidence": "Provides SQL dialect and HTTP interfaces, though custom drivers are required.",
      "contributingFactors": [
        "ClickHouse SQL dialect",
        "HTTP API connector"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "performanceScalability": {
      "score": 100.0,
      "confidence": 0.95,
      "evidence": "Vectorized query compiler utilizes CPU SIMD lanes to scan billions of rows under 1s.",
      "contributingFactors": [
        "Vectorized CPU SIMD processing",
        "MergeTree part storage"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "costEfficiency": {
      "score": 85.0,
      "confidence": 0.95,
      "evidence": "Open source codebase combined with 5x+ compression ratio reduces storage storage costs.",
      "contributingFactors": [
        "LZ4/ZSTD file compression",
        "No license fees"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "reliabilityResilience": {
      "score": 92.0,
      "confidence": 0.95,
      "evidence": "ReplicatedMergeTree engine replicates data blocks asynchronously across shard nodes.",
      "contributingFactors": [
        "Keeper replication nodes",
        "Async write logs"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "operationalSimplicity": {
      "score": 70.0,
      "confidence": 0.95,
      "evidence": "ClickHouse Keeper setup and MergeTree schema tuning requires specialized operational knowledge.",
      "contributingFactors": [
        "Keeper consensus configurations",
        "MergeTree part compaction"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "futureReadiness": {
      "score": 90.0,
      "confidence": 0.95,
      "evidence": "Built-in vector distance search support, Otel metrics exporter.",
      "contributingFactors": [
        "Vector similarity functions",
        "OpenTelemetry exporter"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "ecosystemAdoption": {
      "score": 95.0,
      "confidence": 0.95,
      "evidence": "The industry standard open source OLAP engine for big data monitoring.",
      "contributingFactors": [
        "Enterprise case studies",
        "Active community forums"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "risk": {
      "score": 90.0,
      "confidence": 0.95,
      "evidence": "Low lock-in since core engine is Apache 2.0; easily migrates to ClickHouse Cloud or self-hosted servers.",
      "contributingFactors": [
        "Apache 2.0 core standard",
        "Standard column export files"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    }
  }
}
---

# ClickHouse Technology Profile

![ClickHouse Logo](https://upload.wikimedia.org/wikipedia/commons/c/c4/ClickHouse_logo.svg)

## Identity
- **Name**: ClickHouse
- **Vendor**: ClickHouse, Inc.
- **Licensing**: Apache 2.0
- **Category & subcategory**: Warehouses / OLAP

## Architecture pattern
- **Value**: Columnar Distributed Massively Parallel Processing (MPP) Database

## Internal microservice architecture
- ClickHouse Keeper: Consensus coordinator
- MergeTree Engine: Segment data storage writer
- Distributed Query Processor: Aggregates sub-query results

## Data flow
- **Value**: Client inserts batch data -> Write to MergeTree partition segment -> Column files compressed -> Query scans columns parallelly

## Control plane / data plane
- **Value**: Keeper/ZooKeeper coordinate tables replica metadata (control plane); Distributed query execution engines scan blocks (data plane)

## Runtime topology
- **Value**: ClickHouse cluster nodes, replica pairs, partitioned shards

## Storage model
- **Value**: Columnar stored data blocks, heavily compressed using LZ4/ZSTD, stored on SSDs or Object Storage

## Compute model
- **Value**: Vectorized SIMD instruction query processing, multi-core CPU usage per query execution

## Scaling behavior
- **Value**: Horizontal scaling by adding shards, vertical scaling by adding cores

## HA & failover
- **Value**: ReplicatedMergeTree engine, clickhouse-keeper failover automatic updates

## Workload suitability
- **Value**: Log analytics dashboards, high-volume clickstream analytics, time-series telemetry processing

## Throughput
- **Value**: Millions of rows inserted per second in batches

## Latency
- **Value**: Sub-100ms analytical aggregation query times

## Concurrency
- **Value**: Hundreds of concurrent complex queries per cluster

## SLA/SLO
- **Value**: 99.9% analytical query availability SLO

## MTTR / MTBF
- **Value**: MTTR < 5 min, MTBF > 15,000 hrs

## RPO / RTO
- **Value**: RPO < 1s (asynchronous replication), RTO < 10s node failover

## CPU / Memory / Storage utilization
- **Value**: High CPU utilization during vectorized queries, RAM cached blocks, low storage usage due to 5x+ compression ratios

## Network characteristics
- **Value**: Native TCP TCP protocol, HTTP interface, high inter-node data transfer during sharded joins

## Cost drivers
- Query node compute core capacity
- SSD storage IOPS capability
- Cross-shard network egress

## Dynamic pricing inputs
- Instance CPU core counts
- Storage sizing volume (GB)

## Integration interfaces
- ClickHouse HTTP API
- Native TCP Driver
- JDBC/ODBC Drivers
- ClickHouse SQL Dialect

## Supported formats
- CSV
- TSV
- JSONEachRow
- Parquet
- Native binary

## Native connectors
- Kafka Table engine
- S3 Table engine
- PostgreSQL integration engine

## Open standards
- SQL compatibility support
- OpenTelemetry integration

## Ecosystem maturity
- **Value**: Standard OLAP engine for high-performance open-source analytics

## Security capabilities
- LDAP/Active Directory auth integrations
- Row-level security policies
- IP address firewall restrictions

## Governance capabilities
- **Value**: Detailed system logs tables (query_log, part_log) for resource auditing

## AI readiness
- **Value**: Vector search distance functions natively built-in (L2, Cosine)

## Vendor lock-in
- **Value**: Low (Open-source analytical engine, files stored as standard columns)

## Migration difficulty
- **Value**: Medium (Requires schema restructuring to MergeTree partition keys)

## Benchmarks
- ClickHouse Benchmark Leaderboard positions

## Known bottlenecks
- High latency on single-row inserts (must insert in batches > 1,000 rows)
- Heavy memory usage on large distributed JOIN queries

## Anti-patterns
- Using ClickHouse for point OLTP transactional updates or deletes
- Using as a transaction lock manager database

## Recommended combinations
- Kafka + ClickHouse + Grafana
- Airbyte + ClickHouse + Superset

## Unsupported combinations
- High-concurrency transactional row-level updates (OLTP)

## Operational runbooks
- ClickHouse Cluster Shard Rescaling Guide
- MergeTree Data Part Compaction Guide

## Failure scenarios
- ClickHouse Keeper consensus loss locking writes
- Data parts corruption on disk partition

## Best practices
- Always insert data in large batches (10,000+ rows)
- Define partition keys by date/time fields

## Decision rules
- If analytical query latency must be < 1s over billions of rows: Choose ClickHouse
- If structured report BI requires SaaS warehouse: Choose Snowflake

## Decision Engine KPIs
### Functional Fit
- **Score**: 98.0 / 100
- **Confidence**: 95%
- **Evidence**: Superb aggregate speed OLAP database built for log analytics and telemetry datasets.
- **Contributing Factors**: Columnar indexing layout, Partition grouping keys

### Compatibility
- **Score**: 92.0 / 100
- **Confidence**: 95%
- **Evidence**: Provides SQL dialect and HTTP interfaces, though custom drivers are required.
- **Contributing Factors**: ClickHouse SQL dialect, HTTP API connector

### Performance Scalability
- **Score**: 100.0 / 100
- **Confidence**: 95%
- **Evidence**: Vectorized query compiler utilizes CPU SIMD lanes to scan billions of rows under 1s.
- **Contributing Factors**: Vectorized CPU SIMD processing, MergeTree part storage

### Cost Efficiency
- **Score**: 85.0 / 100
- **Confidence**: 95%
- **Evidence**: Open source codebase combined with 5x+ compression ratio reduces storage storage costs.
- **Contributing Factors**: LZ4/ZSTD file compression, No license fees

### Reliability Resilience
- **Score**: 92.0 / 100
- **Confidence**: 95%
- **Evidence**: ReplicatedMergeTree engine replicates data blocks asynchronously across shard nodes.
- **Contributing Factors**: Keeper replication nodes, Async write logs

### Operational Simplicity
- **Score**: 70.0 / 100
- **Confidence**: 95%
- **Evidence**: ClickHouse Keeper setup and MergeTree schema tuning requires specialized operational knowledge.
- **Contributing Factors**: Keeper consensus configurations, MergeTree part compaction

### Future Readiness
- **Score**: 90.0 / 100
- **Confidence**: 95%
- **Evidence**: Built-in vector distance search support, Otel metrics exporter.
- **Contributing Factors**: Vector similarity functions, OpenTelemetry exporter

### Ecosystem Adoption
- **Score**: 95.0 / 100
- **Confidence**: 95%
- **Evidence**: The industry standard open source OLAP engine for big data monitoring.
- **Contributing Factors**: Enterprise case studies, Active community forums

### Risk
- **Score**: 90.0 / 100
- **Confidence**: 95%
- **Evidence**: Low lock-in since core engine is Apache 2.0; easily migrates to ClickHouse Cloud or self-hosted servers.
- **Contributing Factors**: Apache 2.0 core standard, Standard column export files
