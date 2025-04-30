# --- IMPORTS ---
import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet
from prophet.plot import plot_plotly
from PIL import Image
import os
import base64
import plotly.graph_objects as go

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Coffee Shop Analytics Dashboard",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SIDEBAR --- 
# --- SIDEBAR ---
with st.sidebar:
    # Logo and Branding
    st.image("logo.png", use_container_width=True)
    st.markdown("""
    <h2 style='color: #3E2723; margin-bottom: 0;'>Borcelle</h2>
    <p style='color: #6D4C41; margin-top: 0; font-style: italic;'>Artisan Coffee Since 2010</p>
    """, unsafe_allow_html=True)
    
    # Divider
    st.markdown("<hr style='border: 0.5px solid #D7CCC8; margin: 1.5rem 0;'>", unsafe_allow_html=True)
    
    # Navigation
    selected_page = st.radio(
        "MENU",
        options=["Sales Dashboard", "About"],
        index=0,
        label_visibility="collapsed"
    )
    
    # Divider
    st.markdown("<hr style='border: 0.5px solid #D7CCC8; margin: 1.5rem 0;'>", unsafe_allow_html=True)
    
    # Professional Contact Info (Left-Aligned)
    st.markdown("""
    <div style='font-family: "sans-serif" , Arial; color: #3E2723;'>
        <p style='margin-bottom: 12px;'>
            <span style='color: #5D4037;'>📍</span>123 Coffee Street<br>
            <span style='margin-left: 24px;'>Portland, OR 97201</span>
        </p>
        <p style='margin-bottom: 12px;'>
            <span style='color: #5D4037;'>☎ </span>(503) 555-0199
        </p>
        <p style='margin-bottom: 8px;'>
            <span style='color: #5D4037;'>🕒 </span>Mon-Fri: 6am-8pm
        </p>
        <p>
            <span style='margin-left: 24px;'>Sat-Sun: 7am-9pm</span>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Social Media Icons (Left-Aligned)
    st.markdown("""
    <div style='margin-top: 20px; text-align: left;'>
        <a href="#" style='margin-left: 12px'><img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" width="22"></a>
        <a href="#" style='margin-left: 12px'><img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" width="22"></a>
        <a href="#" style='margin-left: 12px'><img src="https://cdn-icons-png.flaticon.com/512/1384/1384053.png" width="22"></a>
    </div>
    """, unsafe_allow_html=True)

# --- LOAD DATA ---
@st.cache_data(ttl=3600)  # Cache data for 1 hour
def load_data():
    try:
        df = pd.read_csv(
            "cleaned_coffee_shop_data.csv",
            parse_dates=['transaction_date'],
            date_parser=lambda x: pd.to_datetime(x, format='mixed')
        )
        df['transaction_hour'] = pd.to_datetime(df['transaction_time'], format='%H:%M:%S').dt.hour
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return pd.DataFrame()

filtered_df = load_data()




# --- ABOUT PAGE ---
if selected_page == "About":
    st.title("About Our Cafe")
    st.markdown("---")
    
    # Header with image
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("jason-leung-poI7DelFiVA-unsplash.jpg", use_container_width=True, caption="Our charming cafe exterior")
    with col2:
        st.markdown("""
        ## The Art of Coffee Since 2010
        
        We're passionate about crafting the perfect cup of coffee while creating 
        a warm, welcoming space for our community. Our beans are ethically sourced 
        from sustainable farms around the world, roasted in-house to perfection.
        """)
    
    st.markdown("---")
    
    # Our Story
    st.header("Our Story")
    st.markdown("""
    Founded in 2010 by coffee enthusiasts Sarah Johnson and Michael Chen, our cafe began 
    as a small corner shop with a big dream. Today, we've grown to multiple locations 
    while maintaining our commitment to quality and community.
    """)
    
    # Timeline
    with st.container(border=True):
        st.markdown("""
        <style>
        .timeline {
            position: relative;
            max-width: 100%;
            margin: 0 auto;
        }
        .timeline::after {
            content: '';
            position: absolute;
            width: 2px;
            background-color: #4B9CD3;
            top: 0;
            bottom: 0;
            left: 50%;
            margin-left: -1px;
        }
        .timeline-item {
            padding: 10px 40px;
            position: relative;
            width: 50%;
            box-sizing: border-box;
        }
        .timeline-item::after {
            content: '';
            position: absolute;
            width: 15px;
            height: 15px;
            background-color: white;
            border: 3px solid #4B9CD3;
            border-radius: 50%;
            top: 15px;
            z-index: 1;
        }
        .left {
            left: 0;
            text-align: right;
        }
        .right {
            left: 50%;
            text-align: left;
        }
        .left::after {
            right: -10px;
        }
        .right::after {
            left: -10px;
        }
        .timeline-content {
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        </style>
        
        <div class="timeline">
            <div class="timeline-item left">
                <div class="timeline-content">
                    <h4>2010</h4>
                    <p>First location opens in downtown</p>
                </div>
            </div>
            <div class="timeline-item right">
                <div class="timeline-content">
                    <h4>2014</h4>
                    <p>Won "Best Local Coffee Shop" award</p>
                </div>
            </div>
            <div class="timeline-item left">
                <div class="timeline-content">
                    <h4>2018</h4>
                    <p>Expanded to three locations</p>
                </div>
            </div>
            <div class="timeline-item right">
                <div class="timeline-content">
                    <h4>2022</h4>
                    <p>Launched our sustainability initiative</p>
                </div>
            </div>
            <div class="timeline-item left">
                <div class="timeline-content">
                    <h4>2023</h4>
                    <p>Served our 1 millionth customer</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Team Section
 
    st.header("Meet Our Team")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container(border=True):
            st.image("Owner.jpeg", use_container_width=True)
            st.subheader("Saad Khan")
            st.markdown("""
            **Co-Founder & CEO**  
            Coffee connoisseur with 15+ years experience  
            ✉️ saad_khan@cafe.com
            """)
    
    with col2:
        with st.container(border=True):
            st.image("oguz-yagiz-kara-MZf0mI14RI0-unsplash.jpg", use_container_width=True)
            st.subheader("Yasir raza")
            st.markdown("""
            **Co-Founder & Head Roaster**  
            Master roaster and barista champion  
            ✉️ yasir_raza@cafe.com
            """)
    
    with col3:
        with st.container(border=True):
            st.image("vicky-hladynets-C8Ta0gwPbQg-unsplash.jpg", use_container_width=True)
            st.subheader("Vicky Hladyent")
            st.markdown("""
            **Operations Manager**  
            Keeps everything running smoothly  
            ✉️ VickyHladyent@cafe.com
            """)
    
    # Values Section
    st.markdown("---")
    st.header("Our Values")
    
    values = [
        {"icon": "🌱", "title": "Sustainability", "desc": "Ethical sourcing, composting, and recycling programs."},
        {"icon": "❤️", "title": "Community", "desc": "Supporting local artists and schools."},
        {"icon": "✨", "title": "Quality", "desc": "Never compromising from bean to cup."},
    ]
    
    cols = st.columns(3)
    for i, value in enumerate(values):
        with cols[i]:
            with st.container(border=True, height=150):  # Reduced height
                st.markdown(f"#### {value['icon']} {value['title']}")
                st.caption(value['desc'])
    
    # Contact Info
    st.markdown("---")
    st.header("Visit Us")
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True, height=200):
            st.markdown("""
            **Main Location**  
            📍 123 Coffee Street  
            Portland, OR 97201  
            
            **Hours:**  
            🕒 Mon-Fri: 6am - 8pm  
            🕒 Sat-Sun: 7am - 9pm
            """)
    
    with col2:
        with st.container(border=True , height=200):
            st.markdown("""
            **Contact Us**  
            📞 (503) 555-0199  
            ✉️ info@cafe.com  
            
            **Follow Us**  
            📱 [Instagram](#) | [Twitter](#) | [Facebook](#)
            """)
    
    # Map
    st.map(pd.DataFrame({
        'lat': [45.523064],
        'lon': [-122.676483],
        'name': ['Main Cafe Location']
    }), zoom=14, use_container_width=True)
    
    st.markdown("---")
    st.caption("© 2023 Coffee Shop Name. All rights reserved.")


# --- SALES DASHBOARD ---
elif selected_page == "Sales Dashboard":
    # Dashboard Header
    st.title("☕ Coffee Shop Performance Dashboard")
    st.caption("""
        Real-time analytics and insights for your coffee shop business. 
        Last updated: {:%Y-%m-%d %H:%M}
    """.format(pd.Timestamp.now()))
    
    with st.expander("🔍 Quick Filters", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            locations = st.multiselect(
                "Select Locations",
                options=filtered_df['store_location'].unique(),
                default=filtered_df['store_location'].unique(),
                help="Filter by store locations"
            )
        with col2:
            categories = st.multiselect(
                "Select Categories",
                options=filtered_df['product_category'].unique(),
                default=filtered_df['product_category'].unique(),
                help="Filter by product categories"
            )
        
        # Apply filters
        filtered_df = filtered_df[
            filtered_df['store_location'].isin(locations) &
            filtered_df['product_category'].isin(categories)
        ]
    
    st.markdown("---")
    
    # --- METRICS ---
    st.subheader("📈 Performance Overview")
    
    # Calculate metrics
    if not filtered_df.empty:
        total_sales = filtered_df['total_sales'].sum()
        avg_daily_sales = filtered_df.groupby('transaction_date')['total_sales'].sum().mean()
        last_month_sales = filtered_df[
            filtered_df['transaction_date'] > 
            (filtered_df['transaction_date'].max() - pd.DateOffset(months=1))
        ]['total_sales'].sum()
        transaction_count = len(filtered_df)
        avg_transaction_value = total_sales / transaction_count if transaction_count > 0 else 0
    else:
        total_sales = avg_daily_sales = last_month_sales = transaction_count = avg_transaction_value = 0
    
    # Create metrics cards
    col1, col2, col3, col4 = st.columns(4)
    
    def create_metric_card(title, value, icon, delta=None, help_text=None):
        delta_color = "normal"
        if delta is not None:
            delta_color = "inverse" if delta < 0 else "normal"
        
        with st.container(border=True):
            st.markdown(f"**{icon} {title}**")
            if help_text:
                st.caption(help_text)
            st.metric(
                label="",
                value=f"€{value:,.2f}" if isinstance(value, (int, float)) else f"{value:,}",
                delta=f"{delta:.1f}%" if delta is not None else None,
                delta_color=delta_color
            )
    
    with col1:
        create_metric_card(
            "Total Sales",
            total_sales,
            "💰",
            help_text="Sum of all transactions"
        )
    
    with col2:
        create_metric_card(
            "Avg Daily Sales",
            avg_daily_sales,
            "📅",
            help_text="Average daily revenue"
        )
    
    with col3:
        create_metric_card(
            "30-Day Sales",
            last_month_sales,
            "🔄",
            help_text="Recent performance"
        )
    
    with col4:
        create_metric_card(
            "Avg Transaction",
            avg_transaction_value,
            "🛒",
            help_text="Average order value"
        )
    
    st.divider()
    
   
    # --- SALES TRENDS SECTION ---
    st.subheader("📈 Sales Trend Analysis")
    st.caption("Explore sales patterns across different time periods")

    # Create time-based aggregations
    sales_daily = filtered_df.groupby('transaction_date')['total_sales'].sum().reset_index()
    sales_daily['transaction_date'] = pd.to_datetime(sales_daily['transaction_date'])

    # Calculate aggregations
    sales_biweekly = sales_daily.resample('2W', on='transaction_date').sum().reset_index()
    sales_monthly = sales_daily.resample('M', on='transaction_date').sum().reset_index()
    sales_quarterly = sales_daily.resample('Q', on='transaction_date').sum().reset_index()

    # Add interactive period selector
    period = st.radio(
        "Select Analysis Period:",
        options=["Bi-Weekly", "Monthly", "Quarterly"],
        horizontal=True,
        index=1,
        help="Choose the time aggregation for sales analysis"
    )

    # Create tabs for different visualization types
    tab1, tab2 = st.tabs(["📊 Trend Analysis", "🔍 Comparative View"])

    with tab1:
        # Main trend visualization based on selected period
        if period == "Bi-Weekly":
            data = sales_biweekly
            color = "#4B9CD3"
            title = "Bi-Weekly Sales Trend"
        elif period == "Monthly":
            data = sales_monthly
            color = "#636EFA"
            title = "Monthly Sales Performance"
        else:
            data = sales_quarterly
            color = "#FF7F50"
            title = "Quarterly Sales Overview"
        
        fig = px.area(
            data,
            x='transaction_date',
            y='total_sales',
            title=f"<b>{title}</b>",
            template='plotly_white',
            color_discrete_sequence=[color],
            labels={
                'transaction_date': 'Date',
                'total_sales': 'Total Sales (€)'
            }
        )
        
        # Enhanced chart styling
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            hovermode='x unified',
            margin={'t': 60},
            title_x=0.05,
            xaxis_title="Date",
            yaxis_title="Total Sales (€)",
            height=450
        )
        
        fig.update_traces(
            fill='tozeroy',
            line=dict(width=2.5),
            hovertemplate="<b>%{x|%b %d, %Y}</b><br>€%{y:,.2f}"
        )
        
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        # Comparative view of all time periods
        st.markdown("### Comparative Sales Trends")
        
        # Create a single figure with all time aggregations
        fig = go.Figure()
        
        # Add traces for each time period
        fig.add_trace(go.Scatter(
            x=sales_biweekly['transaction_date'],
            y=sales_biweekly['total_sales'],
            name='Bi-Weekly',
            line=dict(color='#4B9CD3', width=2),
            hovertemplate="Bi-Weekly: €%{y:,.2f}<extra></extra>"
        ))
        
        fig.add_trace(go.Scatter(
            x=sales_monthly['transaction_date'],
            y=sales_monthly['total_sales'],
            name='Monthly',
            line=dict(color='#636EFA', width=3),
            hovertemplate="Monthly: €%{y:,.2f}<extra></extra>"
        ))
        
        fig.add_trace(go.Scatter(
            x=sales_quarterly['transaction_date'],
            y=sales_quarterly['total_sales'],
            name='Quarterly',
            line=dict(color='#FF7F50', width=4),
            hovertemplate="Quarterly: €%{y:,.2f}<extra></extra>"
        ))
        
        # Style the comparative chart
        fig.update_layout(
            title="<b>Sales Trends Comparison</b>",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            hovermode='x unified',
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            margin={'t': 60},
            height=450,
            xaxis_title="Date",
            yaxis_title="Total Sales (€)"
        )
        
        st.plotly_chart(fig, use_container_width=True)

    # Add a metrics row below the charts
    st.markdown("### 📊 Key Period Metrics")
    col1, col2, col3 = st.columns(3)

    with col1:
        delta = (sales_biweekly['total_sales'].iloc[-1] - sales_biweekly['total_sales'].iloc[-2]) / sales_biweekly['total_sales'].iloc[-2] * 100
        st.metric(
            label="Last Bi-Weekly Period",
            value=f"€{sales_biweekly['total_sales'].iloc[-1]:,.2f}",
            delta=f"{delta:.1f}%"
        )

    with col2:
        delta = (sales_monthly['total_sales'].iloc[-1] - sales_monthly['total_sales'].iloc[-2]) / sales_monthly['total_sales'].iloc[-2] * 100
        st.metric(
            label="Current Month",
            value=f"€{sales_monthly['total_sales'].iloc[-1]:,.2f}",
            delta=f"{delta:.1f}%"
        )

    with col3:
        delta = (sales_quarterly['total_sales'].iloc[-1] - sales_quarterly['total_sales'].iloc[-2]) / sales_quarterly['total_sales'].iloc[-2] * 100
        st.metric(
            label="Current Quarter",
            value=f"€{sales_quarterly['total_sales'].iloc[-1]:,.2f}",
            delta=f"{delta:.1f}%"
        )

    st.divider()

    # --- CATEGORY SALES ANALYSIS ---
    st.subheader("📊 Category Performance Analysis")
    st.caption("Analyze sales performance by product categories and locations")

    # Create a container for filters with subtle border
    with st.container(border=True):
        col1, col2, col3 = st.columns([1.5, 2, 2])
        
        with col1:
            viz_type = st.radio(
                "**Chart Type**",
                options=["Bar Chart", "Pie Chart"],
                horizontal=True,
                index=0,
                help="Select visualization type for category performance"
            )
        
        with col2:
            categories = filtered_df['product_category'].unique()
            selected_categories = st.multiselect(
                "**Select Categories**",
                options=categories,
                default=categories[:2] if len(categories) > 1 else categories,
                help="Choose one or more product categories to analyze"
            )
        
        with col3:
            locations = ['All Locations'] + sorted(filtered_df['store_location'].unique())
            selected_location = st.selectbox(
                "**Filter by Location**",
                options=locations,
                index=0,
                help="Filter results by specific store location"
            )

    # Add space between filters and chart
    st.write("")  # Vertical spacer

    # Filter the data based on selections
    if selected_categories:
        # Apply filters
        if selected_location == 'All Locations':
            filtered_data = filtered_df[filtered_df['product_category'].isin(selected_categories)]
        else:
            filtered_data = filtered_df[
                (filtered_df['product_category'].isin(selected_categories)) & 
                (filtered_df['store_location'] == selected_location)
            ]
        
        if not filtered_data.empty:
            # Prepare data for visualization
            sales_data = filtered_data.groupby(['product_category', 'product_type'])['total_sales'].sum().reset_index()
            
            # Visualization switch
            if viz_type == "Bar Chart":
                fig = px.bar(
                    sales_data,
                    x='product_type',
                    y='total_sales',
                    color='product_category',
                    title=f"<b>Sales by Product Type</b><br><sub>{selected_location} | {len(selected_categories)} categories selected</sub>",
                    barmode='group',
                    text_auto='.2s',
                    color_discrete_sequence=px.colors.qualitative.Pastel,
                    labels={
                        'product_type': 'Product Type',
                        'total_sales': 'Total Sales (€)',
                        'product_category': 'Category'
                    },
                    height=500
                )
                
                # Enhance bar chart styling
                fig.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    xaxis={'categoryorder': 'total descending'},
                    hovermode='x unified',
                    margin={'t': 80},
                    title_x=0.05
                )
                fig.update_traces(
                    marker_line_width=0.5,
                    marker_line_color='white',
                    textfont_size=12,
                    textangle=0,
                    textposition='outside'
                )
                
            else:  # Pie Chart
                pie_data = sales_data.groupby('product_category')['total_sales'].sum().reset_index()
                fig = px.pie(
                    pie_data,
                    names='product_category',
                    values='total_sales',
                    title=f"<b>Sales Distribution</b><br><sub>{selected_location} | {len(selected_categories)} categories selected</sub>",
                    hole=0.35,
                    color_discrete_sequence=px.colors.qualitative.Pastel,
                    height=500
                )
                
                # Enhance pie chart styling
                fig.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    margin={'t': 80},
                    title_x=0.25,
                    legend=dict(
                        orientation="h",
                        yanchor="bottom",
                        y=-0.2,
                        xanchor="center",
                        x=0.5
                    )
                )
                fig.update_traces(
                    textposition='inside',
                    textinfo='percent+label',
                    insidetextorientation='radial',
                    marker=dict(line=dict(color='white', width=1))
                )
            
            # Display the chart with some top margin
            st.plotly_chart(fig, use_container_width=True, theme="streamlit")
            
        else:
            # No data fallback
            st.warning("⚠️ No sales data available for the selected filters")
            st.image("https://cdn-icons-png.flaticon.com/512/4076/4076478.png", width=150)
            st.markdown("Try adjusting your category or location filters")
            
    else:
        # Default view when no categories selected - show top products
        st.info("ℹ️ Showing top products across all categories")
        
        if selected_location == 'All Locations':
            top_products = filtered_df
        else:
            top_products = filtered_df[filtered_df['store_location'] == selected_location]
        
        top5 = top_products.groupby('product_detail')['total_sales'].sum().nlargest(5).reset_index()
        
        # Create a styled bar chart for top products
        fig = px.bar(
            top5,
            x='product_detail',
            y='total_sales',
            title=f"<b>Top 5 Products</b><br><sub>{selected_location}</sub>",
            text_auto='.2s',
            color='total_sales',
            color_continuous_scale='tealrose',
            labels={
                'product_detail': 'Product',
                'total_sales': 'Total Sales (€)'
            },
            height=450
        )
        
        # Style the top products chart
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis={'categoryorder': 'total descending'},
            margin={'t': 80},
            title_x=0.25,
            coloraxis_showscale=False
        )
        fig.update_traces(
            marker_line_width=0.5,
            marker_line_color='white',
            textfont_size=12,
            textposition='outside'
        )
        
        st.plotly_chart(fig, use_container_width=True, theme="streamlit")

    # Add a subtle divider with some spacing
    st.divider()

    # --- LOCATION PERFORMANCE DRILL-DOWN ---
    st.subheader("📍 Location Performance Analysis")
    st.caption("Deep dive into individual store performance metrics")

    # Create filter row with location and date range
    col1, col2 = st.columns([2, 3])

    with col1:
        # Location selector with search functionality
        location_options = sorted(filtered_df['store_location'].unique())
        selected_location = st.selectbox(
            "Select Store Location",
            options=location_options,
            index=0,
            help="Choose a location to analyze its performance"
        )

    with col2:
        # Date range slider in the same row
        if not filtered_df.empty:
            min_date = filtered_df['transaction_date'].min().date()
            max_date = filtered_df['transaction_date'].max().date()
            
            # Convert dates to timestamps for slider
            min_ts = pd.Timestamp(min_date).timestamp()
            max_ts = pd.Timestamp(max_date).timestamp()
            
            selected_range = st.slider(
                "Date Range",
                min_value=min_date,
                max_value=max_date,
                value=(min_date, max_date),
                format="YYYY-MM-DD",
                help="Drag to select date range for analysis"
            )

    # Filter data for selected location and date range
    loc_df = filtered_df[filtered_df['store_location'] == selected_location]
    if len(selected_range) == 2:
        loc_df = loc_df[
            (loc_df['transaction_date'].dt.date >= selected_range[0]) &
            (loc_df['transaction_date'].dt.date <= selected_range[1])
        ]

    # Calculate KPIs
    total_sales_loc = loc_df['total_sales'].sum()
    transaction_count = len(loc_df)
    avg_transaction = loc_df['total_sales'].mean()
    busiest_hour = loc_df['hour'].value_counts().idxmax()
    busiest_hour_count = loc_df['hour'].value_counts().max()

    # Get top category
    top_category_df = loc_df.groupby('product_category')['transaction_qty'].sum().reset_index()
    if not top_category_df.empty:
        top_category_df = top_category_df.sort_values('transaction_qty', ascending=False)
        best_category = top_category_df.iloc[0]['product_category']
        best_qty = top_category_df.iloc[0]['transaction_qty']
    else:
        best_category = "N/A"
        best_qty = 0

    # Create KPI cards in a 2x2 grid
    st.markdown("### 📊 Location KPIs")
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.metric(
            label="Total Sales",
            value=f"€{total_sales_loc:,.2f}",
            help="Gross revenue for selected period"
        )

    with kpi2:
        st.metric(
            label="Transactions",
            value=f"{transaction_count:,}",
            help="Total number of orders"
        )

    with kpi3:
        st.metric(
            label="Avg. Order Value",
            value=f"€{avg_transaction:,.2f}",
            help="Average spend per transaction"
        )

    with kpi4:
        st.metric(
            label="Busiest Hour",
            value=f"{busiest_hour}:00",
            delta=f"{busiest_hour_count} transactions",
            help="Peak business hour with transaction count"
        )

    # Top category performance
    st.markdown("### 🏆 Top Performing Category")
    col1, col2 = st.columns([1, 3])

    with col1:
        st.metric(
            label=best_category,
            value=f"{best_qty:,} units sold",
            help="Best selling product category"
        )

    with col2:
        category_sales = loc_df.groupby('product_category')['total_sales'].sum().sort_values(ascending=False)
        fig = px.pie(
            names=category_sales.index,
            values=category_sales.values,
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel,
            height=300
        )
        fig.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig, use_container_width=True)

    # --- SALES TREND VISUALIZATION ---
    st.markdown("### 📈 Sales Trend Analysis")
    st.caption(f"Analyzing patterns for {selected_location} from {selected_range[0].strftime('%b %d, %Y')} to {selected_range[1].strftime('%b %d, %Y')}")

    # Create tabs with different visualization approaches
    tab1, tab2, tab3 = st.tabs(["🌐 Geospatial", "⏳ Temporal", "📦 Category Mix"])

    with tab1:
        # Heatmap of sales by day of week vs hour
        st.markdown("#### 🗓️⏰ Day/Hour Heatmap")
        heatmap_data = loc_df.copy()
        heatmap_data['day_of_week'] = heatmap_data['transaction_date'].dt.day_name()
        heatmap_data['hour'] = heatmap_data['transaction_hour']
        
        heatmap_df = heatmap_data.groupby(['day_of_week', 'hour'])['total_sales'].sum().unstack()
        
        # Reorder days
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        heatmap_df = heatmap_df.reindex(days)
        
        fig = px.imshow(
            heatmap_df,
            labels=dict(x="Hour of Day", y="Day of Week", color="Sales (€)"),
            aspect="auto",
            color_continuous_scale='Viridis',
            height=500
        )
        fig.update_xaxes(side="top")
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        # Combined temporal view with line and area charts
        st.markdown("#### 📅 Time Series Patterns")
        
        col1, col2 = st.columns(2)
        with col1:
            time_group = st.radio(
                "Time Period:",
                ["Daily", "Weekly", "Monthly"],
                index=2,
                horizontal=True
            )
        
        with col2:
            metric = st.radio(
                "Metric:",
                ["Revenue", "Transactions"],
                index=0,
                horizontal=True
            )
        
        # Prepare temporal data
        freq_map = {"Daily": "D", "Weekly": "W", "Monthly": "M"}
        temp_df = loc_df.set_index('transaction_date')
        if metric == "Revenue":
            ts_data = temp_df.resample(freq_map[time_group])['total_sales'].sum()
        else:
            ts_data = temp_df.resample(freq_map[time_group])['transaction_id'].count()
        
        # Create dual-axis chart
        fig = go.Figure()
        
        # Main line/area trace
        if time_group == "Daily":
            fig.add_trace(go.Scatter(
                x=ts_data.index,
                y=ts_data.values,
                fill='tozeroy',
                mode='lines',
                name=metric,
                line=dict(color='#4B9CD3', width=2),
                hovertemplate=f"<b>%{{x|%b %d}}</b><br>{metric}: %{{y:,}}<extra></extra>"
            ))
        else:
            fig.add_trace(go.Bar(
                x=ts_data.index,
                y=ts_data.values,
                name=metric,
                marker_color='#4B9CD3',
                hovertemplate=f"<b>%{{x|%b %Y}}</b><br>{metric}: %{{y:,}}<extra></extra>"
            ))
        
        # 7-day moving average if showing daily data
        if time_group == "Daily":
            moving_avg = ts_data.rolling(7).mean()
            fig.add_trace(go.Scatter(
                x=ts_data.index,
                y=moving_avg.values,
                mode='lines',
                name='7-Day Avg',
                line=dict(color='#FF7F50', width=3, dash='dot'),
                hovertemplate="<b>7-Day Avg</b><br>%{y:,.0f}<extra></extra>"
            ))
        
        fig.update_layout(
            title=f"<b>{time_group} {metric} Trend</b>",
            hovermode='x unified',
            plot_bgcolor='rgba(0,0,0,0)',
            height=500,
            xaxis_title="Date",
            yaxis_title=metric,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        # Radial and small multiples view
        st.markdown("#### 🎯 Category Performance")
        
        # Prepare category data
        cat_df = loc_df.groupby('product_category').agg({
            'total_sales': 'sum',
            'transaction_qty': 'sum',
            'transaction_id': 'count'
        }).reset_index()
        
        # Create radial bar chart
        fig = px.bar_polar(
            cat_df,
            r='total_sales',
            theta='product_category',
            color='product_category',
            template='plotly_white',
            color_discrete_sequence=px.colors.qualitative.Pastel,
            height=500
        )
        fig.update_layout(
            title="<b>Revenue by Category</b>",
            polar=dict(
                radialaxis=dict(visible=True, showticklabels=False),
                angularaxis=dict(showticklabels=True)
            ),
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    # Modern divider
    st.markdown("""<hr style="height:1px; border:none; background: linear-gradient(90deg, transparent, #4B9CD3, transparent); margin: 2rem 0;"/>""", 
                unsafe_allow_html=True)

    # Create pie for weekend / weekdays 
    df = filtered_df.copy()
    df['day_of_week'] = df['transaction_date'].dt.dayofweek
    df['day_type'] = df['day_of_week'].apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')
    filtered_df['transaction_time'] = pd.to_datetime(filtered_df['transaction_time'], errors='coerce')
    filtered_df['transaction_hour'] = filtered_df['transaction_time'].dt.hour
    sales_by_hour = filtered_df.groupby('transaction_hour')['total_sales'].sum().reset_index()

    # Group sales
    sales_by_daytype = df.groupby('day_type')['total_sales'].sum().reindex(['Weekday', 'Weekend']).fillna(0)

    # --- PEAK SALES ANALYSIS ---
    st.markdown("### 🌅 Peak Sales Periods")
    st.caption("Identifying high and low traffic hours to optimize staffing and operations")

    # Create two columns for different visual perspectives
    col1, col2 = st.columns([2, 1])

    with col1:
        # Circular Gauge for Peak Hour Performance
        peak_hour = sales_by_hour.loc[sales_by_hour['total_sales'].idxmax(), 'transaction_hour']
        peak_sales = sales_by_hour['total_sales'].max()
        avg_sales = sales_by_hour['total_sales'].mean()
        efficiency_ratio = (peak_sales / avg_sales - 1) * 100  # Percentage above average
        
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = peak_hour,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': f"Peak Hour: {peak_hour}:00", 'font': {'size': 20}},
            delta = {'reference': 12, 'increasing': {'color': "#4B9CD3"}},
            gauge = {
                'axis': {'range': [0, 23], 'tickwidth': 1, 'tickcolor': "#2b2b2b"},
                'bar': {'color': "#FF7F50"},
                'steps': [
                    {'range': [0, 8], 'color': "#f0f0f0"},
                    {'range': [8, 16], 'color': "#e6e6e6"},
                    {'range': [16, 23], 'color': "#dcdcdc"}],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': peak_hour}
            }
        ))
        
        fig_gauge.update_layout(
            height=300,
            margin=dict(t=80, b=30, l=30, r=30),
            font={'color': "#2b2b2b", 'family': "Arial"}
        )
        st.plotly_chart(fig_gauge, use_container_width=True)

    with col2:
        # Metric cards for peak performance
        st.metric(
            label="Peak Hour Sales",
            value=f"€{peak_sales:,.2f}",
            delta=f"{efficiency_ratio:.1f}% above average"
        )
        
        st.metric(
            label="Busiest 3-Hour Window",
            value=f"{peak_hour-1}-{peak_hour+1}:00",
            delta=f"{sales_by_hour.loc[(sales_by_hour['transaction_hour'] >= peak_hour-1) & (sales_by_hour['transaction_hour'] <= peak_hour+1), 'total_sales'].sum()/sales_by_hour['total_sales'].sum()*100:.1f}% of daily sales"
        )

    hourly_stats = filtered_df.groupby('transaction_hour').agg({
        'total_sales': ['sum', 'median', 'count']
    }).reset_index()
    hourly_stats.columns = ['hour', 'total_sales', 'median_sale', 'transaction_count']

    fig = go.Figure()

    # Bar for total sales
    fig.add_trace(go.Bar(
        x=hourly_stats['hour'],
        y=hourly_stats['total_sales'],
        name='Total Sales',
        marker_color='#4B9CD3'
    ))

    # Line for median sale
    fig.add_trace(go.Scatter(
        x=hourly_stats['hour'],
        y=hourly_stats['median_sale'],
        name='Median Sale',
        line=dict(color='#FF7F50', width=3),
        yaxis='y2'
    ))

    fig.update_layout(
        title="📊 Hourly Sales Performance",
        xaxis_title="Hour of Day",
        yaxis_title="Total Sales (€)",
        yaxis2=dict(
            title="Median Sale (€)",
            overlaying='y',
            side='right'
        ),
        barmode='group',
        height=400
    )

    # --- HOURLY SALES DISTRIBUTION ---
    st.markdown("### 📦 Sales Distribution by Hour")
    st.caption("Understand transaction patterns and outliers throughout the day")

    # Create box plot
    fig = px.box(
        filtered_df,
        x='transaction_hour',
        y='total_sales',
        points=False,  # Cleaner without individual points
        color_discrete_sequence=['#4B9CD3'],
        labels={
            'transaction_hour': 'Hour of Day', 
            'total_sales': 'Sales Amount (€)'
        },
        height=500
    )

    # Add reference line for average
    avg_sale = filtered_df['total_sales'].mean()
    fig.add_hline(
        y=avg_sale,
        line_dash="dot",
        line_color="red",
        annotation_text=f"Overall Avg: €{avg_sale:.2f}",
        annotation_position="bottom right"
    )

    # Enhance layout
    fig.update_layout(
        xaxis=dict(
            tickmode='linear',
            dtick=1,
            title="Hour of Day"
        ),
        yaxis_title="Sales Amount (€)",
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        margin=dict(t=40),  # Reduce top margin
        annotations=[
            dict(
                x=0.5,
                y=-0.15,
                xref="paper",
                yref="paper",
                text="Box shows middle 50% of transactions | Lines show 5th/95th percentiles",
                showarrow=False,
                font=dict(size=12)
            )
        ]
    )

    # Add peak hour annotation
    peak_hour = filtered_df.groupby('transaction_hour')['total_sales'].sum().idxmax()
    fig.add_vrect(
        x0=peak_hour-0.5, 
        x1=peak_hour+0.5,
        fillcolor="green",
        opacity=0.1,
        line_width=0,
        annotation_text=f"Peak Revenue Hour: {peak_hour}:00", 
        annotation_position="top left"
    )

    st.plotly_chart(fig, use_container_width=True)

    # Key stats expander
    with st.expander("📊 Hourly Statistics Summary", expanded=True):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Peak Sales Hour",
                value=f"{peak_hour}:00-{peak_hour+1}:00",
                delta=f"€{filtered_df[filtered_df['transaction_hour'] == peak_hour]['total_sales'].sum():,.2f}"
            )
        
        with col2:
            st.metric(
                "Highest Median Sale",
                value=f"{filtered_df.groupby('transaction_hour')['total_sales'].median().idxmax()}:00",
                delta=f"€{filtered_df.groupby('transaction_hour')['total_sales'].median().max():.2f}"
            )
        
        with col3:
            q75 = filtered_df['total_sales'].quantile(0.75)
            st.metric(
                "Premium Threshold",
                value=f"€{q75:.2f}+",
                delta="Top 25% of transactions"
            )