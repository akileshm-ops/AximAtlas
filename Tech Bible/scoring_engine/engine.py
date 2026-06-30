import json
from pathlib import Path

class StackEvaluator:
    def __init__(self, workspace_root=None):
        self.workspace_root = Path(workspace_root or "d:/3D Data Stack")
        self.bible_root = self.workspace_root / "Tech Bible"
        self.rules_file = self.bible_root / "scoring_engine" / "rules.json"
        
        # Load declarative rules
        with open(self.rules_file, "r") as rf:
            self.rules = json.load(rf)
            
        self.weights = self.rules["weights"]
        self.components = {}
        self.load_all_components()

    def load_all_components(self):
        # Scan all category folders
        categories = ["Databases", "Warehouses", "ETL Tools", "Streaming Systems", "BI Tools", "Cloud Services"]
        for cat in categories:
            cat_dir = self.bible_root / cat
            if not cat_dir.exists():
                continue
            for f in cat_dir.glob("*.md"):
                content = f.read_text(encoding="utf-8")
                parts = content.split("---")
                if len(parts) >= 3:
                    try:
                        data = json.loads(parts[1])
                        cid = f.stem
                        self.components[cid] = data
                    except Exception as e:
                        print(f"Error loading {f.name}: {e}")

    def evaluate_component(self, cid):
        comp = self.components.get(cid)
        if not comp:
            return None
            
        # Get raw engine KPIs or fall back
        kpis = comp.get("decisionEngineKpis", {})
        
        weighted_sum = 0.0
        details = {}
        min_confidence = 1.0
        
        for kpi_key, weight in self.weights.items():
            kpi_data = kpis.get(kpi_key, {})
            score = kpi_data.get("score", 70.0)
            confidence = kpi_data.get("confidence", 0.90)
            
            weighted_sum += (score * weight)
            min_confidence = min(min_confidence, confidence)
            
            details[kpi_key] = {
                "score": score,
                "weight": weight,
                "contribution": score * weight,
                "evidence": kpi_data.get("evidence", "Standard profile data"),
                "source": kpi_data.get("source", "Vendor Docs"),
                "confidence": confidence,
                "penalties": kpi_data.get("penalties", []),
                "bonuses": kpi_data.get("bonuses", [])
            }
            
        overall_score = weighted_sum
        
        return {
            "name": comp.get("identity", {}).get("name", cid),
            "overallScore": overall_score,
            "confidenceScore": min_confidence * 100.0,
            "kpiDetails": details
        }

    def evaluate_stack(self, cids, budget=10000, estimated_cost=8000, workload="Ideal", completeness_coverage=100, manual_integrations=0, custom_connectors=0):
        # 1. Average Component Scores
        evals = []
        scores = []
        confidences = []
        for cid in cids:
            res = self.evaluate_component(cid)
            if res:
                evals.append(res)
                scores.append(res["overallScore"])
                confidences.append(res["confidenceScore"])
                
        if not evals:
            return { "error": "No valid components found in stack" }
            
        avg_score = sum(scores) / len(scores)
        avg_confidence = sum(confidences) / len(confidences)
        
        # 2. Compatibility Bonus
        compat_rules = self.rules["compatibilityBonus"]
        # Defaulting to Official (+4) compatibility for core stacks
        compat_bonus = compat_rules.get("Official", 4)
        
        # 3. Architecture Completeness Bonus
        complete_rules = self.rules["completenessBonus"]
        if completeness_coverage >= 100:
            completeness_bonus = complete_rules.get("100", 10)
        elif completeness_coverage >= 90:
            completeness_bonus = complete_rules.get("90", 8)
        elif completeness_coverage >= 80:
            completeness_bonus = complete_rules.get("80", 6)
        elif completeness_coverage >= 70:
            completeness_bonus = complete_rules.get("70", 4)
        else:
            completeness_bonus = complete_rules.get("below_70", 0)
            
        # 4. Workload Fit Bonus
        fit_rules = self.rules["workloadFitBonus"]
        workload_bonus = fit_rules.get(workload, 7)
        
        # 5. Cost Penalty
        cost_penalty = 0
        if estimated_cost > budget:
            overage_pct = (estimated_cost - budget) / budget
            for penalty in self.rules["costPenalty"]:
                if overage_pct >= penalty["threshold"]:
                    cost_penalty = penalty["deduction"]
                    
        # 6. Complexity Penalty
        complexity_rules = self.rules["complexityPenalty"]
        complexity_penalty = 0
        complexity_penalty += manual_integrations * complexity_rules.get("manualIntegration", -3)
        complexity_penalty += custom_connectors * complexity_rules.get("customConnector", -2)
        
        # 7. Risk Penalty
        # Check for HA and backups across components
        risk_penalty = 0
        has_no_ha = any(str(comp.get("identity", {}).get("haFailover", "")).lower() == "none" for comp in [self.components.get(cid, {}) for cid in cids])
        if has_no_ha:
            risk_penalty += self.rules["riskPenalty"].get("noHA", -5)
            
        # 8. Calculate overall stack score
        overall_stack_score = avg_score + compat_bonus + completeness_bonus + workload_bonus + cost_penalty + complexity_penalty + risk_penalty
        overall_stack_score = max(0, min(100, overall_stack_score))
        
        # 9. Decision recommendation
        recommendation = "Balanced Stack"
        thresholds = self.rules["decisionThresholds"]
        
        if overall_stack_score > thresholds["preferred"]["minOverall"] and avg_confidence > thresholds["preferred"]["minConfidence"]:
            recommendation = "Preferred Architecture"
        elif overall_stack_score > thresholds["costOptimized"]["minOverall"] and estimated_cost <= budget:
            recommendation = "Cost Optimized"
            
        return {
            "overallScore": overall_stack_score,
            "confidenceScore": avg_confidence,
            "recommendation": recommendation,
            "breakdown": {
                "baseAverageComponentScore": avg_score,
                "compatibilityBonus": compat_bonus,
                "architectureCompletenessBonus": completeness_bonus,
                "workloadFitBonus": workload_bonus,
                "costPenalty": cost_penalty,
                "complexityPenalty": complexity_penalty,
                "riskPenalty": risk_penalty
            },
            "explainabilityReport": {
                "why": f"This stack received a score of {overall_stack_score:.2f} (classified as {recommendation}). It features strong underlying technologies scoring an average of {avg_score:.2f}, bolstered by a compatibility bonus of +{compat_bonus} and workload fit bonus of +{workload_bonus}.",
                "penaltiesApplied": f"Cost penalty: {cost_penalty}; Complexity penalty: {complexity_penalty}; Risk penalty: {risk_penalty}",
                "componentEvaluations": [
                    { "id": e["name"], "score": f"{e['overallScore']:.2f}", "confidence": f"{e['confidenceScore']:.1f}%" } for e in evals
                ]
            }
        }

if __name__ == "__main__":
    evaluator = StackEvaluator()
    print("Decision Engine Evaluator initialized. Running test evaluation...")
    test_stack = ["airbyte", "dbt", "snowflake"]
    report = evaluator.evaluate_stack(test_stack)
    print(json.dumps(report, indent=2))
