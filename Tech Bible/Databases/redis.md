---
{
  "identity": {
    "name": "Redis",
    "vendor": "Redis Ltd.",
    "licensing": "RSALv2 / SSPLv1",
    "categorySubcategory": "Databases / Databases",
    "architecturePattern": "In-Memory Single-Threaded Key-Value Data Store",
    "internalMicroserviceArchitecture": [
      "Redis Server: Single-threaded event-loop engine",
      "Sentinel: Cluster manager and monitor node",
      "Cluster Node: Multi-master shards"
    ],
    "dataFlow": "Client writes key-value -> Single-threaded CPU process writes to RAM memory -> Async write to AOF/RDB log file",
    "controlPlaneDataPlane": "Redis Sentinel monitors and promotes nodes (control plane); Redis Server executes operations on memory (data plane)",
    "runtimeTopology": "Master-replica replication groups, Sentinel clusters, or Redis Cluster partition shards",
    "storageModel": "Pure in-memory RAM storage, optional Append-Only File (AOF) / Redis Database (RDB) persistent snapshots on disk",
    "computeModel": "Single-threaded event loop driven by multiplexing sockets (epoll)",
    "scalingBehavior": "Scale up by increasing RAM capacity, scale out via cluster sharding keys",
    "haFailover": "Sentinel monitors master, promoting replica automatically under 15s",
    "workloadSuitability": "Low-latency session caching, rate limiting, pub-sub messaging, leaderboards",
    "throughput": "Hundreds of thousands of read/write operations per second per node",
    "latency": "Sub-millisecond response times (<1ms)",
    "concurrency": "Up to 10,000 active concurrent connections",
    "slaSlo": "99.999% cache availability SLO",
    "mttrMtbf": "MTTR < 15s (automatic failover), MTBF > 50,000 hrs",
    "rpoRto": "RPO = 1s (AOF set to everysec), RTO < 15s Sentinel failover",
    "utilization": "Extremely high RAM consumption per GB stored, single core CPU saturation",
    "networkCharacteristics": "TCP-based RESP protocol, TLS 1.3 payload encryption",
    "costDrivers": [
      "RAM capacity GB size",
      "Cluster shard node count",
      "Persistent disk storage sizing"
    ],
    "dynamicPricingInputs": [
      "RAM gigabytes active",
      "Managed service instance sizes"
    ],
    "integrationInterfaces": [
      "RESP API protocol",
      "Redis CLI",
      "Client bindings (Jedis, redis-py, etc.)"
    ],
    "supportedFormats": [
      "Binary payloads",
      "Redis data structures (Hashes, Lists, Sets, Sorted Sets, Streams)"
    ],
    "nativeConnectors": [
      "Redis Streams Connector",
      "Spring Data Redis",
      "Celery Broker adapter"
    ],
    "openStandards": [
      "RESP binary protocol format"
    ],
    "ecosystemMaturity": "Undisputed standard for high-performance in-memory caching",
    "securityCapabilities": [
      "ACL user controls",
      "Mutual TLS (mTLS)",
      "Redis Password protection"
    ],
    "governanceCapabilities": "Key expiry auditing and command execution tracking",
    "aiReadiness": "RedisVL vector search library, memory cache for LLM prompt histories",
    "vendorLockIn": "Low (Open-source replacements like Valkey/KeyDB exist)",
    "migrationDifficulty": "Low (Stateless caches require zero migration; stateful caches migrate via RDB imports)",
    "benchmarks": [
      "YCSB performance validation exceeding 200k ops/sec at 1ms latency"
    ],
    "knownBottlenecks": [
      "Single-threaded thread blocks under heavy commands (e.g. KEYS *)",
      "Fork OOM during background RDB disk writes"
    ],
    "antiPatterns": [
      "Storing petabytes of permanent relational databases without cache invalidation rules",
      "Large objects (>512MB) per single key"
    ],
    "recommendedCombinations": [
      "PostgreSQL + Redis (cache-aside)",
      "Spring Boot + Redis + MySQL"
    ],
    "unsupportedCombinations": [
      "Executing complex analytical SQL joins over gigabytes of raw data"
    ],
    "operationalRunbooks": [
      "Redis Memory Defragmentation Manual",
      "Cluster Node Replacement Guide"
    ],
    "failureScenarios": [
      "Master OOM crash under memory leak",
      "Sentinel split-brain failover during network partition"
    ],
    "bestPractices": [
      "Always configure maxmemory-policy eviction rules",
      "Never run KEYS command in production (use SCAN)"
    ],
    "decisionRules": [
      "If cache latency must be < 2ms: Choose Redis",
      "If database caching with structured queries is required: Choose PostgreSQL with local indexes"
    ]
  },
  "decisionEngineKpis": {
    "functionalFit": {
      "score": 98.0,
      "confidence": 0.95,
      "evidence": "Superb in-memory cache, session store, and transient publisher.",
      "contributingFactors": [
        "Caching key/value pairs",
        "Rate limiting counters"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "compatibility": {
      "score": 95.0,
      "confidence": 0.95,
      "evidence": "RESP protocol has client libraries in all major developer runtimes.",
      "contributingFactors": [
        "RESP binary sockets",
        "Client library wrappers"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "performanceScalability": {
      "score": 100.0,
      "confidence": 0.95,
      "evidence": "Sub-millisecond latency caching, hundreds of thousands of operations/sec.",
      "contributingFactors": [
        "Epoll socket loop",
        "Pure RAM data storage"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "costEfficiency": {
      "score": 75.0,
      "confidence": 0.95,
      "evidence": "High RAM utilization means expensive VM infrastructure costs.",
      "contributingFactors": [
        "RAM storage gigabytes",
        "Replication cluster instances"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "reliabilityResilience": {
      "score": 96.0,
      "confidence": 0.95,
      "evidence": "Redis Sentinel promotes standbys under 15 seconds.",
      "contributingFactors": [
        "Redis Sentinel elections",
        "AOF persistence logs"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "operationalSimplicity": {
      "score": 90.0,
      "confidence": 0.95,
      "evidence": "Simple standalone setup, though clusters require active memory defragmentation.",
      "contributingFactors": [
        "Memory limits eviction",
        "Defragmentation tuning"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "futureReadiness": {
      "score": 90.0,
      "confidence": 0.95,
      "evidence": "RedisVL and RedisAI support fast vector searches and LLM caches.",
      "contributingFactors": [
        "RedisVL embedding search",
        "Prompt memory caches"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "ecosystemAdoption": {
      "score": 100.0,
      "confidence": 0.95,
      "evidence": "Ubiquitous caching layer across all modern web backends.",
      "contributingFactors": [
        "Global caching standard",
        "Docker Hub top downloads"
      ],
      "penalties": [],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    },
    "risk": {
      "score": 80.0,
      "confidence": 0.95,
      "evidence": "LOWER risk, though licensing has changed; Valkey provides open-source alternative.",
      "contributingFactors": [
        "RSALv2 licensing rules",
        "Valkey migration pathways"
      ],
      "penalties": [
        {
          "factor": "Licensing change",
          "deduction": -5
        }
      ],
      "bonuses": [],
      "source": "Antigravity Evaluation Grid / Official Vendor Docs",
      "lastVerified": "2026-06-28"
    }
  }
}
---

# Redis Technology Profile

![Redis Logo](https://raw.githubusercontent.com/devicons/devicon/master/icons/redis/redis-original.svg)

## Identity
- **Name**: Redis
- **Vendor**: Redis Ltd.
- **Licensing**: RSALv2 / SSPLv1
- **Category & subcategory**: Databases / Databases

## Architecture pattern
- **Value**: In-Memory Single-Threaded Key-Value Data Store

## Internal microservice architecture
- Redis Server: Single-threaded event-loop engine
- Sentinel: Cluster manager and monitor node
- Cluster Node: Multi-master shards

## Data flow
- **Value**: Client writes key-value -> Single-threaded CPU process writes to RAM memory -> Async write to AOF/RDB log file

## Control plane / data plane
- **Value**: Redis Sentinel monitors and promotes nodes (control plane); Redis Server executes operations on memory (data plane)

## Runtime topology
- **Value**: Master-replica replication groups, Sentinel clusters, or Redis Cluster partition shards

## Storage model
- **Value**: Pure in-memory RAM storage, optional Append-Only File (AOF) / Redis Database (RDB) persistent snapshots on disk

## Compute model
- **Value**: Single-threaded event loop driven by multiplexing sockets (epoll)

## Scaling behavior
- **Value**: Scale up by increasing RAM capacity, scale out via cluster sharding keys

## HA & failover
- **Value**: Sentinel monitors master, promoting replica automatically under 15s

## Workload suitability
- **Value**: Low-latency session caching, rate limiting, pub-sub messaging, leaderboards

## Throughput
- **Value**: Hundreds of thousands of read/write operations per second per node

## Latency
- **Value**: Sub-millisecond response times (<1ms)

## Concurrency
- **Value**: Up to 10,000 active concurrent connections

## SLA/SLO
- **Value**: 99.999% cache availability SLO

## MTTR / MTBF
- **Value**: MTTR < 15s (automatic failover), MTBF > 50,000 hrs

## RPO / RTO
- **Value**: RPO = 1s (AOF set to everysec), RTO < 15s Sentinel failover

## CPU / Memory / Storage utilization
- **Value**: Extremely high RAM consumption per GB stored, single core CPU saturation

## Network characteristics
- **Value**: TCP-based RESP protocol, TLS 1.3 payload encryption

## Cost drivers
- RAM capacity GB size
- Cluster shard node count
- Persistent disk storage sizing

## Dynamic pricing inputs
- RAM gigabytes active
- Managed service instance sizes

## Integration interfaces
- RESP API protocol
- Redis CLI
- Client bindings (Jedis, redis-py, etc.)

## Supported formats
- Binary payloads
- Redis data structures (Hashes, Lists, Sets, Sorted Sets, Streams)

## Native connectors
- Redis Streams Connector
- Spring Data Redis
- Celery Broker adapter

## Open standards
- RESP binary protocol format

## Ecosystem maturity
- **Value**: Undisputed standard for high-performance in-memory caching

## Security capabilities
- ACL user controls
- Mutual TLS (mTLS)
- Redis Password protection

## Governance capabilities
- **Value**: Key expiry auditing and command execution tracking

## AI readiness
- **Value**: RedisVL vector search library, memory cache for LLM prompt histories

## Vendor lock-in
- **Value**: Low (Open-source replacements like Valkey/KeyDB exist)

## Migration difficulty
- **Value**: Low (Stateless caches require zero migration; stateful caches migrate via RDB imports)

## Benchmarks
- YCSB performance validation exceeding 200k ops/sec at 1ms latency

## Known bottlenecks
- Single-threaded thread blocks under heavy commands (e.g. KEYS *)
- Fork OOM during background RDB disk writes

## Anti-patterns
- Storing petabytes of permanent relational databases without cache invalidation rules
- Large objects (>512MB) per single key

## Recommended combinations
- PostgreSQL + Redis (cache-aside)
- Spring Boot + Redis + MySQL

## Unsupported combinations
- Executing complex analytical SQL joins over gigabytes of raw data

## Operational runbooks
- Redis Memory Defragmentation Manual
- Cluster Node Replacement Guide

## Failure scenarios
- Master OOM crash under memory leak
- Sentinel split-brain failover during network partition

## Best practices
- Always configure maxmemory-policy eviction rules
- Never run KEYS command in production (use SCAN)

## Decision rules
- If cache latency must be < 2ms: Choose Redis
- If database caching with structured queries is required: Choose PostgreSQL with local indexes

## Decision Engine KPIs
### Functional Fit
- **Score**: 98.0 / 100
- **Confidence**: 95%
- **Evidence**: Superb in-memory cache, session store, and transient publisher.
- **Contributing Factors**: Caching key/value pairs, Rate limiting counters

### Compatibility
- **Score**: 95.0 / 100
- **Confidence**: 95%
- **Evidence**: RESP protocol has client libraries in all major developer runtimes.
- **Contributing Factors**: RESP binary sockets, Client library wrappers

### Performance Scalability
- **Score**: 100.0 / 100
- **Confidence**: 95%
- **Evidence**: Sub-millisecond latency caching, hundreds of thousands of operations/sec.
- **Contributing Factors**: Epoll socket loop, Pure RAM data storage

### Cost Efficiency
- **Score**: 75.0 / 100
- **Confidence**: 95%
- **Evidence**: High RAM utilization means expensive VM infrastructure costs.
- **Contributing Factors**: RAM storage gigabytes, Replication cluster instances

### Reliability Resilience
- **Score**: 96.0 / 100
- **Confidence**: 95%
- **Evidence**: Redis Sentinel promotes standbys under 15 seconds.
- **Contributing Factors**: Redis Sentinel elections, AOF persistence logs

### Operational Simplicity
- **Score**: 90.0 / 100
- **Confidence**: 95%
- **Evidence**: Simple standalone setup, though clusters require active memory defragmentation.
- **Contributing Factors**: Memory limits eviction, Defragmentation tuning

### Future Readiness
- **Score**: 90.0 / 100
- **Confidence**: 95%
- **Evidence**: RedisVL and RedisAI support fast vector searches and LLM caches.
- **Contributing Factors**: RedisVL embedding search, Prompt memory caches

### Ecosystem Adoption
- **Score**: 100.0 / 100
- **Confidence**: 95%
- **Evidence**: Ubiquitous caching layer across all modern web backends.
- **Contributing Factors**: Global caching standard, Docker Hub top downloads

### Risk
- **Score**: 80.0 / 100
- **Confidence**: 95%
- **Evidence**: LOWER risk, though licensing has changed; Valkey provides open-source alternative.
- **Contributing Factors**: RSALv2 licensing rules, Valkey migration pathways
