# 🎨 Creating Spotify-Style Animated Visuals

**Want to turn your Wrapped data into shareable animated graphics?**

This guide helps you generate Spotify Wrapped-style animations and visuals from your Claude Code data.

---

## 🎯 Overview

Once you have your Wrapped data, you can create:
- 📱 Animated Instagram/TikTok stories
- 🎥 Video reveals (like Spotify's year-end videos)
- 🖼️ Static social media graphics
- 🎨 Interactive web animations
- 📊 Data visualization dashboards

---

## 🚧 Status: Coming Soon!

**This feature is in development.** We're working on automated generation of visuals.

For now, use the prompts below to manually create animations with AI tools.

---

## 📊 Step 1: Extract Your Data

First, run the analysis to get your stats:

```bash
python3 count_user_inputs.py > my_stats.txt
python3 spotify_wrapped_analysis.py > my_wrapped.txt
```

Or use the full wrapped summary:
```bash
# Your key stats are in:
- WRAPPED_2025.md (detailed)
- SPOTIFY_WRAPPED_2025.md (fun format)
```

---

## 🎨 Step 2: Generate Visuals with AI

### Option A: Using Claude (or any LLM)

Copy this prompt along with your data:

```
I have my Claude Code Wrapped 2025 data. Please help me create Spotify-style animated graphics.

**My Data:**
- Messages typed: [YOUR_NUMBER]
- Conversations: [YOUR_NUMBER]
- Top project: [PROJECT_NAME] ([MESSAGE_COUNT] messages)
- Peak hour: [YOUR_TIME]
- Personality: [YOUR_PERSONALITY]
- Hottest month: [YOUR_MONTH]

**I want to create:**
1. A sequence of 5-6 animated "slides" like Spotify Wrapped
2. Each slide reveals one key stat
3. Style: Bold numbers, fun emojis, gradient backgrounds
4. Format: 1080x1920px (Instagram Story size)

**Please generate:**
1. HTML/CSS/JS code for each animated slide
2. Suggestions for color schemes and fonts
3. Animation timing and transitions
4. Export instructions for video/gif

Make it fun, shareable, and visually striking!
```

### Option B: Using Design Tools

Use the prompt template below with tools like:
- **Midjourney/DALL-E** - For background graphics
- **Figma** - For layout design
- **After Effects** - For animations
- **Canva** - For quick social graphics

---

## 🎬 Animation Prompt Templates

### Template 1: Opening Slide
```
Create an animated opening slide for "Claude Code Wrapped 2025"

Style: Spotify Wrapped aesthetic
- Dark background with vibrant gradient (purple to blue)
- Large bold text: "Your Claude Code Wrapped"
- Subtitle: "2025"
- Animated elements: Sparkles, code symbols floating
- Duration: 2 seconds
- Transition: Fade in

Dimensions: 1080x1920px (vertical)
```

### Template 2: Big Number Reveal
```
Create a "big reveal" slide showing:

Main stat: "[YOUR_NUMBER] Messages"
Subtitle: "That's what YOU actually typed"
Context: "Across [X] deep conversations"

Style:
- Huge number in center
- Counter animation (0 → YOUR_NUMBER)
- Gradient text effect
- Confetti or sparkle particles
- Dark background

Animation: Number counts up over 1.5 seconds
```

### Template 3: Personality Profile
```
Create a personality profile slide:

Title: "Your Coding Personality"
Main text: "[Your Personality Type]"
Description: "[Your personality description based on stats]"

Style:
- Icon/illustration representing "Deep Diver"
- Badge or emblem design
- Stats sidebar
- Animated badge reveal

Colors: Match Spotify's green/purple scheme
```

### Template 4: Timeline Animation
```
Create a timeline visualization:

Title: "Your Hottest Month"
Main stat: "[MONTH] 2025"
Visual: Bar chart or timeline showing:
- Month 1: [X] files
- Month 2: [X] files
- Month 3: [X] files
- Hottest: [X] files (HIGHLIGHTED)
- Month 5: [X] files

Animation: Bars grow sequentially, November bursts with particles
```

### Template 5: Project Showcase
```
Create a "top 3 projects" slide:

Title: "Your Top Projects"

1. 🎨 [Project 1] - [X] messages
2. 💻 [Project 2] - [X] messages
3. 📝 [Project 3] - [X] messages

Style:
- Medal/podium visualization
- Projects appear one by one
- Gold/silver/bronze accents
- Project emojis animate in
```

---

## 🎥 Full Video Sequence

Suggested slide order for a 30-second video:

```
1. Opening (2s)
   "Your Claude Code Wrapped 2025"

2. Days Active (3s)
   "[X] days with Claude Code"

3. Messages Reveal (3s)
   "[YOUR_NUMBER] messages you typed"
   (Counter animation)

4. Top Project (4s)
   "Your biggest project: [PROJECT_NAME]"
   "[X] messages across [X] sessions"

5. Peak Time (3s)
   "You code at [YOUR_TIME]"
   (Clock animation)

6. Personality (4s)
   "You're a [PERSONALITY_TYPE]"
   "[X] messages per session"
   (Badge reveal)

7. Hottest Month (4s)
   "[MONTH] 2025 was 🔥"
   "[X] files created"
   (Chart animation)

8. Fun Fact (3s)
   "You typed [X] words"
   "That's a [X]-page book!"

9. Closing (3s)
   "Share yours: #ClaudeCodeWrapped"
   (Social handle)
```

---

## 🎨 Design Specifications

### Color Palettes

**Spotify Style:**
```
Primary: #1DB954 (Spotify Green)
Secondary: #1ed760
Dark: #121212
Light: #FFFFFF
Accent: #535353
```

**Alternative (Code Theme):**
```
Primary: #007ACC (VS Code Blue)
Secondary: #00D9FF
Dark: #1E1E1E
Purple: #C586C0
Green: #4EC9B0
```

**Gradient Suggestions:**
```
Background: linear-gradient(135deg, #667eea 0%, #764ba2 100%)
Alternative: linear-gradient(to right, #00d2ff 0%, #3a47d5 100%)
Dark: linear-gradient(to bottom, #0f2027, #203a43, #2c5364)
```

### Typography

**Recommended Fonts:**
- Headlines: **Circular** (Spotify's font) or **Montserrat Bold**
- Numbers: **Space Grotesk** or **Inter Bold**
- Body: **Inter** or **SF Pro**

**Size Guidelines (1080x1920):**
- Main number: 120-180px
- Title: 60-80px
- Subtitle: 32-40px
- Body: 24-28px

### Animation Timing

**Principles:**
- Reveal: 0.5-1s
- Dwell: 2-3s per slide
- Transition: 0.3-0.5s
- Total video: 25-35s

---

## 🛠️ Technical Implementation

### HTML/CSS/JS Starter

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .slide {
            width: 1080px;
            height: 1920px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            font-family: 'Montserrat', sans-serif;
            color: white;
        }

        .big-number {
            font-size: 160px;
            font-weight: bold;
            animation: countUp 1.5s ease-out;
        }

        .subtitle {
            font-size: 36px;
            margin-top: 20px;
            opacity: 0;
            animation: fadeIn 0.5s ease-in 1.5s forwards;
        }

        @keyframes countUp {
            from { opacity: 0; transform: scale(0.5); }
            to { opacity: 1; transform: scale(1); }
        }

        @keyframes fadeIn {
            to { opacity: 1; }
        }
    </style>
</head>
<body>
    <div class="slide">
        <div class="big-number" id="counter">0</div>
        <div class="subtitle">Messages You Typed</div>
    </div>

    <script>
        // Counter animation
        const counter = document.getElementById('counter');
        const target = YOUR_MESSAGE_COUNT; // Replace with your actual count
        const duration = 1500;
        const steps = 60;
        const increment = target / steps;
        let current = 0;

        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                counter.textContent = target.toLocaleString();
                clearInterval(timer);
            } else {
                counter.textContent = Math.floor(current).toLocaleString();
            }
        }, duration / steps);
    </script>
