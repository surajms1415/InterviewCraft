import json

filepath = r'c:\Users\91866\.gemini\antigravity\scratch\prepforge-ai\data\gd_topics.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_topics = [
    {
        "id": 1,
        "title": "Artificial Intelligence (AI)",
        "points": [
            "AI is transforming industries like healthcare, finance, and education.",
            "It increases efficiency by automating repetitive tasks.",
            "AI improves decision-making using data analysis.",
            "However, it may lead to job displacement in some sectors.",
            "AI-powered tools like chatbots enhance customer service.",
            "Ethical concerns include bias and lack of transparency.",
            "AI is crucial for future technologies like self-driving cars.",
            "It enables personalized experiences (recommendations, ads).",
            "Governments need regulations for responsible AI use.",
            "Overall, AI is powerful but must be used responsibly."
        ]
    },
    {
        "id": 2,
        "title": "Social Media — Boon or Bane",
        "points": [
            "Social media connects people globally.",
            "It helps in sharing information quickly.",
            "Useful for education and awareness campaigns.",
            "However, it can cause addiction.",
            "Spreads misinformation easily.",
            "Impacts mental health negatively in many cases.",
            "Helps businesses in marketing and branding.",
            "Privacy concerns are increasing.",
            "Influences opinions and elections.",
            "Balance in usage is very important."
        ]
    },
    {
        "id": 3,
        "title": "Online Education VS Offline Education",
        "points": [
            "Online education offers flexibility.",
            "Accessible from anywhere.",
            "Cost-effective compared to offline learning.",
            "Lacks face-to-face interaction.",
            "Offline education builds discipline and routine.",
            "Practical learning is better offline.",
            "Online platforms provide global resources.",
            "Internet access is a limitation.",
            "Hybrid model is the future.",
            "Both have pros and cons depending on context."
        ]
    },
    {
        "id": 4,
        "title": "Is India Ready for Digital Economy?",
        "points": [
            "India is rapidly growing in digital infrastructure.",
            "UPI revolutionized digital payments.",
            "Internet penetration is increasing.",
            "Rural areas still lack proper access.",
            "Cybersecurity is a major concern.",
            "Government initiatives like Digital India help growth.",
            "Startups are boosting innovation.",
            "Digital literacy is still low in some regions.",
            "Data privacy laws are evolving.",
            "India is progressing but needs improvement."
        ]
    },
    {
        "id": 5,
        "title": "Work From Home — Good or Bad",
        "points": [
            "Increases flexibility for employees.",
            "Saves travel time and cost.",
            "Improves work-life balance for many.",
            "Reduces office infrastructure cost.",
            "Can reduce productivity in some cases.",
            "Causes communication challenges.",
            "Leads to isolation and less teamwork.",
            "Suitable for IT and tech roles.",
            "Hybrid work is becoming popular.",
            "Depends on job type and individual discipline."
        ]
    },
    {
        "id": 6,
        "title": "Impact of Technology on Jobs",
        "points": [
            "Technology creates new job opportunities.",
            "Automation replaces repetitive jobs.",
            "Demand for skilled professionals increases.",
            "Requires continuous learning.",
            "AI and ML are reshaping industries.",
            "Gig economy is growing.",
            "Job roles are evolving rapidly.",
            "Digital skills are essential now.",
            "Some traditional jobs are disappearing.",
            "Overall impact is both positive and challenging."
        ]
    },
    {
        "id": 7,
        "title": "Should Students Focus on Skills or Marks?",
        "points": [
            "Skills are more important in real-world jobs.",
            "Marks help in shortlisting during placements.",
            "Practical knowledge matters more than theory.",
            "Skills improve problem-solving ability.",
            "Companies prefer skilled candidates.",
            "Marks reflect academic discipline.",
            "Balance between both is ideal.",
            "Skills help in long-term career growth.",
            "Projects and internships build skills.",
            "Final success depends on ability, not just marks."
        ]
    },
    {
        "id": 8,
        "title": "Startups VS MNCs",
        "points": [
            "Startups offer learning opportunities.",
            "MNCs provide job security.",
            "Startups have fast growth environment.",
            "MNCs offer structured career path.",
            "Startups involve more responsibilities.",
            "MNCs provide better work-life balance.",
            "Risk is higher in startups.",
            "Innovation is higher in startups.",
            "Salary may be higher in MNCs initially.",
            "Choice depends on individual goals."
        ]
    },
    {
        "id": 9,
        "title": "Role of Youth in Nation Building",
        "points": [
            "Youth are the backbone of a nation.",
            "They bring innovation and energy.",
            "Can drive economic growth.",
            "Important for social change.",
            "Should focus on education and skills.",
            "Need awareness about social issues.",
            "Can promote digital transformation.",
            "Responsible citizenship is important.",
            "Youth participation in politics is increasing.",
            "They shape the future of the country."
        ]
    },
    {
        "id": 10,
        "title": "Climate Change",
        "points": [
            "Climate change is a global issue.",
            "Caused by pollution and human activities.",
            "Leads to global warming.",
            "Affects agriculture and weather patterns.",
            "Causes natural disasters.",
            "Renewable energy is a solution.",
            "Government policies are important.",
            "Individual responsibility matters.",
            "Awareness is increasing worldwide.",
            "Urgent action is required."
        ]
    }
]

data['topics'] = new_topics

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print("Updated GD Topics successfully.")
