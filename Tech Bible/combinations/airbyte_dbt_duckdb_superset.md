# Open Source MDS (Airbyte + dbt + DuckDB + Superset) Stack Profile

## Architecture
Airbyte Open Source loads data to local files or PostgreSQL. dbt Core compiles SQL transformations and executes them inside a local DuckDB engine, exporting Parquet files. Apache Superset reads DuckDB datasets for visualization.

---

## Data Flow
APIs -> Airbyte OSS -> Local Storage -> DuckDB transformations via dbt -> Superset Dashboards.

---

## Evaluation Metric Grid
- **Operational Complexity**: Low
- **Scalability**: Low to Moderate
- **Latency**: Minutes
- **Cost**: Very Low (Infrastructure VM cost only)
- **Compatibility Score**: 9.4 / 10
- **Overall Stack Score**: 8.7 / 10
- **Risk Score**: 1.5 / 10

---

## Strengths
* Zero licensing cost
* Extremely fast local execution via DuckDB
* Runs entirely inside a single machine or VM

## Weaknesses
* Not native multi-user write architecture
* Disk space constraints on single-node deployments

---

## Operational Details
- **Failure Points**:
  * DuckDB single-writer file locks when transformations run concurrently with user queries
  * Single VM disk capacity saturation
- **Suitability**: Startup databases, localized team analytics, low-budget BI setups
- **Recommended Scale**: Gigabytes to low Terabytes (<500GB ideal)
- **Estimated Monthly Cost**: $100 - $500
- **Estimated TCO**: Low

---

## Alternatives
* Meltano + dbt + MotherDuck + Lightdash

---

## Migration Paths
* Migrate DuckDB files to Snowflake/BigQuery as data size grows; deploy Superset on Kubernetes for enterprise scaling
