from EmotionDetection import emotion_detector

def test_emotion_detection():
    test_cases = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for text, expected_emotion in test_cases.items():
        response = emotion_detector(text)
        dominant_emotion = response["dominant_emotion"]

        print(f"Input: {text}")
        print(f"Expected: {expected_emotion}")
        print(f"Detected: {dominant_emotion}")

        assert dominant_emotion == expected_emotion

    print("All test cases passed!")

if __name__ == "__main__":
    test_emotion_detection()