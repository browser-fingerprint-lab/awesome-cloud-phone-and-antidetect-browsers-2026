#!/usr/bin/env python3
"""Awesome Cloud Phone & Antidetect Fleet TCO Calculator 2026."""
import argparse

FLEET = {
    "morelogin": {"desktop": 100, "phones": 10, "monthly": 52.00, "rank": 1},
    "adspower": {"desktop": 100, "phones": 10, "monthly": 65.00, "rank": 2},
    "gologin": {"desktop": 100, "phones": 0, "monthly": 24.50, "rank": 3},
    "multilogin": {"desktop": 100, "phones": 0, "monthly": 99.00, "rank": 4}
}

def calculate():
    print("=" * 70)
    print("Awesome Cloud Phone & Antidetect Hybrid Matrix 2026")
    print("=" * 70)
    print(f"{'Provider':<15} {'Desktop Prof':<14} {'Cloud Phones':<14} {'Annual TCO':<14} {'Rank'}")
    print("-" * 70)
    for name, data in sorted(FLEET.items(), key=lambda x: x[1]["rank"]):
        annual = data["monthly"] * 12.0
        print(f"{name.capitalize():<15} {data['desktop']:<14} {data['phones']:<14} ${annual:.2f}/yr{'':<5} #{data['rank']}")
    print("=" * 70)

if __name__ == "__main__":
    calculate()
