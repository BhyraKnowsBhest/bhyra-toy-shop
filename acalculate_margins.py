pythondef analyze_brand_economics(style_name, raw_cmt, fabric_cost, hardware_cost, fixed_monthly_overhead):
    """
    Computes precise product pricing matrices alongside the commercial 
    break-even metrics required to sustain a live Nevada operation.
    """
    # 1. Base production calculations (FOB and true Landed costs)
    fob_cost = raw_cmt + fabric_cost + hardware_cost
    shipping_and_duty = fob_cost * 0.18      # Estimates 18% for logistics
    packaging_and_labels = 2.50              # Trims, bags, hangtags, and stickers
    waste_buffer = fob_cost * 0.05           # 5% fabric scrap allowance
    
    landed_cost = fob_cost + shipping_and_duty + packaging_and_labels + waste_buffer
    
    # 2. Establish commercial pricing tiers
    wholesale_price = landed_cost * 2.0
    retail_msrp = wholesale_price * 2.2
    
    # 3. Compute pure profit margins per single unit
    wholesale_profit_per_unit = wholesale_price - landed_cost
    retail_profit_per_unit = retail_msrp - landed_cost
    
    # 4. Break-even logic (Fixed Operational Overhead / Profit Margin per Unit)
    break_even_units_wholesale = fixed_monthly_overhead / wholesale_profit_per_unit
    break_even_units_retail = fixed_monthly_overhead / retail_profit_per_unit
    
    # Display clean engineering financial telemetry to terminal
    print(f"==================================================")
    print(f" FINANCIAL & RUNRATE METRICS: {style_name.upper()}")
    print(f"==================================================")
    print(f"  • True Unit Landed Cost:     ${landed_cost:.2f}")
    print(f"  • Wholesale Price (B2B):     ${wholesale_price:.2f} [Profit: ${wholesale_profit_per_unit:.2f}/unit]")
    print(f"  • Retail Price (DTC MSRP):    ${retail_msrp:.2f} [Profit: ${retail_profit_per_unit:.2f}/unit]")
    print(f"--------------------------------------------------")
    print(f"  • TARGET MONTHLY OPERATING COSTS: ${fixed_monthly_overhead:.2f}")
    print(f"  • Monthly Break-Even (Wholesale Channels): {int(break_even_units_wholesale) + 1} units")
    print(f"  • Monthly Break-Even (Direct E-Com Channels): {int(break_even_units_retail) + 1} units")
    print(f"==================================================\\n")

if __name__ == "__main__":
    print("[SYSTEM ENGINE] Executing automated financial runrate simulations...\\n")
    
    # Define baseline fixed operational expenses for a lean Nevada startup footprint
    # (Includes SilverFlume amortization, domain routing, basic software stack, and small storage)
    NEVADA_STARTUP_MONTHLY_OVERHEAD = 650.00
    
    # Run calculation pass for the Slim Hoodie
    analyze_brand_economics(
        style_name="Slim Modular Hoodie (NW-2026-HD01-S)",
        raw_cmt=14.50,
        fabric_cost=16.00,
        hardware_cost=1.50,
        fixed_monthly_overhead=NEVADA_STARTUP_MONTHLY_OVERHEAD
    )
    
    # Run calculation pass for the Tapered Trouser
    analyze_brand_economics(
        style_name="Tapered Trouser (NW-2026-TR02-S)",
        raw_cmt=22.00,
        fabric_cost=24.50,
        hardware_cost=4.00,
        fixed_monthly_overhead=NEVADA_STARTUP_MONTHLY_OVERHEAD
    )
