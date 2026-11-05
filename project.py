import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")
st.title("🛒E-commerce revenue growth analysis")
st.divider()
st.header("📄Executive summary")
st.markdown(""" 
This project presents a comparishion analysis of an **Indian E-Commerce Pricing & Revenue Growth Dataset** containing **30,600 transcation 
records ** and ** 16 business related features.** The dashboard explored sales performance pricing strategies, customer behavior, product demand,
 and regional trends through interactive visualizations. The analysis helps identify revenue-driving factors and supports data-driven business 
 decisions.

### 🎯 Key Objectives
- Analyze sales performance across different product categories and regions.
- Examine the impact of discounts on revenue and units sold.
- Understand customer demographics and purchasing behavior.
- Compare pricing strategies for different brand types.
- Identify high-performing states and sales zones.
- Evaluate the influence of sales events, competition, and inventory pressure.

### 📊 Dataset Highlights
- **30,600** transaction records collected over **36 months**.
- **16 business-related features** including pricing, sales, and customer information.
- Covers multiple **states** and **geographical zones** across India.
- Includes product **categories**, **brand types**, and **sales events**.
- Contains customer demographics such as **age** and **gender**.
- Records **base price**, **discount percentage**, **final price**, **units sold**, and **revenue**.

### 🔍 Key Insights
- Revenue is primarily influenced by **final price**, **units sold**, and promotional discounts.
- Customer purchasing behavior varies across different age groups and genders.
- Sales performance differs significantly among product categories and regions.
- Seasonal sales events contribute to noticeable increases in revenue.
- Competition intensity and inventory pressure affect product sales and pricing decisions.
- Regional analysis helps identify high-growth markets and business opportunities.

### 🚀 Expected Outcomes
- Interactive dashboard for real-time business analysis.
- Identification of high-revenue products and profitable regions.
- Better understanding of customer purchasing patterns.
- Insights into pricing and discount effectiveness.
- Strategic recommendations for improving revenue growth and inventory management.
- Data-driven support for marketing, pricing, and business planning.
""")

st.divider()
st.header("📖 Project Description")

st.subheader("Problem Statement")

st.markdown("""
This project presents a comprehensive analysis of an **Indian E-commerce Pricing & Revenue Growth Dataset** containing **30,600 transaction
records** and **16 business-related features**. The dashboard explores sales performance, pricing strategies, customer behavior,
product demand, and regional trends through interactive visualizations. The analysis helps identify revenue-driving factors and
supports data-driven business decisions.
### 🎯 Key Objectives
- Analyze sales performance across different product categories and regions.
- Examine the impact of discounts on revenue and units sold.
- Understand customer demographics and purchasing behavior.
- Compare pricing strategies for different brand types.
- Identify high-performing states and sales zones.
- Evaluate the influence of sales events, competition, and inventory pressure.

### 📊 Dataset Highlights
- **30,600** transaction records collected over **36 months**.
- **16 business-related features** including pricing, sales, and customer information.
- Covers multiple **states** and **geographical zones** across India.
- Includes product **categories**, **brand types**, and **sales events**.
- Contains customer demographics such as **age** and **gender**.
- Records **base price**, **discount percentage**, **final price**, **units sold**, and **revenue**.

### 🔍 Key Insights
- Revenue is primarily influenced by **final price**, **units sold**, and promotional discounts.
- Customer purchasing behavior varies across different age groups and genders.
- Sales performance differs significantly among product categories and regions.
- Seasonal sales events contribute to noticeable increases in revenue.
- Competition intensity and inventory pressure affect product sales and pricing decisions.
- Regional analysis helps identify high-growth markets and business opportunities.

### 🚀 Expected Outcomes
- Interactive dashboard for real-time business analysis.
- Identification of high-revenue products and profitable regions.
- Better understanding of customer purchasing patterns.
- Insights into pricing and discount effectiveness.
- Strategic recommendations for improving revenue growth and inventory management.
- Data-driven support for marketing, pricing, and business planning.
""")

st.divider()
st.header("📖 Project Description")

st.subheader("Problem Statement")

