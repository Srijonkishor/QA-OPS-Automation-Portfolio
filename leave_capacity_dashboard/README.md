# Leave Capacity Dashboard Logic

This project demonstrates simplified leave capacity and shrinkage calculation logic.

## Purpose

The goal is to help operations teams understand workforce availability for a given week.

The workflow calculates:

- Planned leaves
- Expected workdays
- Actual workdays
- Shrinkage rate
- Notification-ready weekly summaries

## Shrinkage Formula

```text
Shrinkage Rate = (Expected Workdays - Actual Workdays) / Expected Workdays
