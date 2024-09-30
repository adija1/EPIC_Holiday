import json
import boto3

# Define boto3 client for Amazon Bedrock invocation and Amazon SES
client = boto3.client(service_name='bedrock-runtime')
ses_client = boto3.client('ses', region_name='us-east-1')  # specify appropriate AWS region

# Define parameters for the Claude model invocation
claude_bedrock_model_id = "anthropic.claude-3-haiku-20240307-v1:0"
claude_accept = 'application/json'
claude_content_type = 'application/json'

# Function to invoke the Bedrock Claude model and parse result back
def call_claude_llm(body):
    response = client.invoke_model(body=body, modelId=claude_bedrock_model_id, accept=claude_accept, contentType=claude_content_type)
    response_body = json.loads(response.get('body').read())
    full_text = ""
    if "content" in response_body and isinstance(response_body["content"], list):
        for item in response_body["content"]:
            if "text" in item:
                full_text += item["text"]
    return full_text

# Function to create body for Claude model request
def create_claude_body(customer, review):
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 500,
        "messages": [{
            "role": "user",
            "content": f"You are drafting emails for the EpicHoliday Customer Experience Team, responding to feedback from customer reviews. \
Draft a follow up email to {customer} based on their recent review of their trip. \
If the review is negative, be apologetic, refer to customer provided details in their review and offer $100 discount for their next vacation. \
If the review was positive, paraphrase their review and thank them for taking the time to leave the review. \
If there's not enough detail to explain why a customer was satisifed or dissatisfied, ask them to provide more details. \
Limit your resopnse to no more than 150 words. \
Your response should include only the email, so the first word should be 'Dear' followed by their first name. \
Every email should end with 'We wish you an EPIC day!'. \
Here is the review: {review}",
        }],
        "temperature": 0.2,
        "top_p": 0.9})
    return body

# Function to send email using Amazon SES
def send_email(email_address, subject, body):
    # Append the signature to the body
    signature = "\n\nEPIC Customer Experience team"
    full_body = body + signature
    
    response = ses_client.send_email(
        Source='epicholiday@mail.com',  # Replace with your "From" address
        Destination={'ToAddresses': [email_address]},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': full_body}}
        }
    )
    return response


# Main Lambda handler
def lambda_handler(event, context):
    try:
        records = event["arguments"]
        results = []
        for record in records:
            customer = record[0]
            review = record[1]
            email_address = record[2]  # Assuming the email address is the third item in the record
            body = create_claude_body(customer, review)
            try:
                email_content = call_claude_llm(body)
                results.append(email_content)
                send_email(email_address, "Follow-up on Your Trip Review", email_content)  # Sending email with updated subject
            except Exception as e:
                results.append(str(e))
        response = {'success': True, 'results': results}
    except Exception as e:
        response = {'success': False, 'error_msg': str(e)}
    return json.dumps(response)