st.markdown("""
The Indian e-commerce industry is growing rapidly, with businesses continuously competing through pricing strategies, discounts, promotional campaigns, and improved customer experiences. Understanding the factors that influence sales performance and revenue growth is essential for making informed business decisions.

This project analyzes a comprehensive **Indian E-commerce Pricing & Revenue Growth Dataset** to generate data-driven insights that can help:

- **Business Managers:** Optimize pricing strategies and maximize revenue.
- **Marketing Teams:** Evaluate the effectiveness of discounts and promotional campaigns.
- **Sales Analysts:** Identify high-performing products, categories, and regions.
- **Supply Chain Managers:** Monitor inventory pressure and demand fluctuations.
- **Decision Makers:** Make strategic business decisions using interactive visual analytics.
""")

st.subheader("📊 Dataset Overview")

st.markdown("""
The dataset contains **30,600 transaction records** collected over **36 months**, providing detailed information about sales, customers, pricing, and business performance across multiple regions in India.

### Core Business Information
- Order ID and Order Date
- Product Categories
- Brand Type
- State and Zone
- Sales Events

### Customer Information
- Customer Age
- Customer Gender
- Regional Distribution
- Purchasing Trends

### Pricing & Sales Features
- Base Price
- Discount Percentage
- Final Selling Price
- Units Sold
- Revenue Generated

### Business Performance Metrics
- Competition Intensity
- Inventory Pressure
- Revenue Growth Indicators
- Regional Sales Performance
- Category-wise Business Analysis

### Project Objectives
- Analyze revenue and sales performance across different regions.
- Study customer purchasing behavior using demographic information.
- Evaluate the impact of discounts on revenue generation.
- Compare product category performance and brand types.
- Identify top-performing states and sales zones.
- Discover business opportunities through interactive visualizations.

### Expected Business Impact
- Improve pricing and discount strategies.
- Increase overall revenue and profitability.
- Enhance inventory planning and demand forecasting.
- Support data-driven business decisions.
- Provide interactive insights for executives and stakeholders.
""")
# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("indian_ecommerce_pricing_revenue_growth_36_months.csv")

        # Cleaning
        df.drop_duplicates(inplace=True)
        df.reset_index(drop=True, inplace=True)

        return df

    except Exception as e:
        st.error(f"Error loading dataset:\n{e}")
        return None

df = load_data()
df

# MODERN SIDEBAR FILTER

st.sidebar.header("🔍 Filter Data")

# Zone 
selected_zone = st.sidebar.multiselect(
    "🌍 Select Zone",
    options=sorted(df["zone"].unique()),
    default=sorted(df["zone"].unique())
)

#State 
state_options = sorted(
    df[df["zone"].isin(selected_zone)]["state"].unique()
)

selected_state = st.sidebar.multiselect(
    "🏙️ Select State",
    options=state_options,
    default=state_options
)

#  Category 
category_options = sorted(
    df[
        (df["zone"].isin(selected_zone)) &
        (df["state"].isin(selected_state))
    ]["category"].unique()
)

selected_category = st.sidebar.multiselect(
    "🛒 Select Category",
    options=category_options,
    default=category_options
)

#  Brand Type 
brand_options = sorted(
    df[
        (df["zone"].isin(selected_zone)) &
        (df["state"].isin(selected_state)) &
        (df["category"].isin(selected_category))
    ]["brand_type"].unique()
)

selected_brand = st.sidebar.multiselect(
    "🏷️ Select Brand Type",
    options=brand_options,
    default=brand_options
)

#  Gender 
gender_options = sorted(
    df[
        (df["zone"].isin(selected_zone)) &
        (df["state"].isin(selected_state)) &
        (df["category"].isin(selected_category)) &
        (df["brand_type"].isin(selected_brand))
    ]["customer_gender"].unique()
)

selected_gender = st.sidebar.multiselect(
    "👤 Customer Gender",
    options=gender_options,
    default=gender_options
)

#  Age 
age_range = st.sidebar.slider(
    "🎂 Customer Age",
    min_value=int(df["customer_age"].min()),
    max_value=int(df["customer_age"].max()),
    value=(
        int(df["customer_age"].min()),
        int(df["customer_age"].max())
    )
)

# - Apply / Reset 
col1, col2 = st.sidebar.columns(2)

with col1:
    apply = st.button("✅ Apply", use_container_width=True)

