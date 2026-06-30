---
{
  "identity": {
    "name": "Milvus",
    "vendor": "LF AI & Data Foundation",
    "licensing": "Apache 2.0",
    "categorySubcategory": "Databases / Databases",
    "architecturePattern": "Decoupled Storage and Compute Vector Database Style",
    "internalMicroserviceArchitecture": [
      "Proxy: Entry endpoint for load-balancing and routing",
      "Coordinator Node: Resource scheduler and catalog metadata mapping",
      "Query Node: Memory vectorized search processor",
      "Data Node: Segment compaction and persistence"
    ],
    "dataFlow": "Proxy receives vectors -> Writes to log broker (Pulsar/Kafka) -> Query nodes load segment indexes in memory -> Search executions run",
    "controlPlaneDataPlane": "Coordinator cluster manages catalog schemas and scheduling (control plane); Query nodes execute search calculations (data plane)",
    "runtimeTopology": "Distributed microservices deployed on Kubernetes, decoupled storage nodes",
    "storageModel": "Log files on object storage (S3/MinIO), vector indexes (HNSW/IVF) loaded into local RAM/SSD caches",
    "computeModel": "Decoupled vectorized math calculation nodes utilizing CPU SIMD (AVX512) and GPUs",
    "scalingBehavior": "Independent horizontal scaling of Query nodes (for search) and Data nodes (for ingest)",
    "haFailover": "Auto-recovery of query pods via coordinator scheduling, replica query groupings",
    "workloadSuitability": "Semantic vector search, high-volume image embedding matching, LLM RAG pipelines",
    "throughput": "Tens of thousands of vector queries per second (QPS)",
    "latency": "Sub-10ms similarity search results",
    "concurrency": "Thousands of concurrent vector query streams",
    "slaSlo": "99.9% search availability SLO",
    "mttrMtbf": "MTTR < 5 min (worker pod recycling), MTBF > 12,000 hrs",
    "rpoRto": "RPO = 2s message broker queue, RTO < 30s Query node promotion",
    "utilization": "Extreme RAM footprint for HNSW indexes, high CPU/GPU SIMD computational usage during query phases",
    "networkCharacteristics": "gRPC / Protobuf communication, heavy payload throughput under large vector insertions",
    "costDrivers": [
      "Query node memory capacity requirements",
      "GPU runtime credits",
      "Message broker sizing"
    ],
    "dynamicPricingInputs": [
      "Vector dimension size and count",
      "Query nodes RAM sizing"
    ],
    "integrationInterfaces": [
      "gRPC API",
      "Python SDK (pymilvus)",
      "Java/Go SDKs",
      "REST API Proxy"
    ],
    "supportedFormats": [
      "Vectors (Floating point, Binary)",
      "Scalar payloads (JSON, INT, VARCHAR)"
    ],
    "nativeConnectors": [
      "LangChain VectorStore integration",
      "LlamaIndex Integration",
      "Kafka Connect sink"
    ],
    "openStandards": [
      "gRPC",
      "Protobuf standard specifications"
    ],
    "ecosystemMaturity": "Leading enterprise-scale open-source vector database",
    "securityCapabilities": [
      "RBAC user management",
      "TLS transport encryption",
      "API Key authorization"
    ],
    "governanceCapabilities": "Metadata catalog collections tracing and segment isolation policies",
    "aiReadiness": "Native vector database built specifically for RAG and LLM embedding pipelines",
    "vendorLockIn": "Low (Open-source vector database, database schemas export to Qdrant or Pinecone format)",
    "migrationDifficulty": "Medium (Requires rebuilding index files on the new vector target)",
    "benchmarks": [
      "1 million vectors benchmark search under 5ms"
    ],
    "knownBottlenecks": [
      "Query node out-of-memory crashes when HNSW index sizes exceed available RAM",
      "Index compilation build queue delays"
    ],
    "antiPatterns": [
      "Using Milvus as a standard transactional RDBMS database for scalar operations only",
      "High-frequency single vector row-by-row updates"
    ],
    "recommendedCombinations": [
      "Milvus + LangChain + vLLM",
      "Kafka + Milvus (real-time embedding ingestion)"
    ],
    "unsupportedCombinations": [
      "Hosting complex transactional SQL queries with multiple relationships"
    ],
    "operationalRunbooks": [
      "Vector Index Tuning Runbook",
      "Query Node OOM Troubleshooting Guide"
    ],
    "failureScenarios": [
      "Broker topic lag blocking vector writes",
      "Query node RAM exhaustion during index loading"
    ],
    "bestPractices": [
      "Pre-build index partitions to restrict search space sizing",
      "Ensure AVX512 SIMD vector instructions are active in VM CPU capabilities"
    ],
    "decisionRules": [
      "If vector size > 50 million embeddings: Choose Milvus",
      "If simple app RAG < 1 million embeddings: Choose pgvector"
    ]
  },
  "decisionEngineKpis": {
    "functionalFit": {
      "score": 98.0,
      "confidence": 0.95,
      "evidence": "Superb vector database built for massive similarity searches.",
      "contributingFactors": [
        "Semantic vector matching",
        "LLM RAG embeddings"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "compatibility": {
      "score": 92.0,
      "confidence": 0.95,
      "evidence": "Integrates well with AI pipelines via gRPC API, but lacks relational interfaces.",
      "contributingFactors": [
        "gRPC API channels",
        "Langchain connector"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "performanceScalability": {
      "score": 96.0,
      "confidence": 0.95,
      "evidence": "Extreme search performance on AVX-512 CPU hardware configurations.",
      "contributingFactors": [
        "AVX-512 SIMD processing",
        "IVF/HNSW indices"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "costEfficiency": {
      "score": 75.0,
      "confidence": 0.95,
      "evidence": "High RAM footprint requirements for vector indices, requires GPU nodes.",
      "contributingFactors": [
        "RAM caching gigabytes",
        "GPU instance rates"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "reliabilityResilience": {
      "score": 90.0,
      "confidence": 0.95,
      "evidence": "Auto-recovery of query pods via coordinator scheduling on Kubernetes.",
      "contributingFactors": [
        "Active replicas pool",
        "Kubernetes pod rescheduling"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "operationalSimplicity": {
      "score": 70.0,
      "confidence": 0.95,
      "evidence": "Decoupled microservice architecture has high deployment complexity.",
      "contributingFactors": [
        "Multiple component nodes",
        "Kubernetes configurations"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "futureReadiness": {
      "score": 98.0,
      "confidence": 0.95,
      "evidence": "Native vector design, heavily utilized in AI and GenAI architectures.",
      "contributingFactors": [
        "Vector embedding storage",
        "RAG model caching"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "ecosystemAdoption": {
      "score": 92.0,
      "confidence": 0.95,
      "evidence": "Fast growing open-source vector store for enterprise applications.",
      "contributingFactors": [
        "LF AI foundation backing",
        "High Github star metrics"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "risk": {
      "score": 90.0,
      "confidence": 0.95,
      "evidence": "LOWER risk, though indexes must be rebuilt if migrating engines.",
      "contributingFactors": [
        "Apache 2.0 open-source",
        "Index rebuild requirements"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    }
  }
}
---

# Milvus Technology Profile

![Milvus Logo](https://raw.githubusercontent.com/devicons/devicon/master/icons/milvus/milvus-original.svg)

## Identity
- **Name**: Milvus
- **Vendor**: LF AI & Data Foundation
- **Licensing**: Apache 2.0
- **Category & subcategory**: Databases / Databases

## Architecture pattern
- **Value**: Decoupled Storage and Compute Vector Database Style

## Internal microservice architecture
- Proxy: Entry endpoint for load-balancing and routing
- Coordinator Node: Resource scheduler and catalog metadata mapping
- Query Node: Memory vectorized search processor
- Data Node: Segment compaction and persistence

## Data flow
- **Value**: Proxy receives vectors -> Writes to log broker (Pulsar/Kafka) -> Query nodes load segment indexes in memory -> Search executions run

## Control plane / data plane
- **Value**: Coordinator cluster manages catalog schemas and scheduling (control plane); Query nodes execute search calculations (data plane)

## Runtime topology
- **Value**: Distributed microservices deployed on Kubernetes, decoupled storage nodes

## Storage model
- **Value**: Log files on object storage (S3/MinIO), vector indexes (HNSW/IVF) loaded into local RAM/SSD caches

## Compute model
- **Value**: Decoupled vectorized math calculation nodes utilizing CPU SIMD (AVX512) and GPUs

## Scaling behavior
- **Value**: Independent horizontal scaling of Query nodes (for search) and Data nodes (for ingest)

## HA & failover
- **Value**: Auto-recovery of query pods via coordinator scheduling, replica query groupings

## Workload suitability
- **Value**: Semantic vector search, high-volume image embedding matching, LLM RAG pipelines

## Throughput
- **Value**: Tens of thousands of vector queries per second (QPS)

## Latency
- **Value**: Sub-10ms similarity search results

## Concurrency
- **Value**: Thousands of concurrent vector query streams

## SLA/SLO
- **Value**: 99.9% search availability SLO

## MTTR / MTBF
- **Value**: MTTR < 5 min (worker pod recycling), MTBF > 12,000 hrs

## RPO / RTO
- **Value**: RPO = 2s message broker queue, RTO < 30s Query node promotion

## CPU / Memory / Storage utilization
- **Value**: Extreme RAM footprint for HNSW indexes, high CPU/GPU SIMD computational usage during query phases

## Network characteristics
- **Value**: gRPC / Protobuf communication, heavy payload throughput under large vector insertions

## Cost drivers
- Query node memory capacity requirements
- GPU runtime credits
- Message broker sizing

## Dynamic pricing inputs
- Vector dimension size and count
- Query nodes RAM sizing

## Integration interfaces
- gRPC API
- Python SDK (pymilvus)
- Java/Go SDKs
- REST API Proxy

## Supported formats
- Vectors (Floating point, Binary)
- Scalar payloads (JSON, INT, VARCHAR)

## Native connectors
- LangChain VectorStore integration
- LlamaIndex Integration
- Kafka Connect sink

## Open standards
- gRPC
- Protobuf standard specifications

## Ecosystem maturity
- **Value**: Leading enterprise-scale open-source vector database

## Security capabilities
- RBAC user management
- TLS transport encryption
- API Key authorization

## Governance capabilities
- **Value**: Metadata catalog collections tracing and segment isolation policies

## AI readiness
- **Value**: Native vector database built specifically for RAG and LLM embedding pipelines

## Vendor lock-in
- **Value**: Low (Open-source vector database, database schemas export to Qdrant or Pinecone format)

## Migration difficulty
- **Value**: Medium (Requires rebuilding index files on the new vector target)

## Benchmarks
- 1 million vectors benchmark search under 5ms

## Known bottlenecks
- Query node out-of-memory crashes when HNSW index sizes exceed available RAM
- Index compilation build queue delays

## Anti-patterns
- Using Milvus as a standard transactional RDBMS database for scalar operations only
- High-frequency single vector row-by-row updates

## Recommended combinations
- Milvus + LangChain + vLLM
- Kafka + Milvus (real-time embedding ingestion)

## Unsupported combinations
- Hosting complex transactional SQL queries with multiple relationships

## Operational runbooks
- Vector Index Tuning Runbook
- Query Node OOM Troubleshooting Guide

## Failure scenarios
- Broker topic lag blocking vector writes
- Query node RAM exhaustion during index loading

## Best practices
- Pre-build index partitions to restrict search space sizing
- Ensure AVX512 SIMD vector instructions are active in VM CPU capabilities

## Decision rules
- If vector size > 50 million embeddings: Choose Milvus
- If simple app RAG < 1 million embeddings: Choose pgvector

## Decision Engine KPIs
### Functional Fit
- **Score**: 98.0 / 100
- **Confidence**: 95%
- **Evidence**: Superb vector database built for massive similarity searches.
- **Contributing Factors**: Semantic vector matching, LLM RAG embeddings

### Compatibility
- **Score**: 92.0 / 100
- **Confidence**: 95%
- **Evidence**: Integrates well with AI pipelines via gRPC API, but lacks relational interfaces.
- **Contributing Factors**: gRPC API channels, Langchain connector

### Performance Scalability
- **Score**: 96.0 / 100
- **Confidence**: 95%
- **Evidence**: Extreme search performance on AVX-512 CPU hardware configurations.
- **Contributing Factors**: AVX-512 SIMD processing, IVF/HNSW indices

### Cost Efficiency
- **Score**: 75.0 / 100
- **Confidence**: 95%
- **Evidence**: High RAM footprint requirements for vector indices, requires GPU nodes.
- **Contributing Factors**: RAM caching gigabytes, GPU instance rates

### Reliability Resilience
- **Score**: 90.0 / 100
- **Confidence**: 95%
- **Evidence**: Auto-recovery of query pods via coordinator scheduling on Kubernetes.
- **Contributing Factors**: Active replicas pool, Kubernetes pod rescheduling

### Operational Simplicity
- **Score**: 70.0 / 100
- **Confidence**: 95%
- **Evidence**: Decoupled microservice architecture has high deployment complexity.
- **Contributing Factors**: Multiple component nodes, Kubernetes configurations

### Future Readiness
- **Score**: 98.0 / 100
- **Confidence**: 95%
- **Evidence**: Native vector design, heavily utilized in AI and GenAI architectures.
- **Contributing Factors**: Vector embedding storage, RAG model caching

### Ecosystem Adoption
- **Score**: 92.0 / 100
- **Confidence**: 95%
- **Evidence**: Fast growing open-source vector store for enterprise applications.
- **Contributing Factors**: LF AI foundation backing, High Github star metrics

### Risk
- **Score**: 90.0 / 100
- **Confidence**: 95%
- **Evidence**: LOWER risk, though indexes must be rebuilt if migrating engines.
- **Contributing Factors**: Apache 2.0 open-source, Index rebuild requirements
