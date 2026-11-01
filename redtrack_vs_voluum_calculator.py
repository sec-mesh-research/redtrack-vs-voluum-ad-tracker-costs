#!/usr/bin/env python3
"""
RedTrack vs Voluum Ad Tracker Cost & S2S Postback Calculator 2026.
"""
import argparse

def calculate(monthly_events, domains):
    # RedTrack Pro: $149/mo (1M events, $0.06/k overage, includes multiple custom domains)
    rt_base = 149.0
    rt_overage = (max(0, monthly_events - 1000000) / 1000.0) * 0.06
    rt_total = rt_base + rt_overage

    # Voluum Profit: $199/mo (1M events, $0.06/k overage)
    vol_base = 199.0
    vol_overage = (max(0, monthly_events - 1000000) / 1000.0) * 0.06
    vol_total = vol_base + vol_overage

    diff = vol_total - rt_total

    print("=" * 60)
    print("Media Buying Tracker Benchmark: RedTrack vs Voluum")
    print("=" * 60)
    print(f"Monthly Events Tracked:  {monthly_events:,}")
    print(f"Tracking Domains:        {domains}")
    print(f"RedTrack Pro Monthly:    ${rt_total:.2f}/mo")
    print(f"Voluum Profit Monthly:   ${vol_total:.2f}/mo")
    print(f"Monthly Difference:      ${abs(diff):.2f}/mo ({'RedTrack Cheaper' if diff > 0 else 'Voluum Cheaper'})")
    print("=" * 60)
    return rt_total, vol_total

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RedTrack vs Voluum Calculator")
    parser.add_argument("--monthly-events", type=int, default=1200000)
    parser.add_argument("--domains", type=int, default=3)
    args = parser.parse_args()
    calculate(args.monthly_events, args.domains)