with col2:
    reset = st.button("🔄 Reset", use_container_width=True)

#  Filter Data 
filtered_df = df[
    (df["zone"].isin(selected_zone)) &
    (df["state"].isin(selected_state)) &
    (df["category"].isin(selected_category)) &
    (df["brand_type"].isin(selected_brand)) &
    (df["customer_gender"].isin(selected_gender)) &
    (df["customer_age"].between(age_range[0], age_range[1]))
]

# Dataset Overview

st.header("📊 Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Records", f"{df.shape[0]:,}")

with col2:
    st.metric("Total Columns", df.shape[1])

with col3:
    memory = df.memory_usage(deep=True).sum() / (1024**2)
    st.metric("Memory Usage", f"{memory:.2f} MB")

# Tabs

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Column Information",
    "Missing Values",
    "Sample Data",
    "Statistics",
    "Categorical Data",
    "Data Quality"
])

# Tab1 : column information
with tab1:
    st.subheader("📓 column information")

    column_info = pd.DataFrame({
        "Column Name": df.columns,
        "Data Type":df.dtypes.astype(str),
        "Missing values":df.isnull().sum().values,
        "Unique values":df.nunique().values
    })
    st.dataframe(column_info,use_container_width = True)

# Tab2 : Missing values
with tab2:
    st.subheader("📔 Missing Values Report")

    Missing = pd.DataFrame({
        "Missing values":df.isnull().sum(),
        "percentage (%)":round(df.isnull().mean() *100,2)
    })
    st.dataframe(Missing,use_container_width = True)

    if Missing ["Missing values"].sum() ==0:
        st.success("✔ no missing values found in the dataset.")
    else:
        st.warning(
            f"⚠ Total Missing values:{Missing["Missing values"].sum()}"
        )

# Tab3 : Sample data
with tab3:
    st.subheader("📓 Sample Data")

    col1, col2= st.columns(2)
    with col1:
        st.markdown("### First 10 Rows")
        st.dataframe(df.head(10),use_container_width= True)

    with col2:
        st.markdown("### Last 10 Rows")
        st.dataframe(df.tail(10),use_container_width = True)

# Tab4 : Statistics
with tab4:
    st.subheader("📈 statistical Summary")
    st.dataframe(df.describe(),use_container_width = True)

# Tab5 : Categorical Data 
with tab5:
    st.subheader("📋 Categorical Data")
    cat= df.select_dtypes(include="object")
    if cat.empty:
        st.info("no Categorical columns found")
    else:
        st.dataframe(cat.describe(),use_container_width = True)

# Tab6 : Data Quality
with tab6:
    st.subheader("📊 Data Quality Report")
    report= pd.DataFrame({
        "Data Type": df.dtypes.astype(str),
        "Missing values": df.isnull().sum(),
        "Unique values": df.nunique(),
        "Duplicate Rows": [df.duplicated().sum()] + [""] * (len(df.columns) - 1)
    })
st.dataframe(report, use_container_width=True)

# Visualization
st.header("📈 Visualizations")

# Graph 1
category_df = (
    df.groupby("category", as_index=False)["revenue"]
    .sum()
)
fig1 = px.bar(
    category_df,
    x = "category",
    y = "revenue",
    color = "category",
    text_auto= ".2s",
    title= "Revenue by Category"
)
fig1.update_layout(
    template ="plotly_dark",
    xaxis_title="category",
    yaxis_title="revenue (₹)",
    xaxis = dict(showgrid = False),
    yaxis = dict(showgrid = False),
    height = 550
)
st.plotly_chart(fig1, "use_contianer_width= True")
st.markdown("""
### 💰 Key Insights
- Reveals the product categories contributing the most revenue.
- Helps identify high-performing and underperforming categories.
- Supports product portfolio and pricing decisions.

""")
st.divider()

# Graph 2
fig2 = px.line(
    category_df,
    x = "category",
    y = "revenue",
    markers= "True",
    title = "Revenue Trends by Category"
)
fig2.update_layout(
    template = "plotly_dark",
    title_x = 0.5,
    xaxis_title ="category",
    yaxis_title = "revenue",
    height = 550
)
st.plotly_chart(fig2, "use_contianer_width =True")
st.markdown(""" 
### 📈 Key Insights
- Shows the overall revenue trend across different product categories.
- Makes it easy to compare category-wise business performance.
- Highlights categories with consistent revenue growth.
""")
st.divider()

