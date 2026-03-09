# Email Header Analysis

## Overview

This analysis compares a phishing email header with a legitimate email header to identify indicators of malicious activity.

---

## Phishing Header Indicators

File: data/sample_email_header.txt

Indicators observed:

- SPF authentication failure
- Sender domain does not match the return path
- Suspicious sending mail server
- Possible spoofed domain

Example:

spf=fail (domain of paypal.com does not designate 185.234.217.12 as permitted sender)

This indicates the sending server was not authorized to send email for the claimed domain.

---

## Legitimate Header Indicators

File: data/legitimate_email_header.txt

Indicators observed:

- SPF authentication passes
- Sender domain matches return path
- Mail server belongs to the sending organization
- Proper authentication results

Example:

spf=pass (google.com: domain of no-reply@accounts.google.com designates permitted sender)

This indicates the email originated from an authorized server.

---

## Key Differences

| Feature | Phishing Header | Legitimate Header |
|-------|-------|-------|
| SPF | Fail | Pass |
| Sending Server | Unknown / suspicious | Official mail server |
| Domain Consistency | Mismatch | Matches organization |
| Trustworthiness | Likely malicious | Legitimate |

---

## Conclusion

Email header analysis can reveal spoofed domains and unauthorized sending servers.  
Authentication failures such as SPF errors are strong indicators that an email may be fraudulent.
