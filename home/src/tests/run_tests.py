import sys
import traceback
import os

# Add the parent directory to sys.path so Python can find summarizer.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_summary_basic():
    from summarizer import summarize_text

    input_text = (
        "Machine learning is a field of computer science that gives computers the ability "
        "to learn without being explicitly programmed. It is seen as a subset of artificial intelligence."
    )
    summary = summarize_text(input_text)
    assert isinstance(summary, str), "Summary should be a string"
    assert len(summary) > 10, "Summary should not be empty or too short"


def test_summary_empty():
    from summarizer import summarize_text

    summary = summarize_text("")
    assert summary.startswith("⚠️"), "Empty input should return warning"


def run_all_tests():
    try:
        print("🧪 Running tests...")
        test_summary_basic()
        print("✅ test_summary_basic passed.")
        test_summary_empty()
        print("✅ test_summary_empty passed.")
        print("🎉 All tests passed.")
    except AssertionError as e:
        print(f"❌ Assertion failed: {e}")
        sys.exit(1)
    except Exception:
        print("❌ An unexpected error occurred:")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    run_all_tests()
