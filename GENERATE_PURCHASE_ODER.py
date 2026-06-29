pythonimport os
from datetime import datetime

def generate_factory_po(po_number, style_id, style_name, size, units, unit_landed_cost, manufacturer_name):
    """
    Programmatically compiles and formats a formal industrial Purchase Order (PO) 
    document to initialize a production run with an authorized vendor.
    """
    # 1. Calculate structural financial milestones
    total_order_value = units * unit_landed_cost
    deposit_required = total_order_value * 0.50  # Strict 50% upfront milestone
    remaining_balance = total_order_value * 0.50 # 50% due post-QA verification
    
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # 2. Build the structural textual layout invoice matrix
    po_template = f"""========================================================================
OFFICIAL INVENTORY PURCHASE ORDER (PO)
========================================================================
PO NUMBER:          {po_number}
PO ISSUED DATE:     {current_date}
DESIGN FIRM:        NEXUS SYSTEM LAYER LLC (Nevada, USA)
MANUFACTURING ENTITY: {manufacturer_name}
========================================================================

PRODUCT LINE MATRIX:
------------------------------------------------------------------------
• Style Reference ID:   {style_id}
• Garment Description:   {style_name}
• Sizing Allocation:     Size {size}
• Order Batch Size:     {units} Units
• Factory Unit Cost:    ${unit_landed_cost:.2f} Per Unit

FINANCIAL RECONCILIATION SUMMARY:
------------------------------------------------------------------------
• TOTAL GROSS INVOICE VALUE:      ${total_order_value:.2f}
• MANDATORY 50% UPFRONT DEPOSIT:  ${deposit_required:.2f} (Due to release fabric)
• FINAL 50% OUTSTANDING BALANCE:  ${remaining_balance:.2f} (Due post-QA clearance)

COMPLIANCE GOVERNANCE TERMS:
------------------------------------------------------------------------
Production must adhere explicitly to specs in "GLOBAL_MASTER_TECH_PACK.md". 
All items must fall within acceptable measurement thresholds. 
Shipments are subject to a 1% late penalty charge per calendar day delayed.

AUTHORIZED RELEASING SIGNATURE:

____________________________________________  Date: __________________
NEXUS SYSTEM LAYER LLC Operational Officer
========================================================================"""

    # 3. Output document layout cleanly to a text log file
    filename = f"PO_{po_number}_{style_id}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(po_template.strip())
        
    print(f"[PO ENGINE] Success! Compiled legal purchase order file: {filename}")

if __name__ == "__main__":
    print("[SYSTEM ENGINE] Running purchase order invoicing automation script...\\n")
    
    # Generate Purchase Order for the initial run of the Slim-Fit Hoodie
    generate_factory_po(
        po_number="PO-2026-001",
        style_id="NW-HD01-S",
        style_name="Slim Modular Hoodie (450 GSM Cotton French Terry)",
        size="MED (Sample Core Block)",
        units=150,
        unit_landed_cost=32.00,  # Base FOB + Hidden overhead adjustments
        manufacturer_name="Alpha Trim & Cut Sew Mills Inc."
