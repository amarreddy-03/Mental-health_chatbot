responses = {

    "hello": "Hello! 😊 How are you feeling today?",

    "hi": "Hi! I'm here to listen. Tell me how you're feeling.",

    "hey": "Hey! Welcome to MindCare. 😊",

    "good morning": "Good morning! I hope you have a wonderful day.",

    "good afternoon": "Good afternoon! Take care of yourself today.",

    "good evening": "Good evening! How was your day?",

    "happy": "That's wonderful! 😊 Keep smiling and enjoy your day.",

    "sad": "I'm sorry you're feeling sad. Talking to someone you trust or doing something you enjoy may help.",

    "stress": "Take a deep breath. Try studying or working for 25 minutes, then take a 5-minute break.",

    "stressed": "It's okay to feel stressed sometimes. Take a short break, drink water, and breathe slowly.",

    "anxiety": "Slow breathing and grounding exercises can help reduce anxiety. Remember, you're not alone.",

    "angry": "Take a few deep breaths before reacting. A short walk can also help.",

    "lonely": "You're not alone. Consider reaching out to a trusted friend or family member.",

    "tired": "Your body may need some rest. Try getting enough sleep and staying hydrated.",

    "sleep": "Aim for 7–8 hours of sleep every night. Avoid screens before bedtime.",

    "exam": "Exams can be stressful. Study in small sessions and remember to take breaks.",

    "study": "Stay focused by studying in short sessions and reviewing regularly.",

    "motivation": "Believe in yourself. Every small step you take brings you closer to your goal.",

    "failure": "Failure is part of learning. Every successful person has faced setbacks.",

    "success": "Congratulations! Celebrate your achievement and keep growing.",

    "friends": "Good friends can make difficult days easier. Stay connected with people you trust.",

    "family": "Family support can be valuable. Don't hesitate to share your feelings with them.",

    "cry": "It's okay to cry. Expressing emotions is natural and healthy.",

    "alone": "Even if you feel alone, there are people who care about you. Reach out if you can.",

    "overthinking": "Try focusing on one thing at a time. Deep breathing and writing your thoughts may help.",

    "fear": "Facing fears one step at a time can help build confidence.",

    "confused": "Take a short break and organize your thoughts. Solving one problem at a time often helps.",

    "bored": "Try reading a book, listening to music, going for a walk, or learning something new.",

    "music": "Listening to calm music can help improve your mood.",

    "exercise": "Regular exercise can improve both physical and mental well-being.",

    "meditation": "Meditation for even 10 minutes can help reduce stress.",

    "thank you": "You're welcome! 😊 I'm always here to listen.",

    "thanks": "Happy to help! Take care and stay positive.",

    "bye": "Goodbye! Take care of yourself and have a wonderful day. 👋"
}


def get_response(user_input):

    user_input = user_input.lower()

    for keyword in responses:

        if keyword in user_input:
            return responses[keyword]

    return (
        "I'm here to listen. ❤️ "
        "Could you tell me a little more about how you're feeling?"
    )