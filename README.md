**<h1>Kidney Stone Prediction based on Urine Analysis</h1>**
The dataset used, consists of six physical characteristics of urine (specific gravity, pH, osmolarity, conductivity, urea concentration, and calcium concentration).
**<h2>Overview</h2>**
This project aims to leverage data science techniques to develop a robust predictive model for kidney stone formation. Kidney stones present a significant medical challenge due to their painful symptoms and potential complications. They vary in size and can cause severe pain, urinary tract obstruction, infections, and kidney damage. Early detection and prediction of kidney stones can facilitate timely intervention and prevent complications.
<br>
**<h2>Approach</h2>**
The Radial Basis Function (RBF) kernel was chosen for Support Vector Machine (SVM) due to its effectiveness in capturing non-linear relationships. After hyperparameter tuning, the model achieved an improved accuracy of 0.8125. The RBF kernel excels in modeling complex patterns, crucial in kidney stone analysis where non-linear relationships between medical features and outcomes are common. Logistic regression and Naive Bayes are unsuitable for non-linear data, while Random Forest may struggle with intricate relationships. Hence, the RBF kernel stands out as a suitable choice for accurate predictions in this context.