# Graph 3
fig3 = px.pie(
    df,
    names = "category",
    values = "revenue",
    hole = 0.50,
    title = "Revenue Share by Category"
)
fig3.update_layout(
    template = "plotly_dark",
    title_x = 0.5,
    height = 550
)
fig3.update_traces(
    textposition="inside",
    textinfo="percent+label"
)
st.plotly_chart(fig3, "use_contianer_width = True")
st.markdown("""
### 🥧 Key Insights
- The donut chart illustrates the percentage contribution of each product category to the total revenue.
- Categories with larger slices are the primary revenue contributors and play a significant role in business profitability.
- Categories with smaller revenue shares may require improved marketing strategies, pricing optimization, or promotional campaigns.
- A balanced revenue distribution indicates a diversified product portfolio, while a dominant category highlights strong customer demand.
- These insights help businesses prioritize high-performing categories and make informed decisions on inventory management, product expansion, 
and revenue growth.
""")
st.divider()
# Graph 4
fig4 = px.scatter(
    df,
    x = "final_price",
    y = "revenue",
    color = "customer_gender",
    size = "units_sold",
    hover_data = ["category","zone"],
    title = "Revenue vs Final Price"
)
fig4.update_layout(
    template = "plotly_dark",
    title_x = 0.5,
    height = 600
)
st.plotly_chart(fig4, "use_contianer_width = True")
st.markdown("""
### 🎯 Key Insights
- The scatter plot highlights the relationship between **final product price** and **generated revenue**.
- Larger bubbles represent **higher units sold**, making it easy to identify products with strong sales volume.
- Products with **high final prices and high revenue** indicate premium items that contribute significantly to business growth.
- Products with **low prices but large bubbles** suggest that high sales volume can also generate substantial revenue.
- The color distinction between **male and female customers** helps compare purchasing patterns across customer segments.
- Hover information provides additional details such as **category** and **zone**, enabling deeper analysis of product and regional performance.
- The visualization helps identify pricing opportunities, customer preferences, and high-performing products for better business decision-making.
""")
st.divider()

# Graph 5
fig5 = px.box(
    df,
    x = "category",
    y = "final_price",
    color = "category",
    title = "Final Price Distributed by Category"
)
fig5.update_layout(
    template ="plotly_dark",
    title_x = 0.5,
    xaxis_title="Category",
    yaxis_title="Final Price (₹)",
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),
    height=550
)
st.plotly_chart(fig5, use_container_width=True)
st.markdown("""
### 📦 Key Insights
- The box plot compares the **distribution of final product prices** across different categories.
- The **median line** inside each box represents the typical selling price for that category.
- A **wider box** indicates greater variation in product prices, while a narrower box suggests more consistent pricing.
- **Outlier points** highlight products priced significantly higher or lower than the majority, which may represent premium products or 
heavy discounts.
- Categories with **higher median prices** generally consist of premium-priced products, whereas lower median prices indicate budget-friendly
 offerings.
- This visualization helps evaluate **pricing consistency**, identify unusual price variations, and support data-driven pricing strategies
 across product categories.
""")
st.divider()
# Graph 6
fig6 = px.violin(
    df,
    x="category",
    y="final_price",
    color="category",
    title="Final Price Distributed by Category",
    box=True,
    points="outliers",
    color_discrete_sequence=px.colors.qualitative.Set2
)
fig6.update_layout(
    template="plotly_dark",
    title_x=0.5,
    xaxis_title="Category",
    yaxis_title="Final Price (₹)",
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),
    height=550
)
st.plotly_chart(fig6, use_container_width=True)
st.markdown("""
### 🎻 Key Insights
- The violin plot combines a **box plot** with a **density distribution**, providing a deeper understanding of product prices across categories.
- The **width of each violin** represents the concentration of products at different price levels.
- The **embedded box plot** displays the median, quartiles, and overall spread of prices.
- **Outlier points** highlight products priced significantly higher or lower than the majority.
- Categories with **wider violins** indicate greater price variability, while **narrower violins** suggest more consistent pricing.
- The visualization helps identify pricing patterns, detect unusual values, and support strategic pricing decisions.
""")

