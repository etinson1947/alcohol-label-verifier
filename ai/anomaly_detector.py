import numpy as np
import cv2


class LabelAnomalyDetector:

    def detect(self, image_path):

        image = cv2.imread(image_path)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        variance = np.var(gray)

        brightness = np.mean(gray)

        anomalies = []

        # Low detail / blur detection
        if variance < 50:
            anomalies.append("LOW_VISUAL_DETAIL")

        # Overexposure / glare detection
        if brightness > 220:
            anomalies.append("OVEREXPOSURE")

        # Underexposure detection
        if brightness < 40:
            anomalies.append("UNDEREXPOSURE")

        return {
            "anomalies": anomalies,
            "risk_score": len(anomalies) * 0.33
        }
