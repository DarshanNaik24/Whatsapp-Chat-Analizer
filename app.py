import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns

st.markdown("""
    <style>
        /* Set background image with blur and transparency */
        .stApp {
            background: url("https://imgs.search.brave.com/JZvnd4Y7bXjTga_jD5JV97pFr0M5csLBgX2AaTtrqzg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/cHJlbWl1bS12ZWN0/b3IvYWJzdHJhY3Qt/YmFja2dyb3VuZC13/aXRoLXdoYXRzYXBw/LWxvZ29fNTI2ODMt/MjY2NDQuanBnP3Nl/bXQ9YWlzX2h5YnJp/ZCZ3PTc0MA") no-repeat center center fixed;
            background-size: cover;
            backdrop-filter: blur(9px); /* Apply blur to background */
        }

        /* Add a semi-transparent layer over background */
        .stApp::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            background-color: rgba(255, 255, 255, 0.3);  /* Semi-transparent white overlay */
            z-index: -1;
            backdrop-filter: blur(5px); /* Adjust blur strength */
        }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("Whatsapp Chat Analyzer")
import base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = image_to_base64("WhatsApp-Logo.wine.png")

st.sidebar.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{img_base64}" width="200">
    </div>
    """,
    unsafe_allow_html=True
)

app_mode = st.sidebar.selectbox("Select Page",["Home","About","Analyze Chat"])
if(app_mode == "Home"):
    st.image("1126d7da-0acc-417f-a562-5515f1ea4a1b (1).jpeg", width=400)  # Replace with your own image path if needed

    st.markdown("""
    ## **WhatsApp Chat Analysis Platform**

#### **Welcome to the WhatsApp Chat Analyzer**

**WhatsApp** is one of the most widely used instant messaging platforms globally. Every day, billions of messages are exchanged, creating a goldmine of data that reflects communication patterns, user behavior, and group dynamics. This platform is designed to **analyze and visualize your WhatsApp chat history** using **Natural Language Processing (NLP)**.

Whether you're curious about your most active friends, peak chatting hours, or the most frequently used emojis, this tool transforms raw chat data into meaningful insights.

---

#### **Why WhatsApp Analysis Matters**

Analyzing chat data can help uncover social dynamics, engagement levels, communication habits, and emotional tone. Our NLP-powered platform provides a simple and intuitive interface to explore these patterns without any coding.

---

#### **Key Features of the Platform**

- **Automated Chat Processing**: Upload `.txt` files exported from WhatsApp chats.
- **Comprehensive Statistics**: Get total messages, word counts, media shares, and link usage.
- **Visual Timelines**: See monthly and daily message trends with interactive charts.
- **User Activity Analysis**: Identify the most active members in the chat.
- **Emoji & Word Clouds**: Discover the most used emojis and commonly spoken words.
- **Heatmaps**: Visualize active hours throughout the week.

---

#### **What You Can Analyze**

1. **Message Statistics**
   - Total messages, words, shared media, and links.

2. **Activity Trends**
   - Daily and monthly timelines that show user engagement over time.

3. **Most Active Users**
   - In group chats, see who contributes the most with stats and bar graphs.

4. **Language and Emotion**
   - Common words used and emoji distribution that reflect emotional tone.

5. **Weekly Activity Heatmap**
   - Visual pattern of chats across different days and time slots.

---

#### **About the Dataset**

The chat file used is exported directly from WhatsApp using its native **"Export Chat"** feature. The file format should be `.txt` and can be from individual or group conversations. Our preprocessing step cleans and structures this data for NLP-based analysis.

The platform supports:
- English chats (best results)
- It supports chats with both 24Hrs and 12Hrs formate 
- WhatsApp formats from both Android and iOS

---

#### **Get Started**

- **Export a Chat**: Use WhatsApp's export feature to download chat as `.txt`.
- **Upload File**: Use the sidebar to upload your file.
- **Explore Visuals**: Interact with graphs, clouds, and heatmaps.
- **Analyze Group or Personal Chats**: Choose specific users or overall group stats.

    """)
