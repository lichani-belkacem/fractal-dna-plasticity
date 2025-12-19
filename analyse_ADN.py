# === FRACTAL-ADN : Calcul de la dimension fractale 3D ===
# Ce script calcule la dimension fractale (D) d'une structure d'ADN (fichier PDB)
import numpy as np
import os

def compute_fractal_dimension_3d(pdb_file):
    """
    Calcule la dimension fractale 3D par la méthode du box-counting.
    Retourne D (dimension), R² (qualité), et les données pour le graphique.
    """
    # 1. LECTURE DU FICHIER PDB
    coords = []
    with open(pdb_file, 'r') as f:
        for line in f:
            if line.startswith(('ATOM', 'HETATM')):
                try:
                    x = float(line[30:38])
                    y = float(line[38:46])
                    z = float(line[46:54])
                    coords.append([x, y, z])
                except:
                    continue
    
    coords = np.array(coords)
    if len(coords) < 10:
        print("❌ Trop peu d'atomes trouvés.")
        return None, None, None, None
    
    # 2. BOX-COUNTING 3D
    min_coord = np.min(coords, axis=0)
    max_coord = np.max(coords, axis=0)
    size = max_coord - min_coord
    max_size = np.max(size)
    
    # Échelles adaptées (celles qui ont donné R²=0.9876)
    r_min = 2.0
    r_max = max_size / 4.0
    rayons = np.logspace(np.log10(r_max), np.log10(r_min), 15)
    
    nb_boites = []
    for r in rayons:
        # Attribution à une grille 3D
        bins_x = np.floor((coords[:, 0] - min_coord[0]) / r).astype(int)
        bins_y = np.floor((coords[:, 1] - min_coord[1]) / r).astype(int)
        bins_z = np.floor((coords[:, 2] - min_coord[2]) / r).astype(int)
        
        # Comptage des boîtes uniques
        boites_uniques = set(zip(bins_x, bins_y, bins_z))
        nb_boites.append(len(boites_uniques))
    
    # 3. CALCUL DE LA DIMENSION FRACTALE D
    log_r = np.log(rayons)
    log_n = np.log(nb_boites)
    
    # Régression linéaire
    coeffs = np.polyfit(log_r, log_n, 1)
    D = -coeffs[0]  # La dimension est l'opposé de la pente
    
    # Calcul de la qualité R²
    correlation_matrix = np.corrcoef(log_r, log_n)
    R2 = correlation_matrix[0, 1]**2
    
    return D, R2, log_r, log_n

# === EXEMPLE D'UTILISATION ===
if __name__ == "__main__":
    # Remplacez "1BNA.pdb" par le chemin de votre fichier
    fichier_pdb = "1BNA.pdb"
    
    if os.path.exists(fichier_pdb):
        D, R2, log_r, log_n = compute_fractal_dimension_3d(fichier_pdb)
        if D is not None:
            print("=" * 50)
            print("RÉSULTATS FRACTALS")
            print("=" * 50)
            print(f"Dimension fractale 3D : D = {D:.3f}")
            print(f"Qualité de l'ajustement : R² = {R2:.4f}")
            print(f"Interprétation : Structure {'rigide' if D < 2.15 else 'plastique'}")
            print("=" * 50)
    else:
        print(f"❌ Fichier '{fichier_pdb}' introuvable.")
        print("   Placez-le dans le même dossier que ce script.")