# Blood Bank Management System

A command-line Python application for blood-bank staff to manage blood stock, register donors, issue blood units, and search donor records.

## Problem Statement
- **PS No.:** 62
- **Project Title:** Blood Bank Management System
- **Language:** Python 3
- **Concepts Used:** Dictionaries, Lists, File Handling, Linear Search

## Features
1. **Add Donor:** Validates donor name, blood group, and positive integer units, saves the record to `donors.txt`, and updates the available blood stock.
2. **Issue Blood:** Checks stock availability for the requested blood group and deducts the issued units if sufficient stock exists.
3. **View Stock:** Displays current available units for all eight blood groups (`A+`, `A-`, `B+`, `B-`, `O+`, `O-`, `AB+`, `AB-`).
4. **Search Donors:** Searches `donors.txt` records by blood group and lists matching donors along with the total count.
5. **Exit:** Safely closes the application.

## Initial Stock
| Blood Group | Initial Units |
| :--- | :---: |
| `A+` | 10 |
| `B+` | 5 |
| `O+` | 8 |
| `AB+` | 2 |
| `A-`, `B-`, `O-`, `AB-` | 0 |

## How to Run
```bash
python3 blood_bank.py
