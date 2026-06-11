# Alcohol Label Compliance Verification System

## Overview

The Alcohol Label Compliance Verification System is a web-based application that verifies alcohol beverage labels against product master records and TTB-oriented labeling requirements.

The application can be deployed directly to Azure App Service and support:

Web-based label uploads
Batch OCR processing
Compliance validation against TTB rules
Product master matching
Manual review workflow
Cloud logging and monitoring hooks
Secure secret management integration points


The system uses:

* PaddleOCR for OCR text extraction
* OpenCV for image preprocessing
* SQLite for product master records
* Flask web application
* TTB Rules Engine for compliance validation
* Batch image upload processing
* OCR confidence scoring
* Manual review workflow

The application is designed to process images captured from alcohol bottles and evaluate whether required label elements are present and match approved product information.

---

# Features

## OCR Processing

* PaddleOCR text extraction
* Angle correction support
* Image preprocessing
* Adaptive thresholding
* Curved bottle label support
* Low-quality image handling

## Product Verification

Compares OCR results against approved product records.

Example:

| Field           | Expected Value                    |
| --------------- | --------------------------------- |
| Brand Name      | OLD TOM DISTILLERY                |
| Class Type      | Kentucky Straight Bourbon Whiskey |
| Alcohol Content | 45% Alc./Vol.                     |
| Proof           | 90 Proof                          |
| Net Contents    | 750 mL                            |

---

## TTB-Oriented Validation Rules

Separate validators are implemented for:

* Brand Name
* Class/Type
* Alcohol Content (ABV)
* Proof Statement
* Net Contents
* Government Warning
* Bottler Information

Additional validators can be added for:

* COLA Number
* Appellation of Origin
* Age Statement
* State-Specific Requirements
* Importer Information

---

## Compliance Reporting

The system generates:

* PASS
* FAIL
* MANUAL REVIEW

Reports include:

* OCR confidence score
* Validation findings
* Errors
* Warnings
* Extracted OCR text

---

## Manual Review Workflow

Labels are automatically flagged when OCR confidence falls below:

```python
0.75
```

Examples:

* Blurry images
* Glare on bottle
* Curved labels
* Incomplete scans
* Damaged labels

---

# System Requirements

## Operating Systems

* Windows 10/11
* Ubuntu 20+
* macOS

---

## Python Version

Python 3.10 or newer

Recommended:

```bash
Python 3.11
```

---

# Project Structure

```text
alcohol-label-verifier/

├── app.py
├── verifier.py
├── products.db
├── requirements.txt

├── uploads/

├── templates/
│   └── index.html

├── static/

└── reports/
```

---

# Installation

## Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Upgrade Pip

