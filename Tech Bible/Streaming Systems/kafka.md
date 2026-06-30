---
{
  "identity": {
    "name": "Apache Kafka",
    "vendor": "Apache Software Foundation",
    "licensing": "Apache 2.0",
    "categorySubcategory": "Streaming / Messaging",
    "architecturePattern": "Distributed Pub-Sub Append-Only Commit Log",
    "internalMicroserviceArchitecture": [
      "Kafka Broker: Manages topics, partitions, and storage logs",
      "ZooKeeper/KRaft: Manages cluster metadata and leader elections"
    ],
    "dataFlow": "Producers send records to partitions -> Append-only write to disk -> Consumers pull logs from specific offsets",
    "controlPlaneDataPlane": "KRaft controller nodes manage metadata (control plane); Brokers manage partition logs and network IO (data plane)",
    "runtimeTopology": "Multi-broker cluster spanning multi-AZ, synchronized via KRaft",
    "storageModel": "Direct append-only local files with OS page cache optimizations",
    "computeModel": "Event-loop network handling, decoupled from storage commits",
    "scalingBehavior": "Scale horizontally by adding brokers and reassigning partition slices",
    "haFailover": "In-Sync Replicas (ISR) model, automatic leader partition election",
    "workloadSuitability": "High-throughput stream processing, CDC, microservice decoupling",
    "throughput": "Millions of messages/sec",
    "latency": "Sub-10ms write-to-read",
    "concurrency": "Tens of thousands of active clients",
    "slaSlo": "99.999% stream availability",
    "mttrMtbf": "MTTR < 2 min, MTBF > 25,000 hrs",
    "rpoRto": "RPO = 0 (synced replication), RTO < 10s partition failover",
    "utilization": "High Network IO utilization, heavy RAM page cache usage, linear storage growth",
    "networkCharacteristics": "TCP-based binary protocol, TLS 1.3, cross-AZ traffic overhead",
    "costDrivers": [
      "Retention period size",
      "Cross-AZ replication volume",
      "Broker VM count"
    ],
    "dynamicPricingInputs": [
      "Egress data (GB)",
      "Compute instance types",
      "Storage volumes (GB)"
    ],
    "integrationInterfaces": [
      "Kafka Client API",
      "REST Proxy",
      "Kafka Connect",
      "gRPC wrappers"
    ],
    "supportedFormats": [
      "Avro",
      "JSON",
      "Protobuf",
      "Binary",
      "CSV"
    ],
    "nativeConnectors": [
      "JDBC Source/Sink",
      "Debezium Connectors",
      "S3 Sink",
      "Elasticsearch Sink"
    ],
    "openStandards": [
      "CloudEvents",
      "OpenTelemetry",
      "JMX metrics"
    ],
    "ecosystemMaturity": "Industry standard event streaming backbone",
    "securityCapabilities": [
      "SASL/SCRAM",
      "SASL/GSSAPI (Kerberos)",
      "mTLS",
      "ACL authorization"
    ],
    "governanceCapabilities": "Schema Registry integration and ACL access auditing",
    "aiReadiness": "Kafka Streams binding for live vector indexing pipelines",
    "vendorLockIn": "Very Low (Open-source standard, drop-in replacements like Redpanda exist)",
    "migrationDifficulty": "Medium (Requires partition mirror-maker setups)",
    "benchmarks": [
      "1 GB/sec throughput validation (Confluent Benchmarks)"
    ],
    "knownBottlenecks": [
      "Partition rebalancing locks consumer groups",
      "JVM Garbage Collection pauses"
    ],
    "antiPatterns": [
      "Using Kafka as a permanent relational database with query lookups",
      "Large payload messages (>10MB)"
    ],
    "recommendedCombinations": [
      "Kafka + Flink + ClickHouse",
      "Debezium + Kafka + Snowflake"
    ],
    "unsupportedCombinations": [
      "Direct synchronous HTTP client callbacks from Kafka Broker"
    ],
    "operationalRunbooks": [
      "Partition Reassignment Runbook",
      "KRaft Metadata Recovery Guide"
    ],
    "failureScenarios": [
      "Broker OOM under consumer lag",
      "Zookeeper network partition split-brain"
    ],
    "bestPractices": [
      "Keep message size below 1MB",
      "Set replication factor to 3 in production"
    ],
    "decisionRules": [
      "If stream processing required with latency < 50ms: Use Kafka",
      "If simple pub-sub with low volume: Use RabbitMQ"
    ]
  },
  "decisionEngineKpis": {
    "functionalFit": {
      "score": 98.0,
      "confidence": 0.95,
      "evidence": "Industry-standard real-time event streaming pub-sub engine.",
      "contributingFactors": [
        "Streaming data ingestion",
        "Decoupling microservices"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "compatibility": {
      "score": 95.0,
      "confidence": 0.95,
      "evidence": "Highly compatible via Kafka Connect, though utilizes specialized binary protocol.",
      "contributingFactors": [
        "Kafka Connect ecosystem",
        "Binary TCP Protocol"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "performanceScalability": {
      "score": 100.0,
      "confidence": 0.95,
      "evidence": "Sub-10ms write latency and linear scalability across hundreds of broker partitions.",
      "contributingFactors": [
        "Million+ events/sec",
        "Zero-copy OS transfers"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "costEfficiency": {
      "score": 75.0,
      "confidence": 0.95,
      "evidence": "High storage and replication VM requirements, high networking egress.",
      "contributingFactors": [
        "Replication factor overhead",
        "Storage disk volumes"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "reliabilityResilience": {
      "score": 98.0,
      "confidence": 0.95,
      "evidence": "In-sync replicas (ISR) and KRaft metadata clustering prevent data loss.",
      "contributingFactors": [
        "ISR replication model",
        "Self-healing partition elections"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "operationalSimplicity": {
      "score": 60.0,
      "confidence": 0.95,
      "evidence": "Operationally complex broker JVM tuning, Zookeeper/KRaft state management.",
      "contributingFactors": [
        "JVM garbage collection lag",
        "State synchronization checks"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "futureReadiness": {
      "score": 95.0,
      "confidence": 0.95,
      "evidence": "Backbone for real-time architectures and streaming pipelines.",
      "contributingFactors": [
        "Real-time CDC adapters",
        "Schema Registry version tracing"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "ecosystemAdoption": {
      "score": 100.0,
      "confidence": 0.95,
      "evidence": "Adopted by over 80% of Fortune 100 enterprise stacks.",
      "contributingFactors": [
        "Global enterprise case studies",
        "Massive open community"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "risk": {
      "score": 90.0,
      "confidence": 0.95,
      "evidence": "Low lock-in since Apache protocol is open and supported by alternatives like Redpanda.",
      "contributingFactors": [
        "Open source core",
        "Interchangeable target connectors"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    }
  }
}
---

# Apache Kafka Technology Profile

![Apache Kafka Logo](https://raw.githubusercontent.com/devicons/devicon/master/icons/apachekafka/apachekafka-original.svg)

## Identity
- **Name**: Apache Kafka
- **Vendor**: Apache Software Foundation
- **Licensing**: Apache 2.0
- **Category & subcategory**: Streaming / Messaging

## Architecture pattern
- **Value**: Distributed Pub-Sub Append-Only Commit Log

## Internal microservice architecture
- Kafka Broker: Manages topics, partitions, and storage logs
- ZooKeeper/KRaft: Manages cluster metadata and leader elections

## Data flow
- **Value**: Producers send records to partitions -> Append-only write to disk -> Consumers pull logs from specific offsets

## Control plane / data plane
- **Value**: KRaft controller nodes manage metadata (control plane); Brokers manage partition logs and network IO (data plane)

## Runtime topology
- **Value**: Multi-broker cluster spanning multi-AZ, synchronized via KRaft

## Storage model
- **Value**: Direct append-only local files with OS page cache optimizations

## Compute model
- **Value**: Event-loop network handling, decoupled from storage commits

## Scaling behavior
- **Value**: Scale horizontally by adding brokers and reassigning partition slices

## HA & failover
- **Value**: In-Sync Replicas (ISR) model, automatic leader partition election

## Workload suitability
- **Value**: High-throughput stream processing, CDC, microservice decoupling

## Throughput
- **Value**: Millions of messages/sec

## Latency
- **Value**: Sub-10ms write-to-read

## Concurrency
- **Value**: Tens of thousands of active clients

## SLA/SLO
- **Value**: 99.999% stream availability

## MTTR / MTBF
- **Value**: MTTR < 2 min, MTBF > 25,000 hrs

## RPO / RTO
- **Value**: RPO = 0 (synced replication), RTO < 10s partition failover

## CPU / Memory / Storage utilization
- **Value**: High Network IO utilization, heavy RAM page cache usage, linear storage growth

## Network characteristics
- **Value**: TCP-based binary protocol, TLS 1.3, cross-AZ traffic overhead

## Cost drivers
- Retention period size
- Cross-AZ replication volume
- Broker VM count

## Dynamic pricing inputs
- Egress data (GB)
- Compute instance types
- Storage volumes (GB)

## Integration interfaces
- Kafka Client API
- REST Proxy
- Kafka Connect
- gRPC wrappers

## Supported formats
- Avro
- JSON
- Protobuf
- Binary
- CSV

## Native connectors
- JDBC Source/Sink
- Debezium Connectors
- S3 Sink
- Elasticsearch Sink

## Open standards
- CloudEvents
- OpenTelemetry
- JMX metrics

## Ecosystem maturity
- **Value**: Industry standard event streaming backbone

## Security capabilities
- SASL/SCRAM
- SASL/GSSAPI (Kerberos)
- mTLS
- ACL authorization

## Governance capabilities
- **Value**: Schema Registry integration and ACL access auditing

## AI readiness
- **Value**: Kafka Streams binding for live vector indexing pipelines

## Vendor lock-in
- **Value**: Very Low (Open-source standard, drop-in replacements like Redpanda exist)

## Migration difficulty
- **Value**: Medium (Requires partition mirror-maker setups)

## Benchmarks
- 1 GB/sec throughput validation (Confluent Benchmarks)

## Known bottlenecks
- Partition rebalancing locks consumer groups
- JVM Garbage Collection pauses

## Anti-patterns
- Using Kafka as a permanent relational database with query lookups
- Large payload messages (>10MB)

## Recommended combinations
- Kafka + Flink + ClickHouse
- Debezium + Kafka + Snowflake

## Unsupported combinations
- Direct synchronous HTTP client callbacks from Kafka Broker

## Operational runbooks
- Partition Reassignment Runbook
- KRaft Metadata Recovery Guide

## Failure scenarios
- Broker OOM under consumer lag
- Zookeeper network partition split-brain

## Best practices
- Keep message size below 1MB
- Set replication factor to 3 in production

## Decision rules
- If stream processing required with latency < 50ms: Use Kafka
- If simple pub-sub with low volume: Use RabbitMQ

## Decision Engine KPIs
### Functional Fit
- **Score**: 98.0 / 100
- **Confidence**: 95%
- **Evidence**: Industry-standard real-time event streaming pub-sub engine.
- **Contributing Factors**: Streaming data ingestion, Decoupling microservices

### Compatibility
- **Score**: 95.0 / 100
- **Confidence**: 95%
- **Evidence**: Highly compatible via Kafka Connect, though utilizes specialized binary protocol.
- **Contributing Factors**: Kafka Connect ecosystem, Binary TCP Protocol

### Performance Scalability
- **Score**: 100.0 / 100
- **Confidence**: 95%
- **Evidence**: Sub-10ms write latency and linear scalability across hundreds of broker partitions.
- **Contributing Factors**: Million+ events/sec, Zero-copy OS transfers

### Cost Efficiency
- **Score**: 75.0 / 100
- **Confidence**: 95%
- **Evidence**: High storage and replication VM requirements, high networking egress.
- **Contributing Factors**: Replication factor overhead, Storage disk volumes

### Reliability Resilience
- **Score**: 98.0 / 100
- **Confidence**: 95%
- **Evidence**: In-sync replicas (ISR) and KRaft metadata clustering prevent data loss.
- **Contributing Factors**: ISR replication model, Self-healing partition elections

### Operational Simplicity
- **Score**: 60.0 / 100
- **Confidence**: 95%
- **Evidence**: Operationally complex broker JVM tuning, Zookeeper/KRaft state management.
- **Contributing Factors**: JVM garbage collection lag, State synchronization checks

### Future Readiness
- **Score**: 95.0 / 100
- **Confidence**: 95%
- **Evidence**: Backbone for real-time architectures and streaming pipelines.
- **Contributing Factors**: Real-time CDC adapters, Schema Registry version tracing

### Ecosystem Adoption
- **Score**: 100.0 / 100
- **Confidence**: 95%
- **Evidence**: Adopted by over 80% of Fortune 100 enterprise stacks.
- **Contributing Factors**: Global enterprise case studies, Massive open community

### Risk
- **Score**: 90.0 / 100
- **Confidence**: 95%
- **Evidence**: Low lock-in since Apache protocol is open and supported by alternatives like Redpanda.
- **Contributing Factors**: Open source core, Interchangeable target connectors
