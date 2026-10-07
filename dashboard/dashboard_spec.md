# Dashboard Specification

## Design direction
Modern recruiter-facing BI dashboard inspired by polished SaaS analytics products: dark navy canvas, blue/cyan/purple accents, glass-like panels, strong spacing, rounded cards, restrained typography, and responsive behavior.

## Implemented layout
1. Persistent left sidebar with dashboard sections
2. Top search/profile bar
3. Dataset/date context header
4. Five KPI cards
5. Sales & Profit monthly trend
6. Sales and Profit by Category
7. Sales by Region
8. Top Products by Sales
9. Discount-band Profitability
10. Evidence-based Key Insights strip

## KPIs
- Total Sales
- Total Profit
- Profit Margin
- Total Orders
- Average Sales per Order

## Data behavior
All displayed figures are derived from the executed Orders sheet of sample_-_superstore.xlsx.
The dashboard does not embed the raw workbook. It embeds derived aggregates required for the visualizations.

## Technical implementation
- HTML/CSS/JavaScript
- Chart.js
- Responsive CSS breakpoints
- No backend required for the dashboard page

## Design principles
- One business question per visual.
- Strong visual hierarchy.
- Consistent currency and percentage formatting.
- Clear chart titles and subtitles.
- Evidence-based insight cards.
- Avoid fabricated comparisons or unsupported causal claims.
- Preserve the documented future-date quality warning.

The implemented dashboard is dashboard/index.html.