# EPIC_Holiday
The code and stuff from the EPIC Holiday session - how to use Redshift data with Gen AI.

# Introduction:
EPIC Holiday is a fictitious Travel Agency that offers it's customers travel packages that comprosed of Flights, Hotels & Tickets to the hottest concerts! What sets them apart from competitiors is that they use Gen AI to deliver their customers a personalized experience from booking of the packages to post travel.

The session covers the following topics and services:

1. Streamlit chatbot for planning a personalized itinerary.
   Components:
   - EC2 running streamlit
   - Redshift with customer & booking tables
   - Bedrock and Claude 3 Haiku
   The entire end to end setup is here:
   https://aws.amazon.com/blogs/machine-learning/build-generative-ai-chatbots-using-prompt-engineering-with-amazon-redshift-and-amazon-bedrock/
   In the actual presentation done by Liat Tzur & Adi Jabkowsky the model being used is Claude Haiku 3 and the modified code can be found in this repo as travel_planner.py

2. Sentiment analysis using Redshift ML capabilites.
   Components:
   - Redshift cluster with customers tables and reviews.
   - SageMaker Jumpstart for deploying Falcon 7B Instruct.
   The entire setup is here:
   https://aws.amazon.com/blogs/big-data/large-language-models-for-sentiment-analysis-with-amazon-redshift-ml-preview/

3. Automatic email drafting according to review / sentiment analysis
   Components:
   - Redshift cluster with customer table, reviews and email address for each customer
   - Amazon Bedrock with Claude 3 Haiku
   - Amazon Lambda
   - Amazon SES
   The entire setup is here:
   https://repost.aws/articles/ARJszlMEepRti6xoM-0fsBmw
   In the actual presentation done by Liat Tzur & Adi Jabkowsky the model being used is Claude Haiku 3 and the modified code can be found in this repo as redshift-trip-reviews-lambda-haiku.py

4. Internal travel agent AI asistant using Amazon Q Business
   Components:
   - Amazon Q Business using S3 & Web cralwer for indexing data

5. Generative BI using Quicksight Q. Generate BI visualizations and insights using natural language.
   Components:
   - Quicksight Q
   https://docs.aws.amazon.com/quicksight/latest/user/quicksight-q-get-started.html

  
   



