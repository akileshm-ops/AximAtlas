# IoT and Time-Series Monitoring (MQTT + Kafka + TimescaleDB + Grafana) Stack Profile

## Architecture
Edge sensors push telemetry via MQTT broker. A connector streams MQTT logs into Apache Kafka topics. Kafka streams data into TimescaleDB relational database. Grafana reads hyper-tables for live dashboarding.

---

## Data Flow
IoT Sensors -> MQTT -> Kafka -> TimescaleDB -> Grafana.

---

## Evaluation Metric Grid
- **Operational Complexity**: Medium
- **Scalability**: High
- **Latency**: Low-millisecond
- **Cost**: Moderate (database storage cost scales with retention)
- **Compatibility Score**: 9.6 / 10
- **Overall Stack Score**: 9.1 / 10
- **Risk Score**: 2.5 / 10

---

## Strengths
* Extreme high write throughput support
* Structured relational queries on time-series records
* Out-of-the-box alerts and telemetry plotting

## Weaknesses
* Requires connection tunings for thousands of active MQTT nodes
* Database index sizes grow rapidly

---

## Operational Details
- **Failure Points**:
  * MQTT broker connection dropouts
  * Kafka replication delay under sudden device telemetry spikes
- **Suitability**: Industrial manufacturing telemetry, server health tracking, smart-home logs
- **Recommended Scale**: Millions of device data points per hour
- **Estimated Monthly Cost**: $1,500 - $8,000
- **Estimated TCO**: Medium

---

## Alternatives
* Kafka + InfluxDB + Grafana
* AWS IoT Core + Timestream

---

## Migration Paths
* Move from TimescaleDB to ClickHouse if time-series analytical query complexity exceeds transactional requirements