</body>
</html>
```

### Using Python for Frames

```python
# Generate individual frames for video export
from PIL import Image, ImageDraw, ImageFont

def create_slide(stat, value, subtitle):
    img = Image.new('RGB', (1080, 1920), color='#667eea')
    draw = ImageDraw.Draw(img)

    # Load fonts
    font_big = ImageFont.truetype('Montserrat-Bold.ttf', 160)
    font_small = ImageFont.truetype('Montserrat-Regular.ttf', 36)

    # Draw text centered
    draw.text((540, 800), value, font=font_big, fill='white', anchor='mm')
    draw.text((540, 1000), subtitle, font=font_small, fill='white', anchor='mm')

    return img

# Generate frames
slide1 = create_slide('Messages', 'YOUR_COUNT', 'What you actually typed')
slide1.save('frame_01.png')
```

---

## 📱 Export Formats

### For Instagram Stories
- Size: 1080x1920px
- Format: MP4 or GIF
- Duration: Max 15s per story
- Aspect ratio: 9:16

### For Twitter/X
- Size: 1200x675px (landscape) or 1080x1920px (portrait)
- Format: MP4, GIF
- Duration: Max 2:20
- File size: <512MB

### For TikTok
- Size: 1080x1920px
- Format: MP4
- Duration: 15-60s recommended
- Aspect ratio: 9:16

### For LinkedIn
- Size: 1200x627px (landscape)
- Format: MP4, native video
- Duration: 30s-3min
- Professional tone

---

## 🎬 Video Creation Tools

### Free Options
- **Canva** - Templates for social graphics
- **Kapwing** - Online video editor
- **OpenShot** - Free video editor
- **GIMP** - Image editing
- **Blender** - Advanced 3D/animation (steep learning curve)

### Paid Options
- **After Effects** - Professional animation
- **Premiere Pro** - Video editing
- **Final Cut Pro** - Mac video editing
- **Figma** - Design + simple animations

---

## 🤖 AI-Assisted Generation Prompt

**For Claude, ChatGPT, or other LLMs:**

```
I want to create animated Spotify Wrapped-style graphics for my Claude Code usage.

