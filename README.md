# Serverless Order Processing System (AWS)

## 🚀 Overview
This project demonstrates a serverless event-driven architecture on AWS for processing orders asynchronously.

## 🏗️ Architecture
- API Gateway (HTTP API)
- AWS Lambda (Create Order & Process Order)
- Amazon SQS (Queue)
- Amazon DynamoDB (Database)
- Amazon SNS (Email Notification)

## 🔄 Workflow
1. User sends POST request via API Gateway
2. Create-order Lambda pushes message to SQS
3. Process-order Lambda consumes message
4. Data stored in DynamoDB
5. SNS sends email notification

## 🛠️ Tech Stack
- AWS Lambda
- Amazon API Gateway
- Amazon SQS
- Amazon DynamoDB
- Amazon SNS
- Python (Boto3)

## 📌 Features
- Asynchronous processing using SQS
- Scalable serverless architecture
- Real-time email notifications

## 🧪 API Endpoint
POST /order

Example:
{
  "item": "Laptop"
}

## ✅ Output
- Order stored in DynamoDB
- Email notification sent via SNS
