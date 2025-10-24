"""
CFA v2.0 - Core Calculation Utilities
All math and scoring logic in one place
"""

from typing import Dict, Tuple, List

PF_TYPES = ["Instrumental", "Composite_70_30", "Holistic_50_50"]

def composite_pf(pf_inst: float, pf_exist: float, pf_type: str) -> float:
    """Calculate composite pragmatic fertility score"""
    if pf_type == "Instrumental":
        return pf_inst
    if pf_type == "Holistic_50_50":
        return 0.5 * pf_inst + 0.5 * pf_exist
    return 0.7 * pf_inst + 0.3 * pf_exist

def apply_fallibilism_bonus(cci: float, bonus: str, admitted_limits: bool = True) -> float:
    """Apply fallibilism bonus if configured"""
    if bonus == "ON" and admitted_limits:
        return min(cci + 0.3, 10.0)
    return cci

def parity_weight(mg: float, parity: str) -> float:
    """Apply parity weighting to moral generativity"""
    return mg if parity == "ON" else 0.5 * mg

def bfi_total(axioms: int, debts: int, debt_weight: str) -> float:
    """Calculate total brute-fact index"""
    w = 1.0 if debt_weight == "Equal_1.0x" else 1.2
    return axioms + w * debts

def ypa_scenario_scores(fr: Dict, cfg: Dict) -> Tuple[Dict, Dict, float]:
    """
    Calculate YPA scores across all scenarios
    Returns: (results_dict, lever_map, bfi)
    """
    CCI = apply_fallibilism_bonus(
        fr["levers"]["CCI"], 
        cfg["fallibilism_bonus"], 
        fr.get("admits_limits", True)
    )
    EDB = fr["levers"]["EDB"]
    PF = composite_pf(
        fr["levers"]["PF_instrumental"], 
        fr["levers"]["PF_existential"], 
        cfg["pf_type"]
    )
    AR = fr["levers"]["AR"]
    MG = parity_weight(fr["levers"]["MG"], cfg["lever_parity"])

    scenarios_weights = {
        "Neutral": {"CCI": 1.0, "EDB": 1.0, "PF": 1.0, "AR": 1.0, "MG": 1.0},
        "Existential": {"CCI": 1.0, "EDB": 2.0, "PF": 1.0, "AR": 1.0, "MG": 2.0},
        "Empirical": {"CCI": 1.5, "EDB": 1.0, "PF": 2.0, "AR": 1.0, "MG": 1.0},
    }

    lever_map = {"CCI": CCI, "EDB": EDB, "PF": PF, "AR": AR, "MG": MG}
    bfi = bfi_total(fr["bf_i"]["axioms"], fr["bf_i"]["debts"], cfg["bfi_debt_weight"])

    results = {}
    for name, weights in scenarios_weights.items():
        total = sum(lever_map[k] * w for k, w in weights.items())
        results[name] = {"total": total, "YPA": total / bfi if bfi > 0 else 0}

    return results, lever_map, bfi

def guardrail_lever_coupling(PF: float, CCI: float) -> Tuple[bool, str]:
    """Check lever coupling guardrail"""
    if PF >= 9 and CCI < 6.5:
        return False, f"⚠️ WARNING: PF={PF:.2f} >= 9 but CCI={CCI:.2f} < 6.5"
    return True, f"✅ PASS: Lever-Coupling satisfied"

def symmetry_audit(fr: Dict, cfg: Dict) -> List[Tuple[str, float, float, float]]:
    """
    Run symmetry audit by testing toggle inversions
    Returns list of (toggle_name, baseline, flipped, delta)
    """
    def get_ypa(framework, config):
        results, _, _ = ypa_scenario_scores(framework, config)
        return results["Neutral"]["YPA"]
    
    baseline = get_ypa(fr, cfg)
    reports = []
    
    # Test lever parity
    cfg_parity = cfg.copy()
    cfg_parity["lever_parity"] = "OFF" if cfg["lever_parity"] == "ON" else "ON"
    delta_parity = get_ypa(fr, cfg_parity) - baseline
    reports.append(("Lever-Parity", baseline, get_ypa(fr, cfg_parity), delta_parity))
    
    # Test PF types
    for pf_type in PF_TYPES:
        if pf_type == cfg["pf_type"]:
            continue
        cfg_pf = cfg.copy()
        cfg_pf["pf_type"] = pf_type
        delta_pf = get_ypa(fr, cfg_pf) - baseline
        reports.append((f"PF->{pf_type}", baseline, get_ypa(fr, cfg_pf), delta_pf))
    
    # Test fallibilism
    cfg_fall = cfg.copy()
    cfg_fall["fallibilism_bonus"] = "OFF" if cfg["fallibilism_bonus"] == "ON" else "ON"
    delta_fall = get_ypa(fr, cfg_fall) - baseline
    reports.append(("Fallibilism", baseline, get_ypa(fr, cfg_fall), delta_fall))
    
    return reports
