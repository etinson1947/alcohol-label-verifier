import cv2
import numpy as np


class CounterfeitDetector:

    def extract_features(self, image_path):

        image = cv2.imread(image_path)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        edges = cv2.Canny(gray, 50, 150)

        texture_score = np.std(gray)

        edge_density = np.sum(edges > 0) / edges.size

        return np.array([texture_score, edge_density])

    def predict_risk(self, image_path):

        features = self.extract_features(image_path)

        score = float(
            (features[0] < 40) or (features[1] < 0.02)
        )

        return {
            "counterfeit_risk": score,
            "confidence": 0.85
        }
