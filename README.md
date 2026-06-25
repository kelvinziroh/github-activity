# GitHub Activity CLI 🐈‍⬛

A simple command-line tool for fetching and displaying GitHub user activity from the last 90 days and present it in a concise, readable format directly from the terminal.

## Features 🎯

* View a user's recent GitHub activity
* View a summary of a user's GitHub profile
* Lightweight and easy to use

## Requirements ✅

* Python 3.13+
* uv

## Installation 🧰🛠️

### Using uv

Clone the repository:

```bash
git clone https://github.com/kelvinziroh/github-activity.git
cd github-activity
```

Install the tool:

```bash
uv tool install .
```

Verify the installation:

```bash
github-activity
```

or

```bash
which github-activity
```

### Development Installation 👨‍💻

If you want to contribute or modify the code:

```bash
git clone https://github.com/kelvinziroh/github-activity.git
cd github-activity

uv venv
source .venv/bin/activate

uv pip install -e .
```

## Usage

### Display Recent Activity

```bash
github-activity <username>
```

Example:

```bash
github-activity torvalds
```

Example output:

```text
- [2026-06-25 01:14:33+0300]: Pushed commit(s) to torvalds/linux
- [2026-06-25 01:08:49+0300]: Pushed commit(s) to torvalds/GuitarPedal
- [2026-06-24 22:55:35+0300]: Pushed commit(s) to torvalds/GuitarPedal
- [2026-06-24 20:32:39+0300]: Pushed commit(s) to torvalds/linux
- [2026-06-24 19:43:36+0300]: Pushed commit(s) to torvalds/GuitarPedal
```

### Display Profile Information

Use the `--profile` option:

```bash
github-activity <username> --profile
```

Example:

```bash
github-activity torvalds --profile
```

Example output:

```text
[name]: Linus Torvalds
[username]: torvalds
[location]: Portland, OR
[created_at]: 2011-09-03 18:26:22+0300
[updated_at]: 2026-06-17 20:35:14+0300
[public_repos]: 12
[followers]: 308776
[following]: 0
[profile_url]: https://github.com/torvalds
```

## Command Reference

```text
github-activity <username> [--profile]
```

### Arguments

| Argument   | Description              |
| ---------- | ------------------------ |
| `username` | GitHub username to query |

### Options

| Option      | Description                                            |
| ----------- | ------------------------------------------------------ |
| `--profile` | Display profile information instead of recent activity |

## Project Structure

```text
.
├── pyproject.toml
├── README.md
├── uv.lock
└── src
    └── github_activity
        ├── __init__.py
        ├── activity.py
        ├── info.py
        └── main.py
```
