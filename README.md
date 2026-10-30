# PPG Pulse Wave Velocity (baPWV) & Biological Vascular Age Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

Photoplethysmography (PPG) pulse transit time (PTT), pulse wave velocity (baPWV m/s), and biological vascular age calibration. Built for GenPark (https://www.genpark.ai).

## Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## MCP Tools Exposed
- `compute_pulse_wave_velocity_and_vascular_age`: Calculate estimated Brachial-Ankle Pulse Wave Velocity (baPWV m/s) and biological vascular age from PPG transit time and blood pressure.
- `prescribe_arterial_elasticity_reversal_protocol`: Formulate targeted lifestyle and nutraceutical interventions to reverse arterial calcification and restore arterial compliance.

## Installation & Usage
```bash
python -m genpark_personal_agent_optical_pulse_wave_velocity_arterial_skill.server --test
```
