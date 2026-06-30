# Enterprise Lakehouse (Spark + Iceberg + Unity Catalog + Databricks) Stack Profile

## Architecture
Apache Spark executes heavy batch ETL on AWS S3/Azure Blob. Databricks manages computation cluster infrastructure, with Unity Catalog governing metadata, and Iceberg storing files.

---

## Data Flow
Raw storage -> Spark cluster compute -> Table writes managed by Unity Catalog metadata -> Client query via Databricks SQL.

---

## Evaluation Metric Grid
- **Operational Complexity**: Medium
- **Scalability**: Exceptional
- **Latency**: Seconds to minutes
- **Cost**: High (Double billing: Cloud VMs + Databricks DBUs)
- **Compatibility Score**: 9.4 / 10
- **Overall Stack Score**: 9.0 / 10
- **Risk Score**: 3.0 / 10

---

## Strengths
* Unified governance for files and SQL tables
* Massive machine learning/analytics scalability
* Shared storage metadata across multiple tools

## Weaknesses
* Databricks proprietary pricing markup
* Unity Catalog locked to Databricks cluster dependencies (partially mitigated by open-source catalog)

---

## Operational Details
- **Failure Points**:
  * Unity Catalog metadata synchronization lag
  * Spark driver OOM during massive table compaction
- **Suitability**: Large-scale corporate data platforms, cross-functional data science, and unified analytical hubs
- **Recommended Scale**: Petabytes of data, hundreds of data developers
- **Estimated Monthly Cost**: $10,000 - $75,000
- **Estimated TCO**: High

---

## Alternatives
* Athena + Glue Catalog + Iceberg
* Snowflake Managed Iceberg

---

## Migration Paths
* Migrate Spark compute to EMR/Dataproc; switch catalog from Unity to Open Source Hive/Polaris Catalog
