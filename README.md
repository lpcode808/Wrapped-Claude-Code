# 🎁 Claude Code Wrapped

**Your Spotify Wrapped for AI-Assisted Development**

Get a beautiful year-end summary of your Claude Code usage - complete with stats, insights, and shareable moments!

View the behind the scenes here [https://lpcode808.github.io/Wrapped-Claude-Code/](https://lpcode808.github.io/Wrapped-Claude-Code/)
---

## 🎨 DIY Usage - let Claude Code drive

### One-Prompt Method (For the Adventurous!)
Don't want to clone repos? See [PROMPT_METHOD.md](PROMPT_METHOD.md) for a single copy-paste prompt that lets Claude Code build everything from scratch.

### Generate Visual Animations
Want Spotify-style animated graphics? See [ANIMATION_GUIDE.md](ANIMATION_GUIDE.md) for prompts to create shareable visuals from your data.

## 🚀 Quick Start

### Run the Analysis

```bash
# Clone this repo and run in your project directory
python3 count_user_inputs.py
```

**Output:** How many messages you typed, your most active projects, and easy-to-understand metrics perfect for sharing!

---

## 📊 What You'll Get

### Core Metrics
- ✍️ **Messages you typed** (not system events!)
- 💬 **Number of conversations**
- 📁 **Projects worked on**
- 🤖 **Agents spawned** (background tasks)
- ⏰ **Peak coding hours**
- 📅 **Busiest days**

### Fun Stats
- 🔥 Longest conversation sessions
- 📝 Total words/characters typed
- 🦉 Early bird or night owl?
- 🎯 Your coding personality
- 🏆 Hottest month/week
- ⚡ Longest coding streak

---

## 🛠️ Available Tools

### 1. User Input Counter (Recommended!)
```bash
python3 count_user_inputs.py
```
**Best for:** Clear, shareable stats that non-technical folks understand

### 2. Session Counter
```bash
chmod +x count_sessions.sh
./count_sessions.sh
```
**Best for:** Conversation-level breakdown

### 3. Project Details
```bash
chmod +x detailed_stats.sh
./detailed_stats.sh
```
**Best for:** Per-project deep dive

### 4. Spotify Wrapped Style
```bash
python3 spotify_wrapped_analysis.py
```
**Best for:** Fun facts and personality insights

---

## 📖 Understanding the Metrics

### What's a "Message"?
**Your messages** = Times you typed something and hit enter
- ✅ Counts: What YOU typed
- ❌ Doesn't count: Claude's responses, tool calls, system messages

### What's a "Session/Conversation"?
One continuous thread in a project directory. Each session = one `.jsonl` file.
- Starting Claude Code creates a new session
- Closing and reopening creates a new session
- One project can have multiple sessions

### What's an "Agent"?
Background tasks Claude Code spawns to work on subtasks in parallel while you continue.
- Shows up as `agent-*.jsonl` files
- Indicates advanced usage and complex workflows

---

## 🎨 Sample Output

```
╔══════════════════════════════════════════════════════════════╗
║       USER INPUT ANALYSIS (What YOU Actually Typed)         ║
╚══════════════════════════════════════════════════════════════╝

✍️  You typed:                        XXX messages
🤖 Claude responded:                  XXX times
🔧 Tools used:                        XXX+ tool calls
💬 Across XX conversations

📈 Your input multiplier:             X.Xx
📊 Average per conversation:          XX messages from you

═══ Your Most Active Conversations ═══

 1. 🔥 XXX messages - [Project-Name]
 2. 🔥 XXX messages - [Project-Name]
 3. 🔥 XXX messages - [Project-Name]
```

---

## 🎁 Create Your Wrapped Summary

After running the analysis, you'll have:

1. **Core stats** - Messages, sessions, projects
2. **Time patterns** - When you code most
3. **Top projects** - Where you spent your time
4. **Personality profile** - Your coding style
5. **Fun facts** - Shareable highlights

Perfect for:
- 📱 Social media posts
- 📊 Year-end reflections
- 🎓 Showing students/colleagues
- 💼 Professional portfolios

---

## 🔒 Privacy & Safety

✅ **Read-only** - Never modifies your Claude Code data
✅ **Local only** - All analysis happens on your machine
✅ **No tracking** - No data sent anywhere
✅ **Open source** - Review the code yourself

---

## 📂 What Gets Analyzed?

### Global Data
- `~/.claude/projects/` - Your conversation sessions
- Session metadata (timestamps, file counts)
- Tool usage patterns

### What's NOT Analyzed
- ❌ Actual conversation content
- ❌ Code you wrote
- ❌ Sensitive project details
- ❌ API keys or credentials

---

## 🎯 For Non-Technical Users

**Simple explanation:**

This tool answers: *"How many times did I actually type something to Claude Code?"*

NOT: *"How many system messages/tool calls/events occurred?"*

It's the **clearest metric** for understanding your AI-assisted development journey.

---

## 🤝 Contributing

Found a bug? Have ideas for new metrics? PRs welcome!

Some ideas for contributions:
- Visual charts/graphs
- HTML export for web viewing
- Team/organization analytics
- Integration with git stats
- Year-over-year comparisons

---

## 📚 How It Works

### Data Sources
1. **`~/.claude/projects/`** - Session files (`.jsonl`)
2. **`~/.claude/history.jsonl`** - Command history
3. **Project `.claude/` folders** - Local settings

### Analysis Process
1. Scans for all `.jsonl` conversation files
2. Parses JSON to extract user messages
3. Calculates timestamps, patterns, frequencies
4. Generates human-readable reports

### File Types
- **Main sessions**: `[uuid].jsonl` - Your conversations
- **Agent tasks**: `agent-[uuid].jsonl` - Background processes
- **Excluded**: System files, cache, settings

---

## 🛟 Troubleshooting

**No data found?**
- Make sure you've actually used Claude Code
- Check that `~/.claude/` directory exists
- Verify you're running from correct directory

**Wrong counts?**
- Ensure you're using Claude Code v2.0+ (check `claude --version`)
- Check for corrupted `.jsonl` files
- Verify Python 3.7+ is installed (`python3 --version`)

**Permission errors?**
- Make scripts executable: `chmod +x *.sh`
- Check file permissions in `~/.claude/`

---

## 📦 Requirements

- **Claude Code** installed and used (v2.0+)
- **Python 3.7+** for Python scripts
- **Bash** for shell scripts (macOS/Linux/WSL)
- **Standard Unix tools**: `find`, `wc`, `sort`, `grep`
- No external dependencies - uses only Python standard library!

---

## 🎵 Inspiration

Inspired by Spotify Wrapped's year-end summaries. Because developers deserve to celebrate their AI-assisted coding journeys too!

---

## 📄 License

MIT License - Feel free to use, modify, and share!

---

## 🙏 Acknowledgments

Built with Claude Code (of course!)

Special thanks to the Claude Code team for building an amazing tool.

---


**Made with ❤️ for the Claude Code community**

*Want to share your Wrapped? Tag #ClaudeCodeWrapped!*