```bash
pip install --upgrade pip
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# requirements.txt

```text
flask
opencv-python
numpy
pillow
paddleocr
paddlepaddle
rapidfuzz
pandas
```

Note:

SQLite is included with Python and normally does not need installation.

---

# PaddleOCR Installation Notes

CPU version:

```bash
pip install paddlepaddle
pip install paddleocr
```

GPU version:

```bash
pip install paddlepaddle-gpu
pip install paddleocr
```

Refer to PaddleOCR documentation for CUDA compatibility requirements.

---

# Database Setup

Create SQLite database:

```bash
products.db
```

Create products table:

```sql
CREATE TABLE products (

    sku TEXT PRIMARY KEY,

    brand_name TEXT,
    class_type TEXT,

    alcohol_content TEXT,
    proof TEXT,

    net_contents TEXT,

    government_warning TEXT,

    bottler_name TEXT,
    bottler_address TEXT
);
```

---

## Sample Product Record

```sql
INSERT INTO products VALUES (

'SKU-1001',

'OLD TOM DISTILLERY',

'Kentucky Straight Bourbon Whiskey',

'45% Alc./Vol.',

'90 Proof',

'750 mL',

'ACCORDING TO THE SURGEON GENERAL WOMEN SHOULD NOT DRINK ALCOHOL BEVERAGES DURING PREGNANCY BECAUSE OF THE RISKS OF BIRTH DEFECTS',

'OLD TOM DISTILLERY',

'LOUISVILLE KY'
);
```

---

# Running the Application

Start Flask:

```bash
python app.py
```

Expected output:

```text
* Running on http://127.0.0.1:5000
```

Open browser:

```text
http://localhost:5000
```

---

# Uploading Labels

Supported formats:

* JPG
* JPEG
* PNG
* TIFF

Users can:

* Upload a single image
* Upload multiple images
* Batch process bottle label scans

---

# Compliance Workflow

## Step 1

Upload label image.

## Step 2

OCR extraction occurs using PaddleOCR.

## Step 3

OCR text is normalized.

Example:

```text
ALC VOL
```

becomes

```text
ALC./VOL.
```

---

## Step 4

Product master record is loaded.

Example:

```text
SKU-1001
```

---

## Step 5

TTB Rules Engine executes validators.

Example:

```text
Brand Name Validator
Class Type Validator
Alcohol Content Validator
Proof Validator
Government Warning Validator
```

---

## Step 6

Compliance report is generated.

Example:

```json
{
  "status": "PASS",
  "ocr_confidence": 0.94,
  "manual_review": false
}
```

---

# Batch Processing

Example:

Upload:

```text
label1.jpg
label2.jpg
label3.jpg
label4.jpg
```

Results:

```json
[
  {
    "file":"label1.jpg",
    "status":"PASS"
  },
  {
    "file":"label2.jpg",
    "status":"FAIL"
  },
  {
    "file":"label3.jpg",
    "status":"MANUAL_REVIEW"
  }
]
```

---

# Error Handling

The application handles:

## Invalid Images

```text
Image cannot be loaded
```

## No OCR Text Found

```text
No text detected
```

## Missing Product Record

```text
Product not found
```

## OCR Confidence Too Low

```text
Manual Review Required
```

---

# Compliance Status Definitions

## PASS

All required validations succeeded.

---

## FAIL

One or more required TTB validations failed.

---

## MANUAL REVIEW

OCR confidence below threshold.

Human review is required before approval.

---

# Production Recommendations

For production deployment:

## Database

Replace SQLite with:

* PostgreSQL
* Microsoft SQL Server
* Oracle

---

## Authentication

Implement:

* Active Directory
* Azure AD
* SAML
* LDAP

---

## Reporting

* PDF compliance reports
* Audit history
* Validation logs

---

## Image Processing Enhancements

* Perspective correction
* Label detection
* Bottle contour detection
* Barcode recognition
* QR code validation

---

## Additional TTB Validators

Additional validators are available using the final top tier or FedRAMP aligned architecture all files are included and referenced in the project structure document:

* COLA Number Validator
* Age Statement Validator
* Distilled By Validator
* Imported By Validator
* Geographic Origin Validator

---

The final top tier or FedRAMP architecture moves from well-architected enterprise app into a compliance-grade, audit-heavy, multi-agency-capable platform.

This provides four upgrades:

Immutable audit logging (FedRAMP-style)
Real TTB/COLA rule engine structure
Secure CI/CD with scanning gates
AI anomaly detection layer (beyond OCR)

Final upgrade achieves the following:
[Regulatory strength]
TTB-style rule modeling
COLA extensibility
Deterministic compliance evaluation

[Security maturity]
Immutable audit logging
CI/CD security gates
Container vulnerability scanning

[Intelligence layer]
OCR + visual anomaly detection
Pre-OCR quality filtering
Reduced false failures

[Government readiness]
Audit defensibility
Traceable decisions
Secure deployment pipeline
Infrastructure suitable for restricted networks

FINAL SYSTEM STATE 
The final system state is a federal-grade, audit-ready, multi-agency compliant platform aligned with NIST 800-53 / FedRAMP Moderate style controls and operational patterns.

1. Compliance-grade intelligence system
TTB rules engine
COLA-style validation model
Versioned regulatory logic

2. Federal audit readiness
Immutable audit ledger
NIST 800-53 mapping
Evidence automation engine

3. Advanced AI layer
OCR (PaddleOCR)
Image anomaly detection
Counterfeit classification model

4. Multi-agency architecture
Federated deployment model
Cross-agency governance support
Event-driven synchronization

5. Enterprise-scale deployment
Azure App Service + AKS hybrid ready
Helm-based orchestration
CI/CD + security scanning already defined

Verify all compliance logic and validation rules against current TTB regulations before use in production regulatory workflows.
