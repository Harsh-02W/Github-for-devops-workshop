# Github-for-devops-workshop
This repository documents my hands-on learning during a DevOps workshop, with a focus on Git, GitHub, and GitHub Actions.
The goal of this repo is not to showcase perfect code, but to practice workflows, automation, and good habits while learning.

**What this repository covers**

Core Git concepts (clone, commit, push, hooks)

Working with GitHub repositories

Basic GitHub Actions workflows

Understanding how local checks and remote automation fit together

**Project files**

- testing.py

A small console-based Python game created for practice.
This file was used to experiment with:

Code changes and commits

Linting checks

Preventing bad code from being pushed

- demo.py

A simple calculator program in Python.
This file helped me practice:

Writing clean, readable code

Running lint checks

Observing how automation reacts to different code states

**Git Hooks**

I implemented a pre-push Git hook inside the .git/hooks directory.

Purpose:

To prevent pushing code when errors or issues are detected

To enforce basic discipline before code reaches the remote repository

This helped me understand how local safeguards can stop problems early.

**GitHub Actions**

I added Pylint using GitHub Actions directly from the GitHub Actions interface.

What this does:

Automatically checks Python code quality on push

Fails the workflow if linting issues are found

Encourages cleaner and more consistent code

This was my first exposure to integrating automated checks into a repository.

**Why this repository exists**

This repository is part of my learning journey.
It reflects:

Experimentation

Mistakes and fixes

Gradual understanding of DevOps practices

It is intentionally simple and focused on fundamentals.

**Acknowledgment**

Learning inspired by the DevOps Junoon workshop by trainwithshubham, with a strong emphasis on practical, hands-on understanding.

**Disclaimer**

This repository is for learning and practice purposes only and is not intended for production use.
