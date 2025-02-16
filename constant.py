import streamlit as st  

skill_col_size = 5

def menu():
    bar0, bar1, bar2, bar3, bar4= st.columns([0.1,1,1,1,1])
    bar1.page_link("Mainpage.py", label="Introduction", icon="🏠")
    bar2.page_link("pages/1_Experience.py", label= "Experience", icon="📚")
    bar3.page_link("pages/2_Portofolio.py", label="Portofolio", icon="🎨")
    bar4.page_link("pages/3_Contacts.py", label="Contacts", icon="🌏")
    st.write("")

#publication_url --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
linkedin_logo = '''                                                                                                                                          
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-linkedin" style="font-size: 28px;"></i>                                                                           
'''

github_logo = '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-github" style="font-size: 28px;"></i>                                                                           
'''

# personal info (for main page) --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
info = {'brief':
              """    
                Data Scientist with 5+ years of experience in machine learning operations, NLP, and data analytics. Specializes in
                optimizing claim processing, reducing false positives, and enhancing model accuracy to provide actionable business insights.
                Certified in Azure DP-100 and eager to leverage expertise in designing and implementing cloud-based AI solutions.
              """,
        'name':'Kin Wong', 
        'study':'University of California Riverside',
        'location':'Kirkland, WA',
        'interest':'Full Stack, Data Science, Product Management',
        'skills':['Python','Transformer', 'LLM'],
        }

# Experience --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#[[header, subheader, date, location, content, link, link_url], [...], etc.]

Experience = [
              [":orange[Optum] | Healthcare", "Data Scientist II", 
              "Apr 2022 – Feb 2025", "Remote", 
              """
              - Currently implementing a Large Language Model (LLM) for medical contract rate extraction to prevent rate mismatches.
              - Created an AI/ML pipeline utilizing healthcare data to reduce 30% of claims in post-pay claim inventory with an increase of 20% true positive rate, reducing auditor needs by 2 across 3 platforms.
              - Optimized claim audit prioritization with healthcare data and saved over $144K annually by using PySpark for data cleaning, feature selection, and feature engineering in an AI/ML model pipeline.
              - Supervised a production claim tiering pipeline in Apache Airflow, accounting for $13.8M in annual savings by ensuring system performance through resolving Kubernetes errors, managing Docker image builds, and performing Spark version upgrades.
              - Collaborated with engineering and operations teams to address system performance issues and engaged with business stakeholders to provide insights and answers.
              - Developed a Streamlit dashboard for a claim tiering pipeline, leveraged by leadership to track KPIs and key metrics like feature drift and recovery amounts, enabling actionable insights, business decisions, and early issue detection.
              """, 
              "Company website", "https://www.optum.com"],

              [":blue[HP] | Consumer Technology", "NLP Data Scientist", 
              "Jul 2021 – Apr 2022", "Remote", 
              """
              - Developed a deep learning MLOps pipeline to process over 2 million call logs weekly, providing insights into product issues and enabling targeted actions by the operational team.
              - Fine-tuned BERT models to classify unstructured text data from helpdesk call logs, improving classification accuracy by 15% as part of a MLOps pipeline.
              - Implemented FastText and mBART models on premise to identify languages of conversational text and translate non-English text, enabling analysis of product issues from overseas customers.
              - Applied mBART model to translate non-English text on premise to address customer issues in multiple languages.
              - Increased classification model accuracy by 20% by summarizing call logs using a GPT model.
              - Created an OCR image to text pipeline using easyocr and cv2, saving 50 hours of manual data entry per month.
              """,
              "Company website", "https://www.hp.com"],

              [":violet[Calpine Corporation] | Energy", "Data Scientist", 
              "Aug 2019 – Jul 2021", "Houston, TX", 
              """
              - Engineered features and developed time series models for machine learning projects, including anomaly detection to correct faulty turbine sensor outputs.
              - Developed data pipelines and a classification system using ensemble methods to transform power plant data and accelerate turbine maintenance processes.
              - Created an NLP model to categorize business reports, enhancing report classification efficiency.
              """, 
              "Company website", "https://www.calpine.com"],

              [":violet[Calpine Corporation] | Energy", "Data Analyst", 
              "Jul 2017 – Dec 2018", "Houston, TX", 
              """
              - Streamlined system report for power plant users by developing a PowerApps application integrated with SharePoint.
              - Designed, enhanced, and tested BIRT reports from EAM software Maximo utilizing SQL and JavaScript, delivering tailored solutions to meet business needs.
              - Created on-demand SSRS reports using real-time data to improve power plant operational insights.
              """, 
              "Company website", "https://www.calpine.com"],
          ]
# Portfolio --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#     {'project1':[HEADER, CONTENT]
#      'project2':[HEADER, CONTENT]
#      ...}

Portfolio = { 1:[':blue[Deis]Evaluation - Course Evaluation Website',
              """
              Launched a course evaluation web app for Brandeis students to review and share courses, exceeding 200+ active users.
              Designed the whole UI with Figma and Implemented front end with Javascript, HTML/CSS in a MERN Stack.
              """],
              2:['Data Visualization in :orange[D3.js]',
                  """
                Created a data visualization web app for Massachusetts police expenditure data using D3.js.
                """],
              3:[':blue[LLM] Desktop ChatApp',
                """
                - Designed and developed a cross-platform **desktop LLM Chat app**, enabling chat over user-upload dataset; providing a more accurate response to domain-specific inquiries than ChatGPT.
                - Utilized Embedding and Searching from **OpenAI API** to optimize Chat app’s response. Split the user-upload file into small chunks; used OpenAI Embedding model to vectorize each chunk and save them into Qdrant database. Transform user query to vector using OpenAI, and then inquire the top match text chunk from Qdrant database using topk value.
                """],
              4:[':orange[Anthropology] Research Project - A Timeless Building',
                """
                - An **qualitative anthropological research** on the preservation and adaption of historical sites; as final project, received the highest score in class.
                - My fieldwork includes interviewing educators, examing archive, on-site obervation. Through my fieldwork at King’s Chapel, I argued for a humane approach to preserving historic sites, that seeks a balance between **maintaining the historical significance and the sites’ adaptations to societal changes**.
                """],
              5:[':green[RAG] playground',  
                """
                - Developed a **RAG** chatbot that support difference choices over Embedding model, chunking strategy, top k retreival, LLM model, prompt engineering, and meta-data retreival search.
                - Implemented the file uploading workflow; Utilized **Langchain splitter** module and Python script to clean and chunk the uploaded file and use Huggingface sentence transformers and **Pinecone** to vectorize and store data.
                - Used SpaCy NER model to retreive meta data from prompt and ran a hybrid search using meta-data and vector.
                """]
            }
              
# Contacts --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
phone = "832-123-1234"
email = "kinwong.ds@gmail.com"
linkedin_link = "www.linkedin.com/in/ki-wong"
github_link = "https://github.com/kinwong-ds"


# iframes --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
figma_iframe = '<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1" allowfullscreen></iframe>'

figma_link = "https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1"

StoryMap_iframe = "https://storymaps.arcgis.com/stories/dfb9689618e343cf9f6ef36d9a8329a7?header"

Evaluation_html = '''
                <div class="github-card" data-github="Rsirp0c/deis-course-evaluation" data-width="400" data-height="" data-theme="default"></div>
                <script src="https://cdn.jsdelivr.net/github-cards/latest/widget.js"></script>                
                '''
