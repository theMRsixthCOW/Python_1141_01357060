
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from fpdf import FPDF
import io

def run_analysis():
    output_buffer = io.StringIO()
    
    # 1. Load Data
    iris = load_iris()
    X = iris.data
    y = iris.target
    target_names = iris.target_names
    
    output_buffer.write("--- Method 1: K-Means Clustering (Unsupervised) ---\n")
    
    # Preprocessing
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # KMeans
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    y_pred_kmeans = kmeans.fit_predict(X_scaled)
    
    # Calculating Accuracy for Clustering (Mapping clusters to labels)
    df = pd.DataFrame({'species': y, 'cluster': y_pred_kmeans})
    ct = pd.crosstab(df['cluster'], df['species'])
    
    # Map each cluster to the most frequent species
    cluster_map = {}
    correct_kmeans = 0
    for cluster_id in ct.index:
        species_counts = ct.loc[cluster_id]
        dominant_species = species_counts.idxmax()
        count = species_counts.max()
        cluster_map[cluster_id] = dominant_species
        correct_kmeans += count
        output_buffer.write(f"Cluster {cluster_id}: Predicted {target_names[dominant_species]} (Matches: {count}/{species_counts.sum()})\n")
    
    accuracy_kmeans = correct_kmeans / len(y)
    output_buffer.write(f"K-Means 'Accuracy': {accuracy_kmeans:.4f} ({correct_kmeans}/{len(y)})\n\n")

    # 2. KNN
    output_buffer.write("--- Method 2: K-Nearest Neighbors (Supervised) ---\n")
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
    
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    y_pred_knn = knn.predict(X_test)
    
    accuracy_knn = accuracy_score(y_test, y_pred_knn)
    output_buffer.write(f"Training set size: {len(X_train)}, Test set size: {len(X_test)}\n")
    output_buffer.write(f"KNN Accuracy on Test Set: {accuracy_knn:.4f}\n")
    
    return output_buffer.getvalue(), accuracy_kmeans, accuracy_knn

def create_pdf(output_text, acc_kmeans, acc_knn):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "HW12: Iris Classification Analysis", ln=True, align='C')
    pdf.ln(10)
    
    # Question 1
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "1. Accuracy Results of the Two Methods:", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"- Method 1 (K-Means): {acc_kmeans:.2%} (Unsupervised)", ln=True)
    pdf.cell(0, 10, f"- Method 2 (KNN): {acc_knn:.2%} (Supervised)", ln=True)
    pdf.ln(5)
    
    # Screenshot simulation
    pdf.set_fill_color(240, 240, 240)
    pdf.set_font("Courier", '', 10)
    pdf.multi_cell(0, 5, output_text, fill=True)
    pdf.ln(10)
    
    # Question 2
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "2. Which method performed better?", ln=True)
    pdf.set_font("Arial", '', 12)
    improvement = acc_knn - acc_kmeans
    pdf.multi_cell(0, 10, f"The KNN (Supervised) method performed better with an accuracy of {acc_knn:.2%}, "
                          f"compared to K-Means' {acc_kmeans:.2%}. KNN benefits from having access to the true labels during training.")
    pdf.ln(5)
    
    # Question 3
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "3. Characteristics of the two methods:", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, 
        "Method 1: K-Means Clustering\n"
        "- Unsupervised Learning: Does not use labeled data for training.\n"
        "- Groups data points based on feature similarity (Euclidean distance).\n"
        "- Requires specifying the number of clusters (k) beforehand.\n\n"
        "Method 2: K-Nearest Neighbors (KNN)\n"
        "- Supervised Learning: Uses labeled training data.\n"
        "- Classifies a new data point based on the majority class of its 'k' nearest neighbors.\n"
        "- Non-parametric and instance-based (lazy learning)."
    )
    
    pdf.output("d:\\py\\theMRsixthCOW\\HW12.pdf")

if __name__ == "__main__":
    text_out, acc1, acc2 = run_analysis()
    create_pdf(text_out, acc1, acc2)
    print("HW12.pdf generated successfully.")
