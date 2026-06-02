\# Security Policy



\## Reporting Security Issues



Please do not open public issues for security vulnerabilities.



Instead, report security concerns privately to the repository maintainer.



\## Sensitive Data Rules



This project must not contain:



\- API keys

\- `.env` files

\- User-uploaded books

\- Copyrighted book samples

\- Private OCR outputs

\- Private translation outputs



\## Provider Safety



OCR and translation providers should be optional and mockable.



Tests must not call real external providers by default.

