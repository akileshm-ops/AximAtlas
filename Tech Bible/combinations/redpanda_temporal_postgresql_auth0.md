# Event-Driven Microservices Workflow Stack Stack Profile

## Architecture
Redpanda processes events between microservices. Temporal orchestrates long-running, stateful workflows, writing tracking data into PostgreSQL. Auth0 manages microservice JWT security tokens.

---

## Data Flow
API event -> Redpanda event queue -> Temporal starts workflow run -> Postgres registers stage -> Auth0 verifies service authorization.

---

## Evaluation Metric Grid
- **Operational Complexity**: Medium to High
- **Scalability**: High
- **Latency**: Low-millisecond messaging, low-second workflow stages
- **Cost**: Moderate to High
- **Compatibility Score**: 9.4 / 10
- **Overall Stack Score**: 9.0 / 10
- **Risk Score**: 2.5 / 10

---

## Strengths
* Durable workflow execution with automated retries
* Extremely low-latency messaging via Redpanda C++ broker
* No identity infrastructure to maintain

## Weaknesses
* Temporal workflow design requires specialized developer knowledge
* Auth0 enterprise pricing scales rapidly with active user counts

---

## Operational Details
- **Failure Points**:
  * PostgreSQL database backend saturation under high workflow state updates
  * Temporal history size limits exceeded in single workflow runs
- **Suitability**: E-commerce order fulfillment pipelines, automated user onboarding, financial transaction steps
- **Recommended Scale**: Thousands of workflow executions per minute, millions of events
- **Estimated Monthly Cost**: $3,000 - $18,000
- **Estimated TCO**: Medium

---

## Alternatives
* Kafka + Airflow + MySQL + Keycloak

---

## Migration Paths
* Redpanda can be swapped for managed Kafka; Temporal workflows can be exported to AWS Step Functions
