# 📦 AWS-Event-Driven-Compliance-Automation

## 🔍 Project Overview

This project demonstrates how to automate resource compliance in AWS using **EventBridge**, **Lambda**, and **CloudWatch Logs**.  
As part of the Cloud Engineering team, our goal is to ensure that all AWS infrastructure adheres to **organizational policies** without requiring manual intervention.

### 🎯 Use Case

We specifically automate a compliance policy that:
- **Detects** when a new EBS volume is created.
- **Identifies** if the volume is of type `gp2`.
- **Automatically modifies** it to type `gp3` using AWS Lambda and `boto3`.

---

## 💡 Key Features

- ✅ Event-driven automation via **Amazon EventBridge**
- ✅ Real-time EBS volume type enforcement using **Lambda**
- ✅ Integration with **CloudWatch Logs** for traceability
- ✅ Fine-grained **IAM Role** setup for secure execution
- ✅ Scalable architecture extendable to EC2, S3, and other services

---

## 🚀 Architecture Diagram

![image](https://github.com/user-attachments/assets/5a562042-edbe-476a-9634-5e7449d2ef16)


---

## ⚙️ Steps Performed

1. **Lambda Setup**
   - Created a basic Lambda function with Python runtime.
   - Attached an IAM role with basic permissions (or created a new IAM role).

2. **EventBridge Rule Configuration**
   - Defined a rule to trigger when an EBS volume is created.
   - Set the target to our Lambda function (`ebs_check`).

3. **Testing the Trigger**
   - Created a dummy EBS volume to validate that the Lambda function is triggered correctly.
   - Logged the event payload using `print(event)` inside Lambda.

4. **Event Debugging & Volume ID Extraction**
   - Fetched CloudWatch logs to retrieve actual event structure.
   - Wrote a helper function to extract the EBS volume ID from the event JSON.

5. **Volume Modification Logic**
   - Used Python `boto3` to create an EC2 client inside Lambda.
   - Called the `modify_volume()` API to convert `gp2` to `gp3`.

6. **IAM Role Permissions**
   - Updated the Lambda execution role with required EC2 permissions:
     - `ec2:ModifyVolume`
     - `ec2:DescribeVolumes`

---

## 🧰 Tools & Technologies

- AWS Lambda (Python runtime)
- Amazon EventBridge
- AWS CloudWatch Logs
- AWS Identity and Access Management (IAM)
- Python 3.9
- boto3 SDK

---

## 📌 Future Scope

- Extend compliance logic to:
  - Enforce EC2 instance type standards
  - Enforce S3 bucket configurations
- Build a generic handler-based Lambda framework
- Integrate with AWS Config or use Step Functions for larger-scale orchestration

