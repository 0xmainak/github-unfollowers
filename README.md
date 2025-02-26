# 🔄 GitHub Unfollower Tool

<div align="center">

![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

</div>

Automate unfollowing GitHub users who don't follow you back using Python.

## 🎯 Key Features

- 📊 Analyzes your GitHub followers and following
- 🔍 Detects non-reciprocal followers
- 🤖 Automates unfollow process
- 🔒 Secure GitHub token authentication
- ⚡ Rate limit protection

## 📥 Installation

1. **Clone Repository**
```bash
git clone https://github.com/yourusername/github-unfollower
cd github-unfollower
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure Authentication**
- Create `.env` file:
```env
GITHUB_USERNAME=your_username
GITHUB_TOKEN=your_token
```
- Get token: GitHub Settings → Developer Settings → PAT (need `user` scope)

## 🚀 Usage

Run:
```bash
python main.py
```

The tool will:
1. Get your network data
2. Find non-mutual followers
3. Process unfollows safely

## ⚙️ Technical Details

- Python 3.6+ required
- Implements API rate limiting
- Secure credential handling
- Robust error management

## 📝 License

MIT

## ⚠️ Note

Use responsibly within GitHub's terms of service.

