# QA-OPS Automation Portfolio

A public, sanitized portfolio of QA operations, Trust & Safety analytics, workflow automation, and data operations projects.

This repository demonstrates how manual QA and operations workflows can be converted into structured, automation-backed data systems using Python, SQL-style logic, JSON parsing, data validation, sampling rules, dashboard-ready metrics, and clear documentation.

## Overview

Many QA and Trust & Safety workflows depend on repeated manual tasks such as:

- Pulling production data
- Selecting QA samples
- Parsing review logs
- Tracking rejected cases
- Calculating workforce capacity
- Monitoring QA performance
- Preparing dashboard-ready metrics
- Converting raw operational data into readable summaries

This portfolio contains simplified, public-friendly versions of those workflows using mock data only.

The goal is to show practical data operations skills: turning messy operational inputs into reliable, structured, and stakeholder-friendly outputs.

---

## Projects Included

### 1. Production Automation

**Folder:** `production_automation`

This module demonstrates a simplified QA production tracking workflow.

It includes:

- Previous working-day calculation
- Production count tracking
- Schema validation
- Duplicate-safe update logic
- Backfill-friendly design

**Use case:**  
Automatically track daily QA production without manually updating records or duplicating rows.

**Skills demonstrated:**

- Python scripting
- date logic
- data validation
- production tracking
- duplicate prevention
- operational reporting logic

---

### 2. QA Sampling Engine

**Folder:** `qa_sampling_engine`

This module demonstrates how QA review samples can be selected from a larger pool of reviewed materials.

It includes:

- Random sample selection
- Fixed-count sampling
- Percentage-based sampling
- Reviewer-level grouping
- Duplicate material prevention

**Use case:**  
Select QA samples fairly and consistently for audit, PM QC, or quality review workflows.

**Skills demonstrated:**

- sampling logic
- pandas data manipulation
- duplicate handling
- QA workflow understanding
- review-data preparation

---

### 3. Case Repository Workflow

**Folder:** `case_repository`

This module demonstrates how raw review records can be converted into a structured rejected-case repository.

It includes:

- JSON-like field parsing
- review status classification
- rejected-case filtering
- metadata enrichment
- case priority tagging
- clean repository output

**Use case:**  
Maintain a structured repository of rejected QA cases for reporting, review, escalation, and quality analysis.

**Skills demonstrated:**

- JSON parsing
- case tracking
- data enrichment
- review status mapping
- rejected-case reporting
- structured output generation

---

### 4. JSON ETL Review Log Parser

**Folder:** `json_etl_pipeline`

This module demonstrates an ETL pipeline for nested JSON review logs.

It includes:

- raw JSON extraction
- nested field flattening
- hypothesis validation
- data-quality checks
- cleaned CSV output
- readable Markdown case summaries

**Use case:**  
Convert raw nested review logs into structured datasets and business-readable summaries for QA and Trust & Safety reporting.

**Skills demonstrated:**

- ETL pipeline design
- JSON parsing
- nested data transformation
- hypothesis testing
- data-quality validation
- readable summary generation
- operational analytics

---

### 5. Leave Capacity Dashboard Logic

**Folder:** `leave_capacity_dashboard`

This module demonstrates simplified leave capacity and shrinkage calculation logic.

It includes:

- planned leave tracking
- expected workday calculation
- actual workday calculation
- shrinkage rate calculation
- notification-ready weekly summaries

**Use case:**  
Help operations teams understand workforce availability, planned leave impact, and weekly shrinkage.

**Skills demonstrated:**

- capacity planning
- workforce analytics
- shrinkage calculation
- dashboard-ready metric logic
- notification summary generation

---

## Repository Structure

```text
QA-OPS-Automation-Portfolio/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── production_automation/
├── qa_sampling_engine/
├── case_repository/
├── json_etl_pipeline/
└── leave_capacity_dashboard/