st.divider()

# Graph 7 - Revenue Distribution by State
fig7 = px.area(
    df,
    x="state",
    y="revenue",
    title="Revenue by State"
)

fig7.update_layout(
    template="plotly_dark",
    title_x=0.5,
    xaxis_title="State",
    yaxis_title="Revenue (₹)",
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),
    height=550
)

st.plotly_chart(fig7, use_container_width=True)
st.markdown("""
### 🌍 Key Insights
- The area chart illustrates the **total revenue generated across different states**.
- States with **higher peaks** contribute the most to overall business revenue and represent key markets.
- Lower-revenue states may indicate opportunities for **targeted marketing, promotional campaigns, or business expansion**.
- Comparing revenue across states helps identify **regional sales performance** and customer demand.
- These insights support **market prioritization**, **resource allocation**, and **strategic business planning**.
""")

st.divider()
# Graph 8
fig8 = px.scatter_3d(
    df,
    x="discount_percent",
    y="units_sold",
    z="customer_age",
    color="category",
    size="revenue",
    title="3D Customer Purchase Analysis"
)
fig8.update_layout(
    template="plotly_dark",
    title_x=0.5,
    height=550,
    scene=dict(
        xaxis_title="Discount (%)",
        yaxis_title="Units Sold",
        zaxis_title="Customer Age"
    )
)
st.plotly_chart(fig8, use_container_width=True)
st.markdown("""
### 🔵 Key Insights
- The 3D scatter plot visualizes the relationship between **Discount Percentage**, **Units Sold**, and **Customer Age**.
- Each point represents a customer transaction, while **bubble size** reflects the generated **Revenue**.
- Different **colors** distinguish product categories, making category-wise sales patterns easy to identify.
- Different **symbols** represent customer gender, enabling demographic comparison.
- Larger bubbles indicate high-revenue transactions, helping identify profitable sales opportunities.
- The visualization supports analysis of how **discount strategies**, **customer age**, and **sales volume** influence overall business
 performance.
""")
st.divider()

# Graph 9 - Revenue Distribution Treemap
fig9 = px.treemap(
    df,
    path=["zone", "state", "category"],
    values="revenue",
    color="revenue",
    title="Revenue Distribution Treemap"
)

fig9.update_layout(
    template="plotly_dark",
    title_x=0.5,
    height=550
)

st.plotly_chart(fig9, use_container_width=True)
st.markdown("""
### 🌳 Key Insights
- The treemap visualizes **revenue contribution** across **zones, states, and product categories** using a hierarchical structure.
- **Larger rectangles** represent higher revenue, allowing quick identification of the most profitable regions and categories.
- **Darker colors** indicate greater revenue values, making high-performing business segments easy to spot.
- The hierarchical layout helps analyze revenue from **Zone → State → Category**, enabling multi-level business insights.
- Smaller rectangles highlight underperforming markets that may benefit from targeted promotions or improved inventory strategies.
- This visualization supports **regional performance analysis**, **resource allocation**, and **strategic business decision-making**.
""")

st.divider()
# Graph 10
fig10 = px.sunburst(
    filtered_df,
    path=["zone", "category", "brand_type"],
    values="units_sold",
    color="zone",
    title="Units Sold Distribution"
)

fig10.update_layout(
    template="plotly_dark",
    title_x=0.5,
    height=550
)

st.plotly_chart(fig10, use_container_width=True)
st.markdown("""
### ☀️ Key Insights
- The Sunburst chart displays the hierarchical distribution of **Units Sold** across **Zones**, **Product Categories**, and **Brand Types**.
- The inner ring represents business **Zones**, followed by **Categories**, and finally **Brand Types**.
- Larger segments indicate higher sales volume, making top-performing regions and products easy to identify.
- The percentage values show each segment's contribution to its parent level, enabling clear hierarchical analysis.
- Hover over any segment to view detailed information about units sold and its parent category.
- This visualization helps identify strong-performing product segments and supports inventory planning and strategic decision-making.
""")

st.divider()
st.header("📌 Business Implications & Recommendations")