elif (app_mode == "About"):
    st.header("About")
    st.image("chat-bot-dialogue-windows-flat-design-for-website-or-mobile-app-user-interface-of-application-with-dialog-boxes-conversation-with-robot-assistant-ai-chatbot-for-online-customer-service-support-vecto.jpg", width=400)  # Replace with your own image path if needed
    st.markdown("""
                #### About Project
                WhatsApp Chat Analyzer is a Natural Language Processing (NLP) project designed to extract meaningful insights from raw WhatsApp chat data. By analyzing the exported `.txt` chat file, the system identifies behavioral patterns, communication trends, most active users, frequently used words, emojis, and more. This project is ideal for those interested in data storytelling using real-world conversational data.
 
                This platform supports both **24-hour and 12-hours format chat files**.

                ---

                #### Content & Features

                The analysis process involves several core components:

                - **Preprocessing**: The raw chat file is cleaned and parsed, separating timestamps, users, and message content.
                - **Statistical Analysis**: 
                    - Total messages, words, media shared, links, etc.
                    - Most active participants in group chats.
                - **Temporal Analysis**:
                    - Monthly and daily message trends.
                    - Activity heatmaps showing hours and days of maximum engagement.
                - **Text & Emoji Analysis**:
                    - Word cloud of most frequently used terms.
                    - Emoji usage chart showing frequency and type.

                Additional functionalities include:
                - Filter by specific user or analyze overall group behavior.
                - Graphs for message trends over time.
                - Pie charts and bar plots to understand communication dynamics visually.

                ---

                #### Dataset Information

                The data for this analysis is sourced directly from WhatsApp using the **Export Chat** feature, available on both Android and iOS devices. The exported file is a `.txt` document that includes:
                - Timestamps
                - Sender names
                - Message content
                - Media labels (e.g., `<Media omitted>`)

                The data is structured to work best with chats in **English**, though the model is capable of basic analysis in other languages as well (with limited NLP features). Each message is broken down into granular components for accurate statistical and temporal tracking.

                The underlying NLP pipeline uses custom Python scripts and libraries like `pandas`, `matplotlib`, and `seaborn` for visualization, and `emoji` and `re` for text/emoji extraction.

                ---

                #### Grading & Evaluation

                The quality of insights is influenced by:
                - File format consistent with both 24Hrs and 12Hrs formate 
                - Chat language and structure
                - Chat length and number of participants

                The system has been tested with personal and group chats of varying sizes, ensuring that it can scale and adapt to real-world usage scenarios. This tool provides a fun and insightful way to explore your digital communication habits through the lens of data science and NLP.

                """)
elif(app_mode=="Analyze Chat"):
    uploaded_file = st.sidebar.file_uploader("Choose a file")
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        data = bytes_data.decode("utf-8")
        df = preprocessor.preprocess(data)

        # fetch unique users
        user_list = df['user'].unique().tolist()
        user_list.remove('group_notification')
        user_list.sort()
        user_list.insert(0,"Overall")

        selected_user = st.sidebar.selectbox("Show analysis wrt",user_list)

        if st.sidebar.button("Show Analysis"):

            # Stats Area
            num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user,df)
            st.title("Top Statistics")
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.header("Total Messages")
                st.title(num_messages)
            with col2:
                st.header("Total Words")
                st.title(words)
            with col3:
                st.header("Media Shared")
                st.title(num_media_messages)
            with col4:
                st.header("Links Shared")
                st.title(num_links)

            # monthly timeline
            st.title("Monthly Timeline")
            timeline = helper.monthly_timeline(selected_user,df)
            fig,ax = plt.subplots()
            ax.plot(timeline['time'], timeline['message'],color='green')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

            # daily timeline
            st.title("Daily Timeline")
            daily_timeline = helper.daily_timeline(selected_user, df)
            fig, ax = plt.subplots()
            ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

            # activity map
            st.title('Activity Map')
            col1,col2 = st.columns(2)

            with col1:
                st.header("Most busy day")
                busy_day = helper.week_activity_map(selected_user,df)
                fig,ax = plt.subplots()
                ax.bar(busy_day.index,busy_day.values,color='purple')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            with col2:
                st.header("Most busy month")
                busy_month = helper.month_activity_map(selected_user, df)
                fig, ax = plt.subplots()
                ax.bar(busy_month.index, busy_month.values,color='orange')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            st.title("Weekly Activity Map")
            user_heatmap = helper.activity_heatmap(selected_user,df)
            fig,ax = plt.subplots()
            ax = sns.heatmap(user_heatmap)
            st.pyplot(fig)

            # finding the busiest users in the group(Group level)
            if selected_user == 'Overall':
                st.title('Most Busy Users')
                x,new_df = helper.most_busy_users(df)
                fig, ax = plt.subplots()

                col1, col2 = st.columns(2)

                with col1:
                    ax.bar(x.index, x.values,color='red')
                    plt.xticks(rotation='vertical')
                    st.pyplot(fig)
                with col2:
                    st.dataframe(new_df)

            # WordCloud
            st.title("Wordcloud")
            df_wc = helper.create_wordcloud(selected_user,df)
            fig,ax = plt.subplots()
            ax.imshow(df_wc)
            st.pyplot(fig)

            # most common words
            most_common_df = helper.most_common_words(selected_user,df)

            fig,ax = plt.subplots()

            ax.barh(most_common_df[0],most_common_df[1])
            plt.xticks(rotation='vertical')

            st.title('Most commmon words')
            st.pyplot(fig)

            # emoji analysis
            emoji_df = helper.emoji_helper(selected_user, df)
            st.title("Emoji Analysis")

            col1, col2 = st.columns(2)

            with col1:
                st.dataframe(emoji_df)
            with col2:
                fig, ax = plt.subplots()

                plt.rcParams['font.family'] = 'Segoe UI Emoji'

                ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct="%0.2f")
                st.pyplot(fig)











