from main import setup_moods, mood_loop
setup_moods()

mood_loop("angry", True, 5000)
mood_loop("happy", True, 5000)
mood_loop("neutral", True, -1)
mood_loop("happy", True, 5000)
