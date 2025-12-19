**© [lichani belkacem], 2024. Tous droits réservés.**

*Ce dépôt contient le code source et les résultats du projet de recherche personnel **FRACTAL-ADN**. Ce travail est publié à titre de **preuve de concept et de démonstration**.*
*La réutilisation, la distribution ou la modification du code, des algorithmes ou des résultats présentés **requièrent une autorisation écrite préalable de l'auteur**. Pour toute demande de collaboration ou d'utilisation, veuillez me contacter.*
---
# FRACTAL-ADN: Predicting Promoter Plasticity from 3D Fractal Dimension

This project introduces a novel geometric biomarker for DNA function: the **3D fractal dimension (D)** calculated directly from atomic structures (PDB files).

## 🔑 Key Discovery
Analysis of large-scale public data suggests a **critical threshold (D ≈ 2.15)** that separates rigid from plastic/active promoters with promising predictive power (AUC = 0.798).

## ✅ Validation
The method was validated on the canonical B-DNA structure **1BNA**, yielding **D = 1.69** with high reliability (R² > 0.98), confirming its geometric rigidity relative to the identified threshold.

## 🛠️ Pipeline
The core script (`fractaldim3d.py`) provides a complete pipeline to:
1.  Load a PDB file.
2.  Compute the 3D fractal dimension via box-counting.
3.  Output the result and a quality metric (R²).

## 👤 Author
lichani belkacem- Instrumentiste 

*This is a personal research project in computational biology.*
