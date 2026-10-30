# -*- coding: utf-8 -*-
"""Optical Pulse Wave Velocity & Arterial Stiffness Model for GenPark Personal Agent."""
import json
from typing import Dict, Any

class OpticalPulseWaveVelocityArterialModel:
    @staticmethod
    def compute_pulse_wave_velocity_and_vascular_age(pulse_transit_time_ms: float, systolic_bp: float, chronological_age: int) -> Dict[str, Any]:
        # Bramwell-Hill / Moens-Korteweg proxy: PWV (m/s) ~ path_length / PTT
        # Estimated arterial path length ~ 1.35 meters
        pwv = round(1350.0 / max(50.0, pulse_transit_time_ms), 2)
        
        # Normative PWV increases ~0.1 m/s per decade after 30
        expected_pwv = round(5.5 + max(0, chronological_age - 20) * 0.12 + (systolic_bp - 120.0) * 0.03, 2)
        pwv_delta = pwv - expected_pwv
        vascular_age = round(chronological_age + (pwv_delta * 8.0), 1)
        
        if pwv >= 10.0:
            stiffness = "ADVANCED_ARTERIAL_STIFFNESS (High Cardiovascular Endpoint Risk)"
        elif pwv >= 8.0:
            stiffness = "MODERATE_VASCULAR_AGING"
        else:
            stiffness = "OPTIMAL_HIGH_ELASTIC_COMPLIANCE"

        return {
            "estimated_pwv_m_per_s": pwv,
            "cohort_expected_pwv_m_per_s": expected_pwv,
            "chronological_age": chronological_age,
            "biological_vascular_age": vascular_age,
            "arterial_compliance_status": stiffness
        }

    @staticmethod
    def prescribe_arterial_elasticity_reversal_protocol(pwv_m_s: float) -> Dict[str, Any]:
        return {
            "current_pwv": pwv_m_s,
            "target_pwv": 6.5,
            "vascular_restoration_stack": [
                "Vitamin K2 (MK-7 180 mcg daily) to activate Matrix Gla Protein (MGP) and inhibit vascular calcification",
                "Grape Seed Extract (Proanthocyanidins 300 mg) to restore elastin cross-linking integrity",
                "Continuous nasal breathing during sleep (mouth taping) to boost endogenous endothelial nitric oxide",
                "Isometric handgrip training (4 x 2 min at 30% MVC) to trigger shear-stress mediated arterial vasodilation"
            ]
        }
