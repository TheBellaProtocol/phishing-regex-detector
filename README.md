# Phishing Detection with Regex

## Overview

This project demonstrates a simple phishing detection tool built in Python. The script analyzes email content using regular expression (regex) rules to identify common phishing indicators such as suspicious language and spoofed email characteristics.

In addition to automated detection, this repository includes documentation analyzing email headers to show how authentication failures and server inconsistencies can indicate phishing attempts.

This project was created to practice practical cybersecurity skills including threat detection, email analysis, and basic security tool development.

---

## Features

- Python-based phishing detection script
- Regex pattern matching for suspicious email indicators
- Sample phishing email content for testing
- Email header analysis comparing phishing and legitimate messages
- Organized project structure separating code, rules, data, and analysis

---

## Project Structure

```
/src
    phishing_detector.py

/data
    phishing_samples.txt
    phishing_email_header.txt
    legitimate_email_header.txt

/rules
    regex_rules.txt

/analysis
    findings.md
    header_analysis.md
```

---


### Folder Descriptions

**src/**  
Contains the Python script used to analyze email content.

**data/**  
Contains sample phishing email content and header examples used for testing and analysis.

**rules/**  
Contains regex patterns used by the detector to identify phishing indicators.

**analysis/**  
Contains documentation describing the investigation process and analysis of phishing indicators.

---

## How the Detector Works

The Python script scans email content using predefined regex rules designed to detect common phishing patterns.

These patterns may include:

- Urgent or threatening language
- Requests for sensitive information
- Suspicious links or domains
- Social engineering language

The detector reads patterns from `rules/regex_rules.txt` and scans the email samples in the `data` folder. When a pattern matches part of the email content, the script reports it as a potential phishing indicator.

---

## Example Output

Example of the detector analyzing phishing content:

Scanning email content...

Rule matched: urgent_language
Matched text: "Your account will be suspended"

Rule matched: credential_request
Matched text: "Verify your account immediately"

Potential phishing indicators detected.

This demonstrates how the script identifies suspicious phrases that commonly appear in phishing emails.

---

## Email Header Analysis

This repository also includes a comparison between a phishing email header and a legitimate email header.

The analysis highlights several indicators that can help identify spoofed or malicious emails, including:

- SPF authentication failures
- Suspicious sending mail servers
- Domain inconsistencies
- Differences between legitimate and spoofed email infrastructure

The full analysis is documented in:

analysis/header_analysis.md

---

## Skills Demonstrated

This project demonstrates several foundational cybersecurity and programming skills:

- Python scripting
- Regular expression pattern matching
- Basic phishing detection techniques
- Email header analysis
- Security investigation documentation
- Organized project structure

---

## Future Improvements

Possible improvements for this project include:

- Expanding the phishing dataset
- Adding additional detection patterns
- Incorporating other email authentication checks such as DKIM or DMARC
- Improving detection logic for more complex phishing techniques

---

## Disclaimer

The phishing examples included in this repository are provided for educational purposes only and are intended to demonstrate common phishing characteristics.
