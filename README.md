# Bug Bounty Automation & Recon Agent

## Overview
This project is an **AI-powered automation tool** designed to help with **HTB** **CTF challanages . It automates **technology fingerprinting**, **vulnerability detection**, and **exploitation prioritization** using:

- **Wappalyzer**: Detects technologies running on a target website.
- **SearchSploit**: Identifies known vulnerabilities for detected technologies.
- **OpenAI GPT-4o**: Analyzes and ranks the most exploitable technologies and provides strategic attack recommendations.

## Features
- **Automated reconnaissance**: Scans a given website to identify web technologies.
- **Exploit discovery**: Finds potential exploits using **SearchSploit**.
- **AI-based vulnerability ranking**: Uses **GPT-4o** to prioritize exploitable technologies.
- **PoC Generation**: Provides exploitation strategies and **proof-of-concept (PoC) suggestions**.

## Installation

### Prerequisites
Ensure you have the following installed:

- **Python 3.8+**
- **pip (Python Package Manager)**
- **SearchSploit (Exploit-DB CLI)**:

Tested only with **dog** machine from HTB

```sh

Enter the target URL: http://dog.htb
Analyzing technologies with balanced scan...
Checking for known exploits using SearchSploit...
Determining most likely exploitable technologies with AI...

http://dog/htb Technologies Detected:
- AngularJS
- Apache HTTP Server
- Backdrop
- Ubuntu
- Drupal
- jQuery
- jQuery UI
- PHP

 Exploits Found:
- Apache HTTP Server (3 exploits) - Most Critical: Apache 1.0/1.2/1.3 - Server Address Disclosure
- Backdrop (3 exploits) - Most Critical: Backdrop CMS 1.20.0 - 'Multiple' Cross-Site Request Forgery (CSRF)
- Ubuntu (3 exploits) - Most Critical: Acpid 1:2.0.10-1ubuntu2 (Ubuntu 11.04/11.10) - Boundary Crossing Privilege Escalation
- Drupal (3 exploits) - Most Critical: Drupal 10.1.2 - web-cache-poisoning-External-service-interaction
- jQuery (3 exploits) - Most Critical: BK Mobile jQuery CMS 2.4 - Multiple Vulnerabilities
- jQuery UI (2 exploits) - Most Critical: jQuery - jui_filter_rules PHP Code Execution
- PHP (3 exploits) - Most Critical: 'customhs_js_content' - 'customhs_js_content' Cross-Site Request Forgery

 AI Recommended Attack Surface:
1. **Backdrop**: This CMS has a known vulnerability for authenticated remote command execution (RCE), which is severe as it may allow attackers to execute arbitrary commands on the server. Exploiting RCE typically provides high returns to attackers by giving them control over the host system.

2. **Apache HTTP Server**: While older versions have several vulnerabilities, cross-site scripting (XSS) through server-side includes can be a serious issue. If a vulnerable configuration is detected, attackers can potentially inject scripts into trusted contexts, threatening data integrity and user privacy.

3. **Drupal**: With vulnerabilities like web-cache poisoning and XSS, Drupal installations can be particularly appealing targets for attackers aiming to inject malicious scripts or interact with external services in unintended ways. These issues can compromise both the site's data confidentiality and integrity depending on the extent of the interaction.

These technologies are significant due to the potential scope of their vulnerabilities, potential for easy exploitation, and the impact of a successful attack, which is why they are prioritized for closer scrutiny.
```

## Disclaimer

 This tool is for educational and ethical testing purposes only.
Unauthorized testing of systems you do not own is illegal. Always obtain explicit permission before running security assessments.