# Real-time Lakehouse (Kafka + Flink + Iceberg) Stack Profile

## Architecture
Event producers stream data into Kafka partitions. Apache Flink consumes stream, executes real-time aggregations/cleansing, and writes directly into Apache Iceberg table format on object storage.

---

## Data Flow
Ingest (Kafka) -> Process & Align (Flink) -> Commit to Open Lakehouse format (Iceberg/S3).

---

## Evaluation Metric Grid
- **Operational Complexity**: High
- **Scalability**: Exceptional
- **Latency**: Sub-second
- **Cost**: Moderate (optimized storage, but continuous compute billing)
- **Compatibility Score**: 9.2 / 10
- **Overall Stack Score**: 8.9 / 10
- **Risk Score**: 4.5 / 10

---

## Strengths
* Near-zero latency analytical updates
* Acid compliance on data lake storage
* No vendor lock-in

## Weaknesses
* Extremely high operational complexity
* Partition schema evolutions require Flink job restarts

---

## Operational Details
- **Failure Points**:
  * Flink coordinator checkpoint failures
  * Iceberg commit conflict lockups
- **Suitability**: Real-time telemetry, live fraud detection, operational monitoring
- **Recommended Scale**: Petabytes of stream logs, >100,000 events/second
- **Estimated Monthly Cost**: $5,000 - $25,000
- **Estimated TCO**: High (due to engineering team support costs)

---

## Alternatives
* Kafka + ClickHouse
* Snowpipe Streaming

---

## Migration Paths
* Can transition storage layer from Iceberg to Delta Lake using catalog synchronization
