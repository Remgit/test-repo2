# Feasibility Analysis App

This repository contains a simple command-line tool that helps evaluate the
viability of a project. The application estimates net present value (NPV),
profit, and return on investment (ROI) from a given cost and expected revenue.

## Usage

```bash
python3 feasibility_app.py COST EXPECTED_REVENUE [-d DISCOUNT_RATE] [-y YEARS]
```

- `COST` – initial project cost
- `EXPECTED_REVENUE` – revenue expected at the end of the evaluation period
- `-d`, `--discount-rate` – discount rate per period (default: `0.1`)
- `-y`, `--years` – number of years until revenue occurs (default: `1`)

Example:

```bash
python3 feasibility_app.py 1000 1500 -d 0.1 -y 1
```

## Running Tests

Run unit tests with:

```bash
python3 -m unittest
```
