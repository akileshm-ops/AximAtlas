# Modern Data Stack (Airbyte + dbt + Snowflake) Stack Profile

## Architecture
Airbyte extracts data from SaaS APIs / OLTP databases, loads raw data into Snowflake. dbt Core runs SQL transformation models on a schedule natively in Snowflake warehouses.

---

## Data Flow
Extract & Load (Airbyte) -> Warehouse Storage (Snowflake) -> Transform & Clean (dbt).

---

## Evaluation Metric Grid
- **Operational Complexity**: Low to Medium
- **Scalability**: High
- **Latency**: Minutes to hours
- **Cost**: High (SaaS billing models for Snowflake compute and Airbyte rows)
- **Compatibility Score**: 9.8 / 10
- **Overall Stack Score**: 9.2 / 10
- **Risk Score**: 2.0 / 10

---

## Strengths
* Highly decoupled components
* SQL-centric developer profile
* Minimal maintenance overhead

## Weaknesses
* Warehouse costs scale quickly with complex dbt models
* Batch-only integrations (usually hourly or daily)

---

## Operational Details
- **Failure Points**:
  * SaaS API schema drift breaking Airbyte connectors
  * dbt model lockups during parallel runs
- **Suitability**: Enterprise BI, executive dashboards, marketing analytics, financial reconciliation
- **Recommended Scale**: Terabytes of mixed database and application logs
- **Estimated Monthly Cost**: $2,000 - $12,000
- **Estimated TCO**: Medium (low engineering resource requirements)

---

## Alternatives
* Fivetran + dbt + BigQuery
* Meltano + dbt + ClickHouse

---

## Migration Paths
* Replace Airbyte with Fivetran for production scale; migrate Snowflake to BigQuery if in GCP ecosystem
