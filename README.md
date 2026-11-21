# Hello Streamlit 👋

A simple **Hello World web application** built with Python and Streamlit. This project also demonstrates a basic Continuous Integration (CI) quality gate using GitHub Actions and automatic deployment through Streamlit Community Cloud.

[![Live App](https://img.shields.io/badge/Live%20App-Open%20Streamlit-brightgreen?logo=streamlit)](https://aaj8fbafdhft65oqsyy5rp.streamlit.app/)

[![Streamlit QA Gate](https://github.com/priandoyo/streamlit/actions/workflows/qa.yml/badge.svg)](https://github.com/priandoyo/streamlit/actions/workflows/qa.yml)

## Live Demo

**[Open the Streamlit application](https://aaj8fbafdhft65oqsyy5rp.streamlit.app/)**

The application displays a greeting, accepts a visitor's name, and returns a personalized response.

## Features

- Display a Hello World message
- Accept user input through a text field
- Display a personalized greeting
- Deploy the application through Streamlit Community Cloud

## Technology

- **Python 3.12** — application language
- **Streamlit** — web application framework
- **GitHub** — source code repository and version history
- **GitHub Actions** — automated CI workflow
- **YAML** — workflow configuration language
- **Ruff** — Python linting and static code analysis
- **Streamlit Community Cloud** — application hosting and deployment

## CI/CD Overview

This project demonstrates a simple CI/CD workflow by separating **quality checks (CI)** from **application deployment (CD)**.

### 1. Continuous Integration — GitHub Actions

The CI workflow is defined in `.github/workflows/qa.yml`.

It runs automatically when code is pushed to the `main` branch, when a pull request targets `main`, or when manually started through GitHub Actions.

The workflow performs three basic quality gates:

| Gate | Check | Purpose |
|---|---|---|
| 1 | Python syntax validation | Detect Python syntax and compilation errors using `compileall` |
| 2 | Streamlit dependency validation | Verify Streamlit is installed and its command-line interface works |
| 3 | Code quality validation | Identify linting issues and common Python problems using Ruff |

Before the checks, GitHub Actions checks out the repository, sets up Python 3.12, and installs the packages listed in `requirements.txt` together with Ruff.

The workflow result is recorded in GitHub Actions, providing an execution history with the triggering commit, status, and logs.

**[View Streamlit QA Gate executions](https://github.com/priandoyo/streamlit/actions/workflows/qa.yml)**

> These are introductory technical and static-analysis checks. They do not yet constitute full functional, integration, security, or performance testing. The workflow also does not itself block merges. Configure a GitHub branch ruleset requiring the QA status check if you want it enforced as a merge gate.

### 2. Continuous Deployment — Streamlit Community Cloud

Streamlit Community Cloud is connected to this GitHub repository and deploys the application from its configured branch.

The basic delivery flow:

```text
Code change
    |
    v
GitHub repository
    |
    +----> GitHub Actions: automated QA checks
    |
    +----> Streamlit Community Cloud: deployment
                  |
                  v
             Live application
```

The CI workflow and Streamlit deployment are separate integrations. A failed GitHub Actions run does not automatically prevent Streamlit Community Cloud from deploying a change.

To enforce QA before deployment, use pull requests and branch protection so changes cannot be merged into the deployment branch until the required checks pass.

## Run Locally

1. Clone this repository:

   ```bash
   git clone https://github.com/priandoyo/streamlit.git
   cd streamlit
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   streamlit run app.py
   ```

## Project Files

```text
streamlit/
├── app.py
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
        └── qa.yml
```

## Related Article

For the accompanying walkthrough and explanation of the CI/CD experiment, read:

**[Streamlit CI/CD — Anjar Priandoyo](https://priandoyo.wordpress.com/2026/11/21/streamlit-ci-cd/)**

---

Built with Python and Streamlit.