**My stats:**
[Paste your SPOTIFY_WRAPPED_2025.md content here]

**Please generate:**

1. **Complete HTML file** with:
   - 6 animated slides
   - Slide 1: Opening ("Your Claude Code Wrapped 2025")
   - Slide 2: Messages count with counter animation
   - Slide 3: Top project reveal
   - Slide 4: Peak coding time with clock visual
   - Slide 5: Personality profile badge
   - Slide 6: Fun fact + sharing CTA

2. **CSS for**:
   - Spotify-inspired gradient backgrounds
   - Smooth slide transitions
   - Number counter animations
   - Fade in/out effects
   - Mobile responsive (1080x1920)

3. **JavaScript for**:
   - Auto-advance slides (3s each)
   - Counter animations
   - Particle effects
   - Progress indicator

4. **Instructions to**:
   - Capture as video using browser tools
   - Export as individual PNG frames
   - Create GIF version
   - Optimize for social media

Style: Bold, colorful, fun - like Spotify Wrapped!
Make the numbers pop, use emojis, add sparkle effects!
```

---

## 🎨 Coming Soon

We're working on:
- ✨ Automated slide generator from your data
- 🎥 One-click video export
- 📱 Pre-made templates for each stat
- 🎨 Customizable themes and colors
- 🌐 Web-based animation builder
- 📤 Direct social media sharing

**Want to help?** Check out [CONTRIBUTING.md](CONTRIBUTING.md)!

---

## 💡 Ideas & Inspiration

**Examples to inspire your visuals:**
- Spotify Wrapped (the OG!)
- GitHub's year in review
- Strava's year end summaries
- Duolingo year in review
- Apple Music Replay

**Visual elements to include:**
- Progress bars
- Counter animations
- Confetti/particle effects
- Badge reveals
- Chart animations
- Timeline scrubbing
- Emoji bursts
- Gradient backgrounds
- Glitch effects

---

## 📤 Sharing Your Creations

Once you create visuals:

1. **Post with hashtag**: #ClaudeCodeWrapped
2. **Tag us** (if we have social presence)
3. **Share in Issues** - Show off your designs!
4. **Contribute templates** - Help others create theirs

---

## 🙏 Community Contributions

Have you created amazing visuals? Share them!

- Submit templates via PR
- Post examples in Discussions
- Share your animation code
- Create tutorial videos

Let's build a gallery of amazing Wrapped visuals together!

---

**Remember:** The goal is to make your AI coding journey fun, visual, and shareable. Get creative! 🎨

🎵 *"This is your year. This is your code. This is your Wrapped."* 🎵
