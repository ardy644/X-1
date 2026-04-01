# Experiment No. 11: Business Intelligence Mini Project Report

## 1. Title of the Project
**Coffee Shop Sales Intelligence Dashboard using Data Mining and BI Analytics**

## 2. Abstract
This project analyzes coffee shop sales data from CSV files to find sales trends, customer buying behavior, and peak demand times. The dataset includes transaction date, time, store, product category, product type, size, quantity, unit price, and total bill.

A classification model is used to predict whether a transaction is **High Sales** or **Low Sales**. Results are shown in a simple BI dashboard with KPI cards, trend charts, and category/store analysis.

This helps management improve pricing, inventory, staffing, and promotions.

## 3. Introduction
Business Intelligence (BI) converts raw transaction data into useful insights for better decision-making. In coffee shops, daily transactions can be analyzed to understand demand by product, time, and location.

This project uses BI and data mining on coffee sales CSV data to support practical business decisions.

## 4. Problem Definition in Detail
### Common Problems
- Unclear peak sales hours (staffing issues)
- Poor inventory planning (stockout/wastage)
- No clear view of top products and top stores
- Difficulty planning offers and combos

### Problem Statement
Build a BI solution that:
- Analyzes historical coffee sales data
- Predicts sales class (**High/Low**)
- Visualizes trends and KPIs for management

## 5. Data Mining Task Used & Why
**Task Used: Classification**

### Why Classification?
- Business needs clear categories (High Sales / Low Sales)
- Supports quick daily decisions (stock, staff, offers)
- Works well with available features (hour, month, store, product category, size)

> Future scope: clustering for customer segmentation.

## 6. About the Dataset Used
The coffee sales CSV includes fields such as:
- transaction_id
- transaction_date
- transaction_time
- store_id
- store_location
- product_id
- transaction_qty
- unit_price
- Total_Bill
- product_category
- product_type
- product_detail
- Size
- Month Name
- Day Name
- Hour
- Month
- Day of Week

**Dataset Nature:** Structured, time-series transactional retail data.

## 7. Algorithm Used & Why
**Algorithm Used: Random Forest Classifier**

### Why Random Forest?
- Handles both categorical and numerical features
- Captures non-linear patterns in sales data
- Reduces overfitting compared to one decision tree
- Gives feature importance (helpful for BI insights)

## 8. Preprocessing Techniques
### Data Cleaning
- Removed duplicate transactions
- Handled missing values in size/category/time fields

### Date-Time Transformation
- Converted date and time to datetime format
- Created features: Hour, Day of Week, Month, Weekend flag

### Encoding
- Applied label/one-hot encoding for categorical columns
  (store_location, product_type, Size)

### Feature Engineering
- Created target class:
  - **High_Sales = 1** if Total_Bill > median bill
  - **Low_Sales = 0** otherwise

### Train-Test Split
- 80% training, 20% testing

### Normalization/Scaling
- Applied when needed for numerical stability

## 9. Random Forest Algorithm Steps
1. Input preprocessed dataset with features **X** and target **Y**.
2. Split data into train and test sets.
3. For each tree in the forest:
   - Draw a bootstrap sample from training data
   - Select random subset of features at each split
   - Grow tree using Gini index
4. Combine all tree outputs using majority voting.
5. Predict class: **High Sales** or **Low Sales**.
6. Evaluate with accuracy, precision, recall, F1-score, and confusion matrix.

## 10. Dashboard Components
### KPI Cards
- Total Revenue
- Total Transactions
- Average Bill Value
- Best-Selling Product Category

### Time Analysis
- Sales by Hour (line chart)
- Sales by Day of Week (bar chart)
- Monthly Revenue Trend (line/area chart)

### Product Analysis
- Revenue by Product Category
- Top 10 Product Types

### Store Analysis
- Revenue by Store Location
- Location-wise Transaction Count

### Filters/Slicers
- Month, Store, Product Category, Size, Day Type (Weekday/Weekend)

## 11. Generated Results with Measures
*(Replace with your actual model output; sample format below)*
- Accuracy: **89.4%**
- Precision: **0.88**
- Recall: **0.90**
- F1-score: **0.89**
- ROC-AUC: **0.92**
- Error Rate: **10.6%**

### Interpretation
The model performs well in identifying high-sales transactions, so it is useful for daily operational planning.

## 12. Visualization Techniques Used
- Bar charts (category/store comparison)
- Line charts (sales trend over time)
- Heatmap (Hour × Day sales intensity)
- Pie/Donut chart (category contribution)
- KPI cards (summary metrics)
- Slicers/filters for interactive analysis

**Tools:** Power BI / Tableau / Excel

## 13. BI Decisions Based on Results
- Optimize staffing during peak hours
- Improve inventory for top-selling categories
- Run targeted promotions on low-demand times
- Plan store-specific strategies by location performance
- Improve product mix using demand + margin insights

## 14. Is It Working? How to Test It
Yes — the report structure is complete and ready to use.

You can test your mini project in 3 simple ways:

### A) Data Check (CSV)
1. Open your CSV file.
2. Confirm required columns exist (transaction_date, transaction_time, Total_Bill, product_category, store_location, etc.).
3. Remove blank or invalid rows.

### B) Model Check (Python)
1. Run preprocessing (datetime conversion, encoding, target creation).
2. Train Random Forest with 80/20 split.
3. Check metrics:
   - Accuracy should be reasonable (example: around 0.85+)
   - Precision, Recall, F1 should not be very low
4. If confusion matrix shows both classes predicted properly, model is working.

### C) Dashboard Check (Power BI/Tableau/Excel)
1. Import processed CSV.
2. Build KPI cards: Total Revenue, Total Transactions, Avg Bill.
3. Add charts (hourly trend, day-wise sales, category revenue, store revenue).
4. Apply slicers (Month, Store, Category, Size).
5. If visuals update correctly when slicers change, dashboard is working.

### Final Validation Checklist
- CSV loads without errors
- Model trains without errors
- Metrics are generated
- Dashboard visuals and filters are interactive
- Insights can support staffing, inventory, and promotion decisions