# ------------------- For Business Owners -------------------
with st.expander("🛒 For E-commerce Business Owners"):
    st.markdown("""
### Business Recommendations
*1. Pricing Strategy*
- Optimize discounts to maximize sales without reducing profit margins.
- Monitor competitor pricing regularly.
- Use dynamic pricing during festive and seasonal sales.

*2. Inventory Management*
- Maintain sufficient stock for high-demand products.
- Reduce overstocking of slow-moving categories.
- Forecast demand using historical sales trends.

*3. Customer Experience*
- Improve delivery speed and order tracking.
- Provide personalized product recommendations.
- Offer loyalty rewards and cashback programs .
*4. Marketing*
- Focus campaigns on high-revenue states and zones.
- Target different customer age groups with personalized offers.
- Increase customer retention through email and app notifications.
""")

# ------------------- For Investors -------------------
with st.expander("💰 For Investors & Entrepreneurs"):
    st.markdown("""
### Investment Insights

- Invest in product categories showing consistent revenue growth.
- Expand operations in high-performing regions.
- Analyze customer demographics before entering new markets.
- Focus on businesses with stable pricing and strong customer retention.
- Digital marketing and AI-based recommendation systems can increase ROI.
""")

# ------------------- For Data Analysts -------------------
with st.expander("📊 For Market Researchers & Analysts"):
    st.markdown("""
### Research Insights

#### 1. Customer Behavior
- Discounted products generally attract higher sales volume.
- Purchasing patterns vary across age groups and regions.
- Customer preferences differ by product category.

#### 2. Sales Trends
- Revenue varies significantly across states and zones.
- Seasonal promotions improve overall sales performance.
- Certain categories consistently generate higher revenue.

#### 3. Predictive Insights
- Historical revenue can help forecast future demand.
- Inventory levels influence sales performance.
- Pricing strategy has a direct impact on profitability.

#### 4. Future Outlook
- AI-driven recommendations can improve customer engagement.
- Personalized marketing will continue driving revenue growth.
- Data-driven decision making enhances long-term business performance.
""")
st.markdown("---")
st.header("📌 Project Conclusion & Key Insights")

st.subheader("📊 Data Analysis Summary")

st.markdown("""
This comprehensive analysis of the *Indian E-commerce Pricing & Revenue Growth* dataset provides valuable insights into customer purchasing behavior, pricing strategies, sales performance, and regional business trends.

Through multiple interactive visualizations and statistical analysis, important patterns have been identified that can help businesses improve revenue, optimize pricing, and enhance customer satisfaction.
""")
st.subheader("🔍 Major Findings & Insights")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
### 🌍 Sales Performance

- High-revenue states contribute significantly to overall business growth.
- Different zones show varying sales performance and customer demand.
- Regional purchasing behavior influences revenue generation.
- Business expansion should prioritize high-performing markets.

### 🛍️ Product Categories

- Certain product categories consistently generate higher revenue.
- Discounts improve sales volume for selected categories.
- Inventory optimization is essential for slow-moving products.
- Category-wise pricing impacts profitability.
""")

with col2:
    st.markdown("""
### 👥 Customer Insights

- Customer age influences purchasing behavior.
- Male and female customers show different buying preferences.
- Repeat customers contribute to stable revenue growth.
- Personalized offers can improve customer engagement.

### 💰 Pricing Strategy

- Moderate discounts generally maximize revenue.
- Excessive discounts reduce profit margins.
- Dynamic pricing improves competitiveness.
- Monitoring pricing trends supports better business decisions.
""")
st.subheader("🚀 Overall Conclusion")

st.success("""
The dashboard demonstrates how data analytics can support strategic decision-making in e-commerce. By analyzing customer demographics,
pricing strategies, sales trends, regional performance, and product categories, businesses can improve operational efficiency, increase 
profitability, and enhance customer satisfaction. The insights generated through this dashboard provide a strong foundation for future
sales forecasting and business growth.
""")
st.markdown("""
---
<div style="text-align:center;">

<h4>🛍️ E-Commerce Revenue Growth Analysis</h4>

<p>Developed by <b>Anamika Kaur</b></p>

<p>Python | Pandas | Plotly | Streamlit</p>

<p>© 2026 All Rights Reserved</p>

</div>
""", unsafe_allow_html=True)










