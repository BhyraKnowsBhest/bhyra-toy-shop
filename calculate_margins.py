pythondef calculate_garment_economics(style_name, raw_cmt, fabric_cost, hardware_cost, overhead_per_unit):
    """
    Computes precise Landed Costs, Wholesale Tiers, and Retail MSRP 
    configurations for the apparel line.
    """
    # 1. Total Raw Manufacturing Cost (FOB Price)
    fob_cost = raw_cmt + fabric_cost + hardware_cost
    
    # 2. Add structural hidden costs (Freight shipping, packaging matrix, waste allowance)
    shipping_and_duty = fob_cost * 0.18  # Estimate 18% for international freight/duties
    packaging_and_labels = 2.50         # Box, polybag, custom woven labels, and hangtags
    waste_buffer = fob_cost * 0.05       # 5% fabric yield scrap allowance buffer
    
    # Realized Landed Cost per single garment unit
    landed_cost = fob_cost + shipping_and_duty + packaging_and_labels + waste_buffer
    
    # 3. Apply standard fashion multiplier markups (2.0x Wholesale, 2.2x Retail markup)
    wholesale_price = landed_cost * 2.0
    retail_msrp = wholesale_price * 2.2
    
    # 4. Extract programmatic margin percentages for profit visibility
    wholesale_margin = ((wholesale_price - landed_cost) / wholesale_price) * 100
    retail_margin = ((retail_msrp - landed_cost) / retail_msrp) * 100
    
    # Display clear financial layout matrix to terminal
    print(f"==================================================")
    print(f" FINANCIAL METRICS FOR: {style_name.upper()}")
    print(f"==================================================")
    print(f" • Base Factory Production (FOB): ${fob_cost:.2f}")
    print(f" • True Landed Cost (With Overhead): ${landed_cost:.2f}")
    print(f" • Target Wholesale Price (B2B): ${wholesale_price:.2f} [Margin: {wholesale_margin:.1f}%]")
    print(f" • Target Retail Price (DTC MSRP):  ${retail_msrp:.2f} [Margin: {retail_margin:.1f}%]")
    print(f"==================================================\\n")

if __name__ == "__main__":
    print("[SYSTEM ENGINE] Running collection margin modeling calculations...\\n")
    
    # Sourcing projections for the Slim-Fit Modular Hoodie
    calculate_garment_economics(
        style_name="Slim Modular Hoodie (NW-2026-HD01-S)",
        raw_cmt=14.50,       # Cut, Make, Trim labor cost
        fabric_cost=16.00,    # 450 GSM Organic Cotton French Terry
        hardware_cost=1.50,   # High strength drawcords
        overhead_per_unit=3.00
    )
    
    # Sourcing projections for the Tapered Trouser
    calculate_garment_economics(
        style_name="Tapered Trouser (NW-2026-TR02-S)",
        raw_cmt=22.00,       # Tailoring labor cost
        fabric_cost=24.50,    # Wool/Poly Gabardine Twill
        hardware_cost=4.00,   # Zipper fly, closures, and internal grip waistband
        overhead_per_unit=3.50
    )
