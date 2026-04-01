# Coffee Sales BI Self-Hosted Dashboard

This project now includes a self-hosted web dashboard you can run on any machine after download.

## 1) Setup
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 2) Add your CSV
Place your coffee sales CSV at:

```bash
data/coffee_sales.csv
```

Or set a custom path:

```bash
export COFFEE_CSV=/full/path/to/your.csv
```

## 3) Run the site
```bash
python app.py
```

Open in browser:
- `http://localhost:8000`

## 4) What you should see
- KPI cards: Revenue, Transactions, Avg Bill, Best Category
- Charts: Sales by Hour, Sales by Day, Category Revenue, Store Revenue
- If CSV is missing, page shows clear instructions.

## 5) Why changes may not be visible on GitHub
If you can see changes locally but not on GitHub, the branch is likely not pushed yet.

Check commits locally:
```bash
git log --oneline -n 5
```

Push your current branch:
```bash
git push origin HEAD
```

If you are working on a feature branch, open/create a PR on GitHub after pushing.
