# AWS Learning & Labs

Notes and hands-on lab work from my AWS learning path, following **KodeKloud** courses and their free hands-on labs — covering core AWS Free Tier services with practical, in-console exercises.

## Overview

This folder tracks my progress learning AWS as part of my DevOps internship at Expertflow. Each service/topic includes a short summary of what it does, what I practiced, and any gotchas or key commands worth remembering. Labs were done using KodeKloud's free-tier playgrounds, so most exercises are safe, low-cost, sandboxed environments rather than a personal AWS account.

## Learning Source

- **Platform:** [KodeKloud](https://kodekloud.com/)
- **Format:** Video courses + KodeKloud's free browser-based AWS labs
- **Scope:** AWS Free Tier services (core compute, storage, networking, IAM, and monitoring)

## Services Covered

- [x] **IAM** — Users, groups, roles, policies, MFA, least-privilege access
- [x] **EC2** — Launching instances, security groups, key pairs, AMIs, Elastic IPs, instance types
- [x] **VPC** — Custom VPCs, subnets (public/private), route tables, internet gateways, NAT gateways, security groups vs NACLs
- [x] **S3** — Buckets, object storage, versioning, bucket policies, static website hosting
- [x] **EBS** — Volumes, snapshots, attaching/detaching storage to EC2
- [x] **RDS** — Managed relational databases, Multi-AZ basics, security groups for DB access
- [x] **Route 53** — DNS records, hosted zones, routing policies
- [x] **CloudWatch** — Metrics, alarms, logs for monitoring resources
- [x] **Lambda** — Serverless functions, triggers, basic event-driven automation
- [x] **CloudFormation** — Infrastructure as Code basics, templates, stacks
- [x] **ELB / Auto Scaling** — Load balancers, target groups, scaling policies
- [x] **SNS / SQS** — Notification and messaging services basics

> Update the checklist above as you add or revisit topics — uncheck anything not yet covered, or add new services as you go.

## Folder Structure

```
aws/
├── README.md
├── iam/
├── ec2/
├── vpc/
├── s3/
├── rds/
├── route53/
├── cloudwatch/
├── lambda/
└── cloudformation/
```

## Key Concepts Learned

- Core AWS global infrastructure: regions, availability zones, edge locations
- Shared Responsibility Model (AWS vs customer responsibilities)
- Identity and access management fundamentals — least privilege, role-based access
- Difference between security groups (stateful, instance-level) and NACLs (stateless, subnet-level)
- Designing a basic VPC with public/private subnet separation
- Static vs dynamic content hosting (S3 vs EC2)
- Monitoring and alerting fundamentals with CloudWatch
- Serverless basics — when to use Lambda vs EC2
- Infrastructure as Code fundamentals with CloudFormation

## Tools Used

- AWS Management Console
- AWS CLI (where labs allowed)
- KodeKloud browser-based labs (free-tier sandboxed AWS environments)

## Notes

- Labs were run in KodeKloud's provided sandbox accounts rather than a personal AWS account, to stay within free-tier limits and avoid unexpected billing.
- This folder will keep growing as I complete more KodeKloud modules — check individual subfolder READMEs (once added) for topic-specific details.

## Author

**Zeeshan Khan** — DevOps Intern
