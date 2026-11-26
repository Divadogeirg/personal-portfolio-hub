from flask import Flask, render_template

app = Flask(__name__)


@app.route("/") # Maps root URL to the home() function. Whenever a browser visits, / Flask runs home()
def home():
    profile_data = {
        "name": "David Griego III",
        "headline": "Computer Science Undergraduate at UTEP | U.S. Army Veteran",
        "bio": "Building software, hardware logic designs, and live streaming integrations.",
        "github_url": "https://github.com/divadogeirg",
        "linkedin_url": "https://www.linkedin.com/in/david-griego-028680161",
        "youtube_url": "https://www.youtube.com/@Divadogeirg",
        "twitch_url": "https://www.twitch.tv/",
    }

    projects = [
        {
            "title": "Mecha_m0d (AI Twitch Co-Host)",
            "stack": "Python, Google GenAI SDK",
            "summary": "Modular Twitch chat bot and AI co-host split across AICoHost.py and bot.py.",
            "repo_url": "https://github.com/divadogeirg",
        },
        {
            "title": "Digital Logic & FPGA Designs",
            "stack": "Verilog, Xilinx Vivado",
            "summary": "Combinational and sequential circuits with simulation testbenches.",
            "repo_url": "https://github.com/divadogeirg",
        },
        # {
        #     "title": "Portfolio Website",
        #     "stack": "Flask, HTML, CSS",
        #     "summary": "Personal portfolio website built with Flask and deployed on Render.",
        #     "repo_url": "https://github.com/divadogeirg/portfolio-website"
        # }
    ]

    return render_template("index.html", profile=profile_data, projects=projects)


if __name__ == "__main__":
    app.run(debug=True) # Make False to publish