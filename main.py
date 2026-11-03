import random

MAX_TRIES = 5
LOW, HIGH = 1, 100
RANKS = {
    1: "نمونه‌ای",
    2: "بسیار خوبی",
    3: "خوب",
    4: "قبول",
    5: "با شانس بردی!",
}


def get_guess():
    """تا وقتی ورودی معتبر (عدد ۱ تا ۱۰۰) نباشد دوباره می‌پرسد."""
    while True:
        text = input(f"حدس خود را وارد کن ({LOW} تا {HIGH}): ").strip()
        try:
            guess = int(text)
        except ValueError:
            print("ورودی نامعتبر است؛ لطفاً فقط عدد وارد کن.")
            continue
        if guess < LOW or guess > HIGH:
            print(f"عدد باید بین {LOW} تا {HIGH} باشد.")
            continue
        return guess


def closeness_hint(diff):
    if diff <= 5:
        return "خیلی نزدیکی!"
    elif diff <= 15:
        return "نزدیکی، ولی هنوز فاصله داری!"
    else:
        return "خیلی دوری!"


def play_round():
    secret = random.randint(LOW, HIGH)

    for attempt in range(1, MAX_TRIES + 1):
        print(f"\nتلاش {attempt} از {MAX_TRIES}")
        print(f"جان باقی‌مانده: {MAX_TRIES - attempt + 1}")

        guess = get_guess()

        if guess == secret:
            print("آفرین! درست حدس زدی، برنده شدی!")
            print(f"رتبه تو: {RANKS[attempt]}")
            return

        if guess > secret:
            direction = "کوچک‌تر وارد کن"
        else:
            direction = "بزرگ‌تر وارد کن"
        print(f"{direction} - {closeness_hint(abs(guess - secret))}")

    print("\nمتأسفانه باختی!")
    print(f"عدد مخفی {secret} بود.")


def ask_play_again():
    while True:
        answer = input("\nمی‌خواهی دوباره بازی کنی؟ (بله/خیر): ").strip()
        if answer in ("بله", "آره", "y", "Y", "yes", "Yes"):
            return True
        if answer in ("خیر", "نه", "n", "N", "no", "No"):
            return False
        print("لطفاً فقط «بله» یا «خیر» وارد کن.")


def main():
    print("به بازی حدس عدد خوش آمدی!")
    while True:
        play_round()
        if not ask_play_again():
            print("خداحافظ!")
            break


if __name__ == "__main__":
    main()
