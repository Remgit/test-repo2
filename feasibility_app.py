import argparse


def analyze_feasibility(cost, expected_revenue, discount_rate=0.1, years=1):
    """Compute feasibility metrics.

    Parameters
    ----------
    cost : float
        Initial cost of the project.
    expected_revenue : float
        Expected revenue at the end of the evaluation period.
    discount_rate : float, optional
        Discount rate per period. Default is 0.1 (10%).
    years : int, optional
        Number of periods until revenue is realized. Default is 1.

    Returns
    -------
    dict
        Contains net present value (npv), profit, return on investment (roi)
        and feasibility flag.
    """
    npv = expected_revenue / ((1 + discount_rate) ** years)
    profit = npv - cost
    roi = profit / cost
    feasible = roi > 0
    return {"npv": npv, "profit": profit, "roi": roi, "feasible": feasible}


def main():
    parser = argparse.ArgumentParser(description="Feasibility analysis app")
    parser.add_argument("cost", type=float, help="Initial cost")
    parser.add_argument(
        "expected_revenue",
        type=float,
        help="Expected revenue at the end of the period",
    )
    parser.add_argument(
        "-d",
        "--discount-rate",
        type=float,
        default=0.1,
        help="Discount rate per period (default: 0.1)",
    )
    parser.add_argument(
        "-y",
        "--years",
        type=int,
        default=1,
        help="Number of periods until revenue occurs (default: 1)",
    )
    args = parser.parse_args()

    result = analyze_feasibility(
        args.cost, args.expected_revenue, args.discount_rate, args.years
    )
    print(f"NPV: {result['npv']:.2f}")
    print(f"Profit: {result['profit']:.2f}")
    print(f"ROI: {result['roi']:.2%}")
    print("Feasible" if result["feasible"] else "Not feasible")


if __name__ == "__main__":
    main()
