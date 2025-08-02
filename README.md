# One-Tap EC2 Control from Android 🔘📱

A secure, serverless solution to start/stop AWS EC2 instances from an Android phone with a single tap — no console login needed.

## 🔧 Stack Used

- AWS Lambda (Python + boto3)
- Amazon API Gateway (HTTP API + API Key)
- IAM Roles (Least Privilege)
- Android app: HTTP Request Shortcuts

## 📲 Workflow Overview

Android Shortcut → API Gateway → Lambda → EC2 Instance

![Architecture](ec2_architecture_diagram.png)

## ✅ Features

- Start and Stop EC2 with one tap
- API secured with API Key
- Lambda error handling with CloudWatch
- Works from mobile — no login needed

## 🛠️ Files Included

- `lambda/start_instance.py` & `lambda/stop_instance.py`
- `iam_policy.json`
- `api_gateway_config.md`
- `android_shortcut_setup.md`

## 🔗 Connect

Built by [Rehan Ahmad](https://www.linkedin.com/in/rehanxahmad)