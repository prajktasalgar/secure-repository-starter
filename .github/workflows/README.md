# Secure Repository Starter

## 1. Project Overview

Secure Repository Starter is a reusable Python repository template designed to demonstrate secure software development practices and DevSecOps automation.

It includes automated testing, Python security analysis, dependency vulnerability checking, and secret detection using GitHub Actions.

## 2. Project Objectives

- Establish a reusable and organized Python project structure.
- Automate software testing using pytest.
- Identify common Python security issues using Bandit.
- Detect vulnerable dependencies using pip-audit.
- Identify exposed credentials using Gitleaks.
- Automate security checks through GitHub Actions.

## 3. Project Structure

```text
secure-repository-starter/
│
├── .github/
│   └── workflows/
│       └── security.yml
│
├── src/
│   └── app.py
│
├── tests/
│   └── test_app.py
│
├── .gitignore
├── SECURITY.md
└── requirements.txt
```

## 4. Technologies Used

- Python 3.12
- pytest – automated testing
- Bandit – Python security analysis
- pip-audit – dependency vulnerability scanning
- Gitleaks – secret detection
- GitHub Actions – CI automation
- Dependabot – dependency update monitoring

## 5. Setup Instructions

### Prerequisites

- Python 3.12
- pip package manager
- GitHub account

### Install dependencies

Clone the repository:

```bash
git clone https://github.com/prajktasalgar/secure-repository-starter.git
cd secure-repository-starter
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Install the security tools:

```bash
python -m pip install bandit pip-audit
```

## 6. Run the Application

```bash
python src/app.py
```

Expected output:

```text
Secure Repository Starter is running!
Addition: 30
```

## 7. Run Tests

```bash
pytest -q
```

The project includes five tests covering the welcome message, positive number addition, zero, negative numbers, and invalid input.

## 8. Security Checks

The GitHub Actions workflow automatically runs the following checks:

| Tool | Purpose |
|---|---|
| Bandit | Detects common Python security issues |
| pip-audit | Checks dependencies for known vulnerabilities |
| pytest | Executes automated tests |
| Gitleaks | Scans for exposed secrets |

The workflow runs on pushes and pull requests targeting the main branch. It can also be started manually through GitHub Actions.

## 9. Security Practices

- Never commit real passwords, API keys, or access tokens.
- Use environment variables or a secure secrets manager for credentials.
- Keep dependencies updated.
- Review security scan results.
- Follow the vulnerability reporting guidance in SECURITY.md.

## 10. Known Limitations

- Security scanners can produce false positives and may miss certain vulnerabilities.
- Bandit detects only supported patterns of Python security issues; it cannot guarantee that the application is secure.
- pip-audit checks known vulnerabilities in installed or declared dependencies and cannot detect every software supply-chain risk.
- Gitleaks scans the commit range configured in the workflow; the current workflow scans the latest commit rather than the entire repository history.
- The example application is a basic demonstration and is not intended for production use.
- Automated checks do not replace manual security reviews and testing.

## 11. References

- Python: https://docs.python.org/3/
- pytest: https://docs.pytest.org/
- Bandit: https://bandit.readthedocs.io/
- pip-audit: https://pypi.org/project/pip-audit/
- Gitleaks: https://github.com/gitleaks/gitleaks
- GitHub Actions: https://docs.github.com/en/actions
- Dependabot: https://docs.github.com/en/code-security/dependabot

## 12. License

License information will be provided in the repository's LICENSE file.
